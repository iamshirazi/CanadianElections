# Copyright (c) 2025 Matthew Shirazi

import pandas as pd
import numpy as np

dataframe1 = pd.read_excel('./voting_data/electionsCandidates.xlsx') ## Downloaded the excel file from Library of Parliament website

dataframe2 = dataframe1.drop(['Province or Territory', 'Gender', 'Occupation', 'Result'], axis=1)

np.savetxt(r'./voting_data/ElectionData1940.txt', dataframe2.values, fmt='%s')

modified_lines = []
election_data = []
formatted_line = []

# def set_accilmation_votes():
#     if formatted_line[2] == "Conservative":
#         formatted_line[3] = "1 0 0 0 0 0 0"
#     elif formatted_line[2] == "Liberal-Party-of-Canada":
#         formatted_line[3] = "0 1 0 0 0 0 0"
#     elif formatted_line[2] == "Progressive":
#         formatted_line[3] = "0 0 1 0 0 0 0"
#     elif "Alberta" in formatted_line[2]:
#         formatted_line[3] = "0 0 0 1 0 0 0"
#     elif "Labour" in formatted_line[2]:
#         formatted_line[3] = "0 0 0 0 1 0 0"
#     elif "Independent" in formatted_line[2]:
#         formatted_line[3] = "0 0 0 0 0 1 0"

def set_winner_votes(election_data):
    winner_party = election_data[0][2]
    winner_votes = election_data[0][3]
    riding = election_data[0][0]
    winner = election_data[0][1]
    loser = election_data[1][1]
    global formatted_line

    if winner_party == "Conservative" or winner_party == "National-Government":
        formatted_line = riding + " " + winner + " " + loser + " " + winner_votes + " 0 0 0 0 0 0 0 0 0"
    elif winner_party == "Liberal-Party-of-Canada":
        formatted_line = riding + " " + winner + " " + loser + " 0 " + winner_votes + " 0 0 0 0 0 0 0 0"
    elif "Social-Credit" in winner_party:
        formatted_line = riding + " " + winner + " " + loser + " 0 0 " + winner_votes + " 0 0 0 0 0 0 0"
    elif winner_party == "Co-operative-Commonwealth-Federation":
        formatted_line = riding + " " + winner + " " + loser + " 0 0 0 " + winner_votes + " 0 0 0 0 0 0"
    elif winner_party == "Liberal-Progressive":
        formatted_line = riding + " " + winner + " " + loser + " 0 0 0 0 " + winner_votes + " 0 0 0 0 0"
    elif "Independent" in winner_party:
        formatted_line = riding + " " + winner + " " + loser + " 0 0 0 0 0 " + winner_votes + " 0 0 0 0"
    elif winner_party == "New-Democracy" or winner_party == "New-Democratic-Party":
        formatted_line = riding + " " + winner + " " + loser + " 0 0 0 0 0 0 " + winner_votes + " 0 0 0"
    elif "United-Reform" in winner_party or "Unity" in winner_party or "United-Progressive" in winner_party:
        formatted_line = riding + " " + winner + " " + loser + " 0 0 0 0 0 0 0 " + winner_votes + " 0 0"
    else:
        ### False positive
        formatted_line = riding + " " + winner + " " + "FALSE_POSITIVE" + " 0 0 0 0 0 0 0 0 0 " + winner_votes


