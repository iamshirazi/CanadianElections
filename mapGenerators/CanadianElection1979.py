# Copyright (c) 2026 Matthew Shirazi

import geopandas as gpd
import pandas as pd
import parliament_charts
import generateHtmlMapFiles

# COLOURS
Liberal = '#EE3224'  # (238, 50, 36)
Progressive_Conservative = '#0F2D52'  # (15, 45, 82)
Social_Credit = '#005F00'
New_Democratic = '#F58220'

PROGRESSIVE_CONSERVATIVE_SEATS = 136
LIBERAL_SEATS = 114
NEW_DEMOCRATIC_SEATS = 26
SOCIAL_CREDIT_SEATS = 6

# read shapefile
districts = gpd.read_file("districts2/CBF_RO1976_CSRS.shp")
districts['id'] = districts['id'].astype(int)

## Simplifiy district shapes to increase loading speed
districts["geometry"] = (districts.to_crs(districts.estimate_utm_crs()).simplify(20).to_crs(districts.crs))

# ************************************************************************************ #
### SIMPLIFY NUNATSIAQ SHAPE SIZE BY 100, MERGE INTO districts DATAFRAME WHERE ALL OTHER DISTRICTS ARE SIMPLIFIED BY 20
nunatsiaq_district = districts[districts['id'] == 61002]

nunatsiaq_district["geometry"] = nunatsiaq_district.to_crs(
    nunatsiaq_district.estimate_utm_crs()).simplify(100).to_crs(nunatsiaq_district.crs)

new_attributes = nunatsiaq_district.iloc[0].drop('geometry')

merged_geometry = nunatsiaq_district.geometry.union_all()
new_row = gpd.GeoSeries([merged_geometry], crs=districts.crs, name='geometry')
new_row_gdf = gpd.GeoDataFrame(new_attributes.to_frame().T, geometry=new_row)

new_row_gdf['geometry'] = merged_geometry

gdf_updated = districts.drop(nunatsiaq_district.index)

districts_new = pd.concat([gdf_updated, new_row_gdf], ignore_index=True)
# ************************************************************************************ #

dataframe2 = districts_new.sort_values('fedname')
dataframe2.reset_index(drop=True, inplace=True)

votes = pd.read_csv("voting_data/Canada1979.txt", sep=" ", header=0)

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
with open('voting_data/Canada1979.txt') as file:

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
            colour.append(Progressive_Conservative)
            win.append("Progressive Conservative")
        elif winner == int(results[1]):
            colour.append(Liberal)
            win.append("Liberal")
        elif winner == int(results[2]):
            colour.append(New_Democratic)
            win.append("New Democratic")
        elif winner == int(results[3]):
            colour.append(Social_Credit)
            win.append("Social Credit")
        else:
            continue
        
## DEBUG
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# print(dataframe3[["fedname", "Riding"]])

total_seats = (PROGRESSIVE_CONSERVATIVE_SEATS + LIBERAL_SEATS + NEW_DEMOCRATIC_SEATS + SOCIAL_CREDIT_SEATS)

sorted_parliament_seats = parliament_charts.create_parliament_seating_plan_1979(PROGRESSIVE_CONSERVATIVE_SEATS, LIBERAL_SEATS, NEW_DEMOCRATIC_SEATS, SOCIAL_CREDIT_SEATS)

parliament_chart = parliament_charts.generateParliamentChart(total_seats, sorted_parliament_seats)

with open("pages/main/parliament_charts/parl_chart1979.html", "w") as file:
    generic_lines = "<!DOCTYPE html>\n<html>\n<head>\n\t<link rel='stylesheet' href='/main/elections_style.css'>\n</head>\n</head>\n<body>\n"
    file.writelines(generic_lines)
    file.writelines(parliament_chart)
    file.writelines("</body>\n</html>")

## DROP UNNECESSARY COLUMNS IN DATAFRAME:
dataframe3 = dataframe3.drop(['OBJECTID', 'id', 'fedname', 'fedid', 'Shape_Area'], axis=1)

## Colour the ridings
dataframe3["Party"] = win
dataframe3['color'] = colour

foliumMap = dataframe3.explore(
    column="Party", # make choropleth vased on winner in column
    tooltip=["Riding", "Party", "winner", "loser"], # show all party votes for a riding when hovering over it
    popup=True, # show all values of a riding when you click it
    tiles="CartoDB positron", # use "CartoDB positron" tiles
    cmap=['#EE3224', '#F58220', '#0F2D52', '#005F00'],
    style_kwds=dict(color="black"), #use black outline
)

foliumMap.save("./pages/elections/election1979.html")


### Generate election page in main folder
generateHtmlMapFiles.generateElectionMapFile(1979)
