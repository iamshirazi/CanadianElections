# Copyright (c) 2025 Matthew Shirazi

import geopandas as gpd
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.pyplot as plt
import pandas as pd
import parliament_charts
import generateHtmlMapFiles

# COLOURS
Liberal = '#EE3224'  # (238, 50, 36)
Progressive_Conservative = '#0F2D52'  # (15, 45, 82)
CC_Federation = '#FF9900'
Social_Credit = '#005F00'
Independent = '#847e7e'
Liberal_Progressive = '#00DCB0'
Liberal_Labour = '#A91CB9'

PROGRESSIVE_CONSERVATIVE_SEATS = 41
LIBERAL_SEATS = 191
CC_FEDERATION_SEATS = 13
SOCIAL_CREDIT_SEATS = 10
INDEPENDENT_SEATS = 5
LIBERAL_PROGRESSIVE_SEATS = 1
LIBERAL_LABOUR_SEATS = 1

# read shapefile
districts = gpd.read_file("districts2/CBF_RO1947_CSRS.shp")
districts['id'] = districts['id'].astype(int)

## Simplifiy district shapes to increase loading speed
districts["geometry"] = (districts.to_crs(districts.estimate_utm_crs()).simplify(20).to_crs(districts.crs))


dataframe2 = districts.sort_values('fedname')
dataframe2.reset_index(drop=True, inplace=True)

votes = pd.read_csv("voting_data/Canada1949.txt", sep=" ", header=0)

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
with open('voting_data/Canada1949.txt') as file:

    for _ in range(1):
        next(file)  # SKIP FIRST LINE

    for line in file:
        # Removes new line symbol and splits the votes
        line = line[:-1].split()

        if len(line) != 0:
            results = [int(line[3]), int(line[4]), int(line[5]), int(line[6]), int(line[7]), int(line[8]), int(line[9])]

        winner = 0

        for i in range(0, 7):
            if results[i] > winner:
                winner = int(results[i])
        

        if winner == int(results[0]):
            colour.append(Progressive_Conservative)
            win.append("Progressive Conservative")
        elif winner == int(results[1]):
            colour.append(Liberal)
            win.append("Liberal")
        elif winner == int(results[2]):
            colour.append(CC_Federation)
            win.append("Co-operative Commonwealth")
        elif winner == int(results[3]):
            colour.append(Social_Credit)
            win.append("Social Credit")
        elif winner == int(results[4]):
            colour.append(Independent)
            win.append("Independent")
        elif winner == int(results[5]):
            colour.append(Liberal_Progressive)
            win.append("Liberal-Progressive")
        elif winner == int(results[6]):
            colour.append(Liberal_Progressive)
            win.append("Liberal-Labour Party")
        else:
            continue
        
## DEBUG
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# print(dataframe3[["fedname", "Riding"]])

total_seats = (PROGRESSIVE_CONSERVATIVE_SEATS + LIBERAL_SEATS + CC_FEDERATION_SEATS + SOCIAL_CREDIT_SEATS + INDEPENDENT_SEATS + LIBERAL_PROGRESSIVE_SEATS + LIBERAL_LABOUR_SEATS)

sorted_parliament_seats = parliament_charts.create_parliament_seating_plan_1949(PROGRESSIVE_CONSERVATIVE_SEATS, LIBERAL_SEATS, CC_FEDERATION_SEATS, SOCIAL_CREDIT_SEATS, INDEPENDENT_SEATS, LIBERAL_PROGRESSIVE_SEATS, LIBERAL_LABOUR_SEATS)

parliament_chart = parliament_charts.generateParliamentChart(total_seats, sorted_parliament_seats)

with open("pages/main/parliament_charts/parl_chart1949.html", "w") as file:
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
    cmap=['#FF9900', '#847e7e', '#EE3224', '#A91CB9', '#00DCB0', '#0F2D52', '#005F00'],
    style_kwds=dict(color="black"), #use black outline
)

foliumMap.save("./pages/elections/election1949.html")

### Generate election page in main folder
generateHtmlMapFiles.generateElectionMapFile(1949)
