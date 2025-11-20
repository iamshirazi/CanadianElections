# Copyright (c) 2025 Matthew Shirazi

import geopandas as gpd
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.pyplot as plt
import pandas as pd
import parliament_charts

# COLOURS
Liberal = '#EE3224'  # (238, 50, 36)
Conservative = '#0F2D52'  # (15, 45, 82)
Social_Credit = '#005F00'
CC_Federation = '#FF9900'
Liberal_Progressive = '#00DCB0'
Independent = '#847e7e'
Reconstruction = '#F5F5DC'
UF_Ontario = '#C0BD07'

CONSERVATIVE_SEATS = 39
LIBERAL_SEATS = 173
SOCIAL_CREDIT_SEATS = 17
CC_FEDERATION_SEATS = 7
LIBERAL_PROGRESSIVE_SEATS = 4
INDEPENDENT_SEATS = 3
RECONSTRUCTION_SEATS = 1
UF_ONTARIO_SEATS = 1

# read shapefile
districts = gpd.read_file("districts2/CBF_RO1933_CSRS.shp")
districts['id'] = districts['id'].astype(int)

## Simplifiy district shapes to increase loading speed
districts["geometry"] = (districts.to_crs(districts.estimate_utm_crs()).simplify(20).to_crs(districts.crs))


dataframe2 = districts.sort_values('fedname')
dataframe2.reset_index(drop=True, inplace=True)

votes = pd.read_csv("voting_data/Canada1935.txt", sep=" ", header=0)

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
with open('voting_data/Canada1935.txt') as file:

    for _ in range(1):
        next(file)  # SKIP FIRST LINE

    for line in file:
        # Removes new line symbol and splits the votes
        line = line[:-1].split()

        if len(line) != 0:
            results = [int(line[3]), int(line[4]), int(line[5]), int(line[6]), int(line[7]), int(line[8]), int(line[9]), int(line[10])]

        winner = 0

        for i in range(0, 8):
            if results[i] > winner:
                winner = int(results[i])
        

        if winner == int(results[0]):
            colour.append(Conservative)
            win.append("Conservative")
        elif winner == int(results[1]):
            colour.append(Liberal)
            win.append("Liberal")
        elif winner == int(results[2]):
            colour.append(Social_Credit)
            win.append("Social Credit")
        elif winner == int(results[3]):
            colour.append(CC_Federation)
            win.append("Co-operative Commonwealth")
        elif winner == int(results[4]):
            colour.append(Liberal_Progressive)
            win.append("Liberal-Progressive")
        elif winner == int(results[5]):
            colour.append(Independent)
            win.append("Independent")
        elif winner == int(results[6]):
            colour.append(Reconstruction)
            win.append("Reconstruction Party")
        elif winner == int(results[7]):
            colour.append(UF_Ontario)
            win.append("United Farmers of Ontario")
        else:
            continue
        
## DEBUG
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# print(dataframe3[["fedname", "Riding"]])

total_seats = (CONSERVATIVE_SEATS + LIBERAL_SEATS + SOCIAL_CREDIT_SEATS + CC_FEDERATION_SEATS + LIBERAL_PROGRESSIVE_SEATS + INDEPENDENT_SEATS + RECONSTRUCTION_SEATS + UF_ONTARIO_SEATS)

sorted_parliament_seats = parliament_charts.create_parliament_seating_plan_1935(CONSERVATIVE_SEATS, LIBERAL_SEATS, SOCIAL_CREDIT_SEATS, CC_FEDERATION_SEATS, LIBERAL_PROGRESSIVE_SEATS, INDEPENDENT_SEATS, RECONSTRUCTION_SEATS, UF_ONTARIO_SEATS)

parliament_chart = parliament_charts.generateParliamentChart(total_seats, sorted_parliament_seats)

with open("pages/main/parliament_charts/parl_chart1935.html", "w") as file:
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
    cmap=['#FF9900', '#0F2D52', '#847e7e', '#EE3224', '#00DCB0', '#F5F5DC', '#005F00', '#C0BD07'],
    style_kwds=dict(color="black"), #use black outline
)

foliumMap.save("./pages/elections/election1935.html")
