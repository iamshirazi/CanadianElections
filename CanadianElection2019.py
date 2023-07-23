import geopandas as gpd
import matplotlib.pyplot as plt

# COLOURS
Lib = '#EE3224'  # (238, 50, 36)
Con = '#0F2D52'  # (15, 45, 82)
NDP = '#F58220'  # (253, 185, 19)
Green = '#3D9B35'  # (61, 155, 53)
BQ = '#00A7EC'  # (0, 167, 236)
Ind = '#847e7e'

# read file
districts = gpd.read_file("districts2/lfed000b16a_e.shp")

colour = []

# read file with results
with open('voting_data/Canada2019.txt') as file:

    for _ in range(1):
        next(file)  # SKIp FIRST LINE

    for line in file:
        # Removes new line symbol and splits the votes
        line = line[:-1].split()

        # print(line)

        if len(line) != 0:
            results = [int(line[2]), int(line[3]), int(
                line[4]), int(line[5]), int(line[6])]

        winner = 0

        for i in range(0, 5):
            if results[i] > winner:
                winner = int(results[i])

        if winner == int(results[0]):
            colour.append(Lib)
        elif winner == int(results[1]):
            colour.append(Con)
        elif winner == int(results[2]):
            colour.append(NDP)
        elif winner == int(results[3]):
            colour.append(Green)
        elif winner == int(results[4]):
            colour.append(BQ)
        elif winner == 0:
            colour.append(Ind)


# Colour the ridings
districts['color'] = colour

# plot the coloured ridings
districts.sort_values('FEDUID').plot(color=districts['color'])

# show map
plt.axis('off')
plt.show()
