# Copyright (c) 2025 Matthew Shirazi

import pandas as pd
import numpy as np

dataframe1 = pd.read_excel('./voting_data/electionsCandidates.xlsx') ## Downloaded the excel file from Library of Parliament website

dataframe2 = dataframe1.drop(['Province or Territory', 'Gender', 'Occupation', 'Result'], axis=1)

np.savetxt(r'./voting_data/ElectionData1935.txt', dataframe2.values, fmt='%s')

previous_previous_line = ['testing', 'testing', 'testing']
previous_line = ['test', 'test', 'test', 'test']
modified_lines = []
skip_next_line = False
skip_next_line_again = False
UNKNOWN = False

def set_accilmation_votes():
    if formatted_line[2] == "Conservative":
        formatted_line[3] = "1 0 0 0 0 0 0"
    elif formatted_line[2] == "Liberal-Party-of-Canada":
        formatted_line[3] = "0 1 0 0 0 0 0"
    elif formatted_line[2] == "Progressive":
        formatted_line[3] = "0 0 1 0 0 0 0"
    elif "Alberta" in formatted_line[2]:
        formatted_line[3] = "0 0 0 1 0 0 0"
    elif "Labour" in formatted_line[2]:
        formatted_line[3] = "0 0 0 0 1 0 0"
    elif "Independent" in formatted_line[2]:
        formatted_line[3] = "0 0 0 0 0 1 0"

def set_winner_votes(winner_party, winner_votes):
    global previous_previous_line
    global previous_line
    global current_line
    global i

    if winner_party == "Conservative":
        formatted_line[3] = winner_votes + " 0 0 0 0 0 0 0"
    elif winner_party == "Liberal-Party-of-Canada":
        formatted_line[3] = "0 " + winner_votes + " 0 0 0 0 0 0"
    elif "Social-Credit" in winner_party:
        formatted_line[3] = "0 0 " + winner_votes + " 0 0 0 0 0"
    elif winner_party == "Co-operative-Commonwealth-Federation":
        formatted_line[3] = "0 0 0 " + winner_votes + " 0 0 0 0"
    elif winner_party == "Reconstruction-Party":
        formatted_line[3] = "0 0 0 0 " + winner_votes + " 0 0 0"
    elif "Independent" in winner_party:
        formatted_line[3] = "0 0 0 0 0 " + winner_votes + " 0 0"
    else:
        ### False positive
        formatted_line[3] = "0 0 0 0 0 0 0 " + winner_votes
        previous_previous_line = previous_line
        previous_line = current_line
        i += 1
        UNKNOWN = True

def set_party_votes(winner_party, loser_party, loser_votes):
    global i

    string_party_votes = formatted_line[3].split()
    party_votes = list(map(int, string_party_votes))

    if loser_party == "Conservative" and party_votes[0] == 0:
        string_of_votes = formatted_line[3].split()
        formatted_line[3] = loser_votes + ' ' +  string_of_votes[1] + ' ' +  string_of_votes[2] + ' ' + string_of_votes[3] + ' ' +  string_of_votes[4] + ' ' + string_of_votes[5] + ' ' + string_of_votes[6] + ' ' + string_of_votes[7]
    elif loser_party == "Liberal-Party-of-Canada" and party_votes[1] == 0:
        string_of_votes = formatted_line[3].split()
        formatted_line[3] = string_of_votes[0] + ' ' +  loser_votes + ' ' +  string_of_votes[2] + ' ' +  string_of_votes[3] + ' ' +  string_of_votes[4] + ' ' + string_of_votes[5] + ' ' + string_of_votes[6] + ' ' + string_of_votes[7]
    elif "Social-Credit" in loser_party and party_votes[2] == 0:
        string_of_votes = formatted_line[3].split()
        formatted_line[3] = string_of_votes[0] + ' ' +  string_of_votes[1] + ' ' +  loser_votes + ' ' +  string_of_votes[3] + ' ' +  string_of_votes[4] + ' ' + string_of_votes[5] + ' ' + string_of_votes[6] + ' ' + string_of_votes[7]
    elif loser_party == "Co-operative-Commonwealth-Federation" and party_votes[3] == 0:
        string_of_votes = formatted_line[3].split()
        formatted_line[3] = string_of_votes[0] + ' ' +  string_of_votes[1] + ' ' +  string_of_votes[2] + ' ' +  loser_votes + ' ' + string_of_votes[4] + ' ' + string_of_votes[5] + ' ' + string_of_votes[6] + ' ' + string_of_votes[7]
    elif loser_party == "Reconstruction-Party" and party_votes[4] == 0:
        string_of_votes = formatted_line[3].split()
        formatted_line[3] = string_of_votes[0] + ' ' +  string_of_votes[1] + ' ' +  string_of_votes[2] + ' ' + string_of_votes[3] + ' ' +  loser_votes + ' ' + string_of_votes[5] + ' ' + string_of_votes[6] + ' ' + string_of_votes[7]
    elif "Independent" in loser_party and party_votes[5] == 0:
        string_of_votes = formatted_line[3].split()
        formatted_line[3] = string_of_votes[0] + ' ' +  string_of_votes[1] + ' ' +  string_of_votes[2] + ' ' + string_of_votes[3] + ' ' + string_of_votes[4] + ' ' + loser_votes + ' ' + string_of_votes[6] + ' ' + string_of_votes[7]
    elif loser_party == "Communist-Party-of-Canada" and party_votes[6] == 0:
        string_of_votes = formatted_line[3].split()
        formatted_line[3] = string_of_votes[0] + ' ' +  string_of_votes[1] + ' ' +  string_of_votes[2] + ' ' + string_of_votes[3] + ' ' + string_of_votes[4] + ' ' + string_of_votes[5] + ' ' + loser_votes + ' ' + string_of_votes[7]
    elif loser_party == "Unknown" or loser_party == winner_party or loser_party in winner_party or winner_party in loser_party:
        if party_votes[7] == 0:
            string_of_votes = formatted_line[3].split()
            formatted_line[3] = string_of_votes[0] + ' ' + string_of_votes[1] + ' ' + string_of_votes[2] + ' ' +  string_of_votes[3] + ' ' + string_of_votes[4] + ' ' + string_of_votes[5] + ' ' + string_of_votes[6] + ' ' + loser_votes