def set_other_votes(election_data, index):
    loser_party = election_data[index][2]
    loser_votes = election_data[index][3]
    winner_party = election_data[0][2]
    global formatted_line


    string_party_votes = formatted_line.split()
    party_winner_loser = string_party_votes[0:3]
    party_votes = list(string_party_votes[3:])
    updated_party_votes = []

    if (loser_party == "Conservative" or loser_party == "National-Government") and int(party_votes[0]) == 0:
        updated_party_votes = loser_votes + ' ' +  party_votes[1] + ' ' +  party_votes[2] + ' ' + party_votes[3] + ' ' +  party_votes[4] + ' ' + party_votes[5] + ' ' + party_votes[6] + ' ' + party_votes[7] + ' ' + party_votes[8] + ' ' + party_votes[9]
    elif loser_party == "Liberal-Party-of-Canada" and int(party_votes[1]) == 0:
        updated_party_votes = party_votes[0] + ' ' +  loser_votes + ' ' +  party_votes[2] + ' ' +  party_votes[3] + ' ' +  party_votes[4] + ' ' + party_votes[5] + ' ' + party_votes[6] + ' ' + party_votes[7] + ' ' + party_votes[8] + ' ' + party_votes[9]
    elif "Social-Credit" in loser_party and int(party_votes[2]) == 0:
        updated_party_votes = party_votes[0] + ' ' +  party_votes[1] + ' ' +  loser_votes + ' ' +  party_votes[3] + ' ' +  party_votes[4] + ' ' + party_votes[5] + ' ' + party_votes[6] + ' ' + party_votes[7] + ' ' + party_votes[8] + ' ' + party_votes[9]
    elif loser_party == "Co-operative-Commonwealth-Federation" and int(party_votes[3]) == 0:
        updated_party_votes = party_votes[0] + ' ' +  party_votes[1] + ' ' +  party_votes[2] + ' ' +  loser_votes + ' ' + party_votes[4] + ' ' + party_votes[5] + ' ' + party_votes[6] + ' ' + party_votes[7] + ' ' + party_votes[8] + ' ' + party_votes[9]
    elif loser_party == "Liberal-Progressive" and int(party_votes[4]) == 0:
        updated_party_votes = party_votes[0] + ' ' +  party_votes[1] + ' ' +  party_votes[2] + ' ' + party_votes[3] + ' ' +  loser_votes + ' ' + party_votes[5] + ' ' + party_votes[6] + ' ' + party_votes[7] + ' ' + party_votes[8] + ' ' + party_votes[9]
    elif "Independent" in loser_party and int(party_votes[5]) == 0:
        updated_party_votes = party_votes[0] + ' ' +  party_votes[1] + ' ' +  party_votes[2] + ' ' + party_votes[3] + ' ' + party_votes[4] + ' ' + loser_votes + ' ' + party_votes[6] + ' ' + party_votes[7] + ' ' + party_votes[8] + ' ' + party_votes[9]
    elif (loser_party == "New-Democracy" or loser_party == "New-Democratic-Party") and int(party_votes[6]) == 0:
        updated_party_votes = party_votes[0] + ' ' +  party_votes[1] + ' ' +  party_votes[2] + ' ' + party_votes[3] + ' ' + party_votes[4] + ' ' + party_votes[5] + ' ' +  loser_votes + ' ' + party_votes[7] + ' ' + party_votes[8] + ' ' + party_votes[9]
    elif ("United-Reform" in loser_party or "Unity" in loser_party or "United-Progressive" in loser_party) and int(party_votes[7]) == 0:
        updated_party_votes = party_votes[0] + ' ' +  party_votes[1] + ' ' +  party_votes[2] + ' ' + party_votes[3] + ' ' + party_votes[4] + ' ' + party_votes[5] + ' ' + party_votes[6] + ' ' + loser_votes + ' ' + party_votes[8] + ' ' + party_votes[9]
    elif loser_party == "Communist-Party-of-Canada" and int(party_votes[8]) == 0:
        updated_party_votes = party_votes[0] + ' ' +  party_votes[1] + ' ' +  party_votes[2] + ' ' + party_votes[3] + ' ' + party_votes[4] + ' ' + party_votes[5] + ' ' + party_votes[6] + ' ' + party_votes[7] + ' ' + loser_votes + ' ' + party_votes[9]
    elif loser_party == "Unknown" or loser_party == winner_party or loser_party in winner_party or winner_party in loser_party:
        if int(party_votes[9]) == 0:
            updated_party_votes = party_votes[0] + ' ' + party_votes[1] + ' ' + party_votes[2] + ' ' +  party_votes[3] + ' ' + party_votes[4] + ' ' + party_votes[5] + ' ' + party_votes[6]+ ' ' + party_votes[7] + ' ' + party_votes[8] + ' ' + loser_votes
        else:
            return
    else:
        if int(party_votes[9]) == 0:
            updated_party_votes = party_votes[0] + ' ' + party_votes[1] + ' ' + party_votes[2] + ' ' +  party_votes[3] + ' ' + party_votes[4] + ' ' + party_votes[5] + ' ' + party_votes[6] + ' ' + party_votes[7] + ' ' + party_votes[8] + ' ' + loser_votes
        else:
            return
    
    ### Merge updated election data
    party_winner_loser = " ".join(party_winner_loser)
    updated_party_votes = "".join(updated_party_votes)

    formatted_line = party_winner_loser + " " + updated_party_votes


### Read ElectionData1940.txt, everytime a line starts with a name, append it to the previous line.
with open("./voting_data/ElectionData1940.txt", "r") as file:

    passes = 0
    for current_line in file:

        current_line = current_line[:-1].split()

        if len(election_data) == 0:
            election_data.append(current_line)

        ### FIRST LINE IS ALREADY SAVED TO election_data LIST
        if passes > 0:
            if current_line[0] == election_data[0][0]:
                election_data.append(current_line)
            
            else:
                for i in range(0, len(election_data)):
                    if i == 0:
                        set_winner_votes(election_data)
                    else:
                        set_other_votes(election_data, i)


                election_data.clear()
                election_data.append(current_line)
                modified_lines.append('\n' + formatted_line)

        passes += 1


### Write modified_lines to thirdpass.txt
with open("./voting_data/Canada1940.txt", "w") as file:
    file.writelines(modified_lines)
