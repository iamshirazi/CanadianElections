# Copyright (c) 2025 Matthew Shirazi

import pandas as pd
import numpy as np

dataframe1 = pd.read_excel('./voting_data/electionsCandidates.xlsx') ## Downloaded the excel file from Library of Parliament website

dataframe2 = dataframe1.drop(['Province or Territory', 'Gender', 'Occupation', 'Result'], axis=1)

np.savetxt(r'./voting_data/ElectionData1904.txt', dataframe2.values, fmt='%s')

### Read firstPass.txt, everytime a line starts with a name, append it to the previous line.
previous_line = ['test', 'test', 'test', 'test']
modified_lines = []
skip_next_line = False
with open("./voting_data/ElectionData1904.txt", "r") as file:

    i = 0
    for current_line in file:

        current_line = current_line[:-1].split()

        if skip_next_line == True:
            skip_next_line = False
            previous_line = current_line
            i += 1
            continue

        ## Elected by acclamation
        if i != 0:
            if previous_line[0] != current_line[0]:
                if previous_line[2] == "Liberal-Conservative" or previous_line[2] == "Conservative":
                    previous_line[3] = "1 0 0 0"
                elif previous_line[2] == "Liberal-Party-of-Canada":
                    previous_line[3] = "0 1 0 0"
                elif "Independent" in previous_line[2]:
                    previous_line[3] = "0 0 1 0"
                # elif "Patrons" in previous_line[2]:
                #     previous_line[3] = "0 0 0 1 0 0"
                # elif previous_line[2] == "McCarthyite":
                #     previous_line[3] = "0 0 0 0 1 0"

                previous_line[2] = "None"
                previous_line = " ".join(previous_line)
                modified_lines.append('\n' + previous_line)

            ## Election with more than one candidate
            if previous_line[0] == current_line[0]:
                winner_party = previous_line[2]
                winner_votes = previous_line[3]
                loser = current_line[1]
                loser_party = current_line[2]
                loser_votes = current_line[3]

                if winner_party == "Liberal-Conservative" or previous_line[2] == "Conservative":
                    previous_line[3] = winner_votes + " 0 0 0"
                elif winner_party == "Liberal-Party-of-Canada":
                    previous_line[3] = "0 " + winner_votes + " 0 0"
                elif "Independent" in winner_party:
                    previous_line[3] = "0 0 " + winner_votes + " 0"
                # elif "Patrons" in winner_party:
                #     previous_line[3] = "0 0 0 " + winner_votes + " 0 0"
                # elif winner_party == "McCarthyite":
                #     previous_line[3] = "0 0 0 0 " + winner_votes + " 0"
                else:
                    ### Unknown
                    previous_line = current_line
                    i += 1
                    continue

                ## Don't want to overwrite winner_votes, so just send loser_votes to Unkown section
                if loser_party == "Unknown" or loser_party == winner_party or loser_party in winner_party or winner_party in loser_party:
                    string_of_votes = previous_line[3].split()
                    previous_line[3] = string_of_votes[0] + ' ' + string_of_votes[1] + ' ' + string_of_votes[2] + ' ' + loser_votes
                elif loser_party == "Liberal-Conservative" or loser_party == "Conservative":
                    string_of_votes = previous_line[3].split()
                    previous_line[3] = loser_votes + ' ' +  string_of_votes[1] + ' ' +  string_of_votes[2] + ' ' + string_of_votes[3]
                elif loser_party == "Liberal-Party-of-Canada":
                    string_of_votes = previous_line[3].split()
                    previous_line[3] = string_of_votes[0] + ' ' +  loser_votes + ' ' +  string_of_votes[2] + ' ' +  string_of_votes[3]
                elif "Independent" in loser_party:
                    string_of_votes = previous_line[3].split()
                    previous_line[3] = string_of_votes[0] + ' ' +  string_of_votes[1] + ' ' +  loser_votes + ' ' +  string_of_votes[3]
                # elif "Patrons" in loser_party:
                #     string_of_votes = previous_line[3].split()
                #     previous_line[3] = string_of_votes[0] + ' ' +  string_of_votes[1] + ' ' +  string_of_votes[2] + ' ' +  loser_votes + ' ' +  string_of_votes[4] + ' ' +  string_of_votes[5]
                # elif loser_party == "McCarthyite":
                #     string_of_votes = previous_line[3].split()
                #     previous_line[3] = string_of_votes[0] + ' ' +  string_of_votes[1] + ' ' +  string_of_votes[2] + ' ' +  loser_votes + ' ' +  string_of_votes[4] + ' ' +  string_of_votes[5]

                previous_line[2] = loser
                previous_line = " ".join(previous_line)
                modified_lines.append('\n' + previous_line)
                skip_next_line = True

        previous_line = current_line
        i += 1


### Write modified_lines to thirdpass.txt
with open("./voting_data/Canada1904.txt", "w") as file:
    file.writelines(modified_lines)