### Read ElectionData1935.txt, everytime a line starts with a name, append it to the previous line.
with open("./voting_data/ElectionData1935.txt", "r") as file:

    i = 0
    for current_line in file:

        current_line = current_line[:-1].split()

        if skip_next_line == True:
            skip_next_line = False
            previous_previous_line = previous_line
            previous_line = current_line
            i += 1
            continue
    
        if skip_next_line_again == True:
            skip_next_line_again = False
            previous_previous_line = previous_line
            previous_line = current_line
            i += 1
            continue

        ## Elected by acclamation
        if i > 1:
            ## Election with 3 candidates
            if previous_line[0] == current_line[0] and previous_line[0] == previous_previous_line[0]:
                formatted_line = previous_previous_line.copy()
                winner_party = previous_previous_line[2]
                winner_votes = previous_previous_line[3]
                loser = previous_line[1]
                loser_party = previous_line[2]
                loser_votes = previous_line[3]
                last_place_party = current_line[2]
                last_place_votes = current_line[3]

                set_winner_votes(winner_party, winner_votes)
                if (UNKNOWN == True):
                    continue

                set_party_votes(winner_party, loser_party, loser_votes)

                set_party_votes(winner_party, last_place_party, last_place_votes)

                formatted_line[2] = loser
                formatted_line = " ".join(formatted_line)
                modified_lines.append('\n' + formatted_line)
                skip_next_line = True
                skip_next_line_again = True

            ## First case of 2 election candidates
            elif previous_line[0] == current_line[0] and previous_line[0] != previous_previous_line[0]:
                formatted_line = previous_line.copy()
                winner_party = previous_line[2]
                winner_votes = previous_line[3]
                loser = current_line[1]
                loser_party = current_line[2]
                loser_votes = current_line[3]

                set_winner_votes(winner_party, winner_votes)
                if (UNKNOWN == True):
                    continue

                set_party_votes(winner_party, loser_party, loser_votes)

                formatted_line[2] = loser
                formatted_line = " ".join(formatted_line)
                modified_lines.append('\n' + formatted_line)
                skip_next_line = True
            
            ## Second case of 2 election candidates
            elif previous_line[0] != current_line[0] and previous_line[0] == previous_previous_line[0]:
                formatted_line = previous_previous_line.copy()
                winner_party = previous_previous_line[2]
                winner_votes = previous_previous_line[3]
                loser = previous_line[1]
                loser_party = previous_line[2]
                loser_votes = previous_line[3]

                set_winner_votes(winner_party, winner_votes)
                if (UNKNOWN == True):
                    continue

                set_party_votes(winner_party, loser_party, loser_votes)

                formatted_line[2] = loser
                formatted_line = " ".join(formatted_line)
                modified_lines.append('\n' + formatted_line)
                skip_next_line = True
            
            ## Elected by Acclamation
            # if current_line[3] == '0':
            #     formatted_line = current_line.copy()

            #     set_accilmation_votes()

            #     formatted_line[2] = "None"
            #     formatted_line = " ".join(formatted_line)
            #     modified_lines.append('\n' + formatted_line)
            
            # if previous_line[3] == '0':
            #     formatted_line = previous_line.copy()

            #     set_accilmation_votes()

            #     formatted_line[2] = "None"
            #     formatted_line = " ".join(formatted_line)
            #     modified_lines.append('\n' + formatted_line)

            # if previous_previous_line[3] == '0':
            #     formatted_line = previous_previous_line.copy()

            #     set_accilmation_votes()

            #     formatted_line[2] = "None"
            #     formatted_line = " ".join(formatted_line)
            #     modified_lines.append('\n' + formatted_line)

        previous_previous_line = previous_line
        previous_line = current_line
        i += 1


### Write modified_lines to thirdpass.txt
with open("./voting_data/Canada1935.txt", "w") as file:
    file.writelines(modified_lines)
