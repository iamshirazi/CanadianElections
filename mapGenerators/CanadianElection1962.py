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
Social_Credit = '#005F00'
New_Democratic = '#F58220'
Liberal_Labour = '#A91CB9'

PROGRESSIVE_CONSERVATIVE_SEATS = 116
LIBERAL_SEATS = 99
SOCIAL_CREDIT_SEATS = 30
NEW_DEMOCRATIC_SEATS = 19
LIBERAL_LABOUR_SEATS = 1

# read shapefile
districts = gpd.read_file("districts2/CBF_RO1952_CSRS.shp")
districts['id'] = districts['id'].astype(int)

## Simplifiy district shapes to increase loading speed
districts["geometry"] = (districts.to_crs(districts.estimate_utm_crs()).simplify(20).to_crs(districts.crs))


dataframe2 = districts.sort_values('fedname')
dataframe2.reset_index(drop=True, inplace=True)

votes = pd.read_csv("voting_data/Canada1962.txt", sep=" ", header=0)

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
with open('voting_data/Canada1962.txt') as file:

    for _ in range(1):
        next(file)  # SKIP FIRST LINE

    for line in file:
        # Removes new line symbol and splits the votes
        line = line[:-1].split()

        if len(line) != 0:
            results = [int(line[3]), int(line[4]), int(line[5]), int(line[6]), int(line[7])]

        winner = 0

        for i in range(0, 5):
            if results[i] > winner:
                winner = int(results[i])
        

        if winner == int(results[0]):
            colour.append(Progressive_Conservative)
            win.append("Progressive Conservative")
        elif winner == int(results[1]):
            colour.append(Liberal)
            win.append("Liberal")
        elif winner == int(results[2]):
            colour.append(Social_Credit)
            win.append("Social Credit")
        elif winner == int(results[3]):
            colour.append(New_Democratic)
            win.append("New Democratic")
        elif winner == int(results[4]):
            colour.append(Liberal_Labour)
            win.append("Liberal-Labour Party")
        else:
            continue
        
## DEBUG
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# print(dataframe3[["fedname", "Riding"]])

total_seats = (PROGRESSIVE_CONSERVATIVE_SEATS + LIBERAL_SEATS + SOCIAL_CREDIT_SEATS + NEW_DEMOCRATIC_SEATS + LIBERAL_LABOUR_SEATS)

sorted_parliament_seats = parliament_charts.create_parliament_seating_plan_1962(PROGRESSIVE_CONSERVATIVE_SEATS, LIBERAL_SEATS, SOCIAL_CREDIT_SEATS, NEW_DEMOCRATIC_SEATS, LIBERAL_LABOUR_SEATS)

parliament_chart = parliament_charts.generateParliamentChart(total_seats, sorted_parliament_seats)

with open("pages/main/parliament_charts/parl_chart1962.html", "w") as file:
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
    cmap=['#EE3224', '#A91CB9', '#F58220', '#0F2D52', '#005F00'],
    style_kwds=dict(color="black"), #use black outline
)

foliumMap.save("./pages/elections/election1962.html")


### Generate election page in main folder
generateHtmlMapFiles.generateElectionMapFile(1962)
