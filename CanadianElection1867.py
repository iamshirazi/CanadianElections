# Copyright (c) 2023 Matthew Shirazi

import geopandas as gpd
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.pyplot as plt
import pandas as pd

# COLOURS
Lib = '#EE3224'  # (238, 50, 36)
Con = '#0F2D52'  # (15, 45, 82)
AntiCon = '#F58220'  # (253, 185, 19)
Unknown = '#847e7e'

# read shapefile
districts = gpd.read_file("districts2/CBF_RO1867_CSRS.shp", rows=186) ### Removed Manitoba
districts['id'] = districts['id'].astype(int)
districts_new = districts[districts['id'] < 59000] ### REMOVED BC DISTRICTS

## Simplifiy district shapes to increase loading speed
districts_new["geometry"] = (districts_new.to_crs(districts_new.estimate_utm_crs()).simplify(10).to_crs(districts_new.crs))

dataframe2 = districts_new.sort_values('fedname')
dataframe2.reset_index(drop=True, inplace=True)

votes = pd.read_csv("voting_data/Canada1867.txt", sep=" ", header=0)

## Merge district shapes and number of votes
dataframe3 = pd.concat([dataframe2, votes], axis=1)

colour = []
win = []

## FOR DEBUGGING
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# print(dataframe3)

## FOR TESTING, JUST FILL COLOUR AND WIN WITH LIBERAL TO SEE COLOUR
# for i in range(181):
#     colour.append(Lib)
#     win.append("Liberal")


# read file with voting results
with open('voting_data/Canada1867.txt') as file:

    for _ in range(1):
        next(file)  # SKIP FIRST LINE

    for line in file:
        # Removes new line symbol and splits the votes
        line = line[:-1].split()

        if len(line) != 0:
            results = [int(line[3]), int(line[4]), int(
                line[5]), int(line[6])]

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
            colour.append(AntiCon)
            win.append("Anti-Confederation")
        else:
            colour.append(Unknown)
            win.append("Unknown")
        

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
    cmap=['#F58220', '#0F2D52', '#EE3224', '#847e7e'],
    style_kwds=dict(color="black"), #use black outline
)

outfp = r"./pages/elections/election1867.html"

foliumMap.save(outfp)
