# Copyright (c) 2023 Matthew Shirazi

import geopandas as gpd
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.pyplot as plt
import pandas as pd

# COLOURS
Lib = '#EE3224'  # (238, 50, 36)
Con = '#0F2D52'  # (15, 45, 82)
NDP = '#F58220'  # (253, 185, 19)
Green = '#3D9B35'  # (61, 155, 53)
BQ = '#00A7EC'  # (0, 167, 236)
Ind = '#847e7e'

# read shapefile
districts = gpd.read_file("districts2/lfed000b16a_e.shp")
votes = pd.read_csv("voting_data/Canada2021.txt", sep=" ", header=0)

# Merge district shapes and number of votes
districts['FEDUID'] = districts['FEDUID'].astype(int)
districts = districts.merge(votes, on='FEDUID')

## Simplifiy district shapes to increase loading speed
districts["geometry"] = (districts.to_crs(districts.estimate_utm_crs()).simplify(100).to_crs(districts.crs))

colour = []
win = []

# read file with voting results
with open('voting_data/Canada2021.txt') as file:

    for _ in range(1):
        next(file)  # SKIP FIRST LINE

    for line in file:
        # Removes new line symbol and splits the votes
        line = line[:-1].split()

        if len(line) != 0:
            results = [int(line[2]), int(line[3]), int(
                line[4]), int(line[5]), int(line[6]), int(line[7])]

        winner = 0

        for i in range(0, 6):
            if results[i] > winner:
                winner = int(results[i])

        if winner == int(results[0]):
            colour.append(Lib)
            win.append("Liberal")
        elif winner == int(results[1]):
            colour.append(Con)
            win.append("Conservative")
        elif winner == int(results[2]):
            colour.append(NDP)
            win.append("NDP")
        elif winner == int(results[3]):
            colour.append(Green)
            win.append("Green")
        elif winner == int(results[4]):
            colour.append(BQ)
            win.append("Bloc Quebecois")
        elif winner == int(results[5]):
            colour.append(Ind)
            win.append("Independent")


# Sort the ridings
ridings = districts.sort_values('FEDUID')

## DROP UNNECESSARY COLUMNS IN DATAFRAME:
ridings = ridings.drop(['FEDUID', 'FEDNAME', 'FEDENAME', 'FEDFNAME', 'PRUID', 'PRNAME'], axis=1)

# Colour the ridings
ridings["Party"] = win
ridings['color'] = colour

foliumMap = ridings.explore(
    column="Party", # make choropleth vased on winner in column
    tooltip=["Riding", "Party", "Lib", "Con", "NDP", "Green", "BQ", "Ind"], # show all party votes for a riding when hovering over it
    popup=True, # show all values of a riding when you click it
    tiles="CartoDB positron", # use "CartoDB positron" tiles
    cmap=['#00A7EC', '#0F2D52', '#3D9B35', '#EE3224', '#F58220'], ## Removed '#847e7e' (Indepedendent colour) because no indepedent MPs were elected in 2021
    style_kwds=dict(color="black") #use black outline
)

foliumMap.save("./pages/elections/election2021.html")
