# Copyright (c) 2023 Matthew Shirazi

import pandas as pd
import numpy as np

dataframe1 = pd.read_excel('./voting_data/ElectionsCandidates.xlsx') ## Downloaded the excel file from Library of Parliament website

dataframe2 = dataframe1.drop(['Gender', 'Occupation', 'Result'], axis=1)

np.savetxt(r'./voting_data/Canada1867_firstPass.txt', dataframe2.values, fmt='%s')

file2 = open('./voting_data/Canada1867_secondPass.txt','w')

### REMOVES LINES STARTING WITH PROVINCE, REMOVE EVERYTHING IN THE "CONSTITUENCY"
#   EXCEPT FOR THE RIDING NAME, PRINT RIDING NAME AT START OF LINE
with open("./voting_data/Canada1867_firstPass.txt", "r") as file:

    for line in file:

        ## line = line[:-1].split() ## Removes new line symbol

        if not line.startswith('Province') and not line.startswith('Constituency'):
            file2.write(line)

        elif line.startswith('Constituency'):
            line = line.split('"')

            file2.write(line[5] + ' ')

file2.close()

### Read secondPass.txt, everytime a line starts with a name, append it to the previous line.
modified_lines = []
with open("./voting_data/Canada1867_secondPass.txt", "r") as file:

    i = 0
    for line in file:

        line_split = line[:-1].split()

        if i == 0:
            modified_lines.append(line) ### ADD FIRST LINE SO THAT modified_lines is not empty

        elif line_split[0].endswith(","):
            modified_lines[-1] = modified_lines[-1].strip('\n') + ' ' + line
        else:
            modified_lines.append(line)
        i += 1

### Write modified_lines to thirdpass.txt
with open("./voting_data/Canada1867_thirdPass.txt", "w") as file:
    file.writelines(modified_lines)


# SORT txt file based on fedname (riding name) so it lines up with the sorted shapefile
with open("./voting_data/Canada1867_thirdPass.txt", "r+") as file:
    lines = file.readlines()
    lines.sort()        
    file.seek(0)
    file.writelines("Riding winner loser Con Lib AntiCon Unknown\n")
    file.writelines(lines)