# Copyright (c) 2025 Matthew Shirazi

import geopandas as gpd
import pandas as pd
import parliament_charts
import generateHtmlMapFiles

# COLOURS
Lib = '#EE3224'  # (238, 50, 36)
Con = '#0F2D52'  # (15, 45, 82)
Independent = '#847e7e'
NationalistCon = '#800080'

CON_SEATS = 117
LIB_SEATS = 90
INDEPENDENT_SEATS = 6
NATIONALIST_SEATS = 2

# read shapefile
districts = gpd.read_file("/app/CBF_RO1882_CSRS.shp")
districts['id'] = districts['id'].astype(int)

# ************************************************************************************ #
####### MERGE THE TERRITORIES CLAIMED BY ONTARIO FOR THIS ELECTION (GIVEN TO ONTARIO IN 1889) - PRE WORK ######
rows_to_merge = districts[districts['fedname'].isin(['Algoma', 'Claimed by Ontario (awarded 1889)', 'Disputed Territories (Awarded to Ontario 1889)'])]

new_attributes = rows_to_merge.iloc[0].drop('geometry')
new_attributes['fedname'] = "Algoma"

merged_geometry = rows_to_merge.geometry.unary_union
new_row = gpd.GeoSeries([merged_geometry], crs=districts.crs, name='geometry')
new_row_gdf = gpd.GeoDataFrame(new_attributes.to_frame().T, geometry=new_row)

new_row_gdf['geometry'] = merged_geometry

gdf_updated = districts.drop(rows_to_merge.index)

districts_new = pd.concat([gdf_updated, new_row_gdf], ignore_index=True)
# ************************************************************************************ #

## Simplifiy district shapes to increase loading speed
districts_new["geometry"] = (districts_new.to_crs(districts_new.estimate_utm_crs()).simplify(20).to_crs(districts_new.crs))

dataframe2 = districts_new.sort_values('fedname')
dataframe2.reset_index(drop=True, inplace=True)

votes = pd.read_csv("voting_data/Canada1891.txt", sep=" ", header=0)

## Merge district shapes and number of votes
dataframe3 = pd.concat([dataframe2, votes], axis=1)

colour = []
win = []

## FOR DEBUGGING
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# print(dataframe2[['id','fedname']])

## FOR TESTING, JUST FILL COLOUR AND WIN WITH LIBERAL TO SEE COLOUR
# for i in range(181):
#     colour.append(Lib)
#     win.append("Liberal")


# read file with voting results
with open('voting_data/Canada1891.txt') as file:

    for _ in range(1):
        next(file)  # SKIP FIRST LINE

    for line in file:
        # Removes new line symbol and splits the votes
        line = line[:-1].split()

        if len(line) != 0:
            results = [int(line[3]), int(line[4]), int(line[5]), int(line[6])]

        winner = 0

        for i in range(0, 4):
            if results[i] > winner:
                winner = int(results[i])

        if winner == int(results[0]):
            colour.append(Con)
            win.append("Conservative")
        elif winner == int(results[1]):
            colour.append(Lib)
            win.append("Liberal")
        elif winner == int(results[2]):
            colour.append(Independent)
            win.append("Independent")
        else:
            colour.append(NationalistCon)
            win.append("Nationalist Conservative")
            
        
## DEBUG
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# print(dataframe3[["fedname", "Riding"]])


total_seats = (CON_SEATS + LIB_SEATS + INDEPENDENT_SEATS + NATIONALIST_SEATS)

sorted_parliament_seats = parliament_charts.create_parliament_seating_plan_1878(CON_SEATS, LIB_SEATS, INDEPENDENT_SEATS, NATIONALIST_SEATS)

parliament_chart = parliament_charts.generateParliamentChart(total_seats, sorted_parliament_seats)

with open("pages/main/parliament_charts/parl_chart1891.html", "w") as file:
    generic_lines = "<!DOCTYPE html>\n<html>\n<head>\n\t<link rel='stylesheet' href='/main/elections_style.css'>\n</head>\n</head>\n<body>\n"
    file.writelines(generic_lines)
    file.writelines(parliament_chart)
    file.writelines("</body>\n</html>")

## DROP UNNECESSARY COLUMNS IN DATAFRAME:
dataframe3 = dataframe3.drop(['OBJECTID', 'id', 'fedname', 'fedid', 'areatotal', 'arealand', 'areawater'], axis=1)

## Colour the ridings
dataframe3["Party"] = win
dataframe3['color'] = colour

foliumMap = dataframe3.explore(
    column="Party", # make choropleth vased on winner in column
    tooltip=["Riding", "Party", "winner", "loser"], # show all party votes for a riding when hovering over it
    popup=True, # show all values of a riding when you click it
    tiles="CartoDB positron", # use "CartoDB positron" tiles
    cmap=['#0F2D52', '#847e7e', '#EE3224', '#800080'],
    style_kwds=dict(color="black"), #use black outline
)

foliumMap.save("./pages/elections/election1891.html")

### Generate election page in main folder
generateHtmlMapFiles.generateElectionMapFile(1891)
