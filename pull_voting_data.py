# Copyright (c) 2025 Matthew Shirazi

import pandas as pd
import numpy as np
import sort

### SET THE ELECTION YEAR EVERYTIME BEFORE YOU RUN THIS SCRIPT
ELECTION_YEAR = "1974"

dataframe1 = pd.read_excel('./voting_data/electionsCandidates.xlsx') ## Downloaded the excel file from Library of Parliament website

dataframe2 = dataframe1.drop(['Province or Territory', 'Gender', 'Occupation', 'Result'], axis=1)

np.savetxt(r'./voting_data/ElectionData' + ELECTION_YEAR + '.txt', dataframe2.values, fmt='%s')

modified_lines = []
election_data = []
formatted_line = []

def set_accilmation_votes(election_data):
    winner_party = election_data[0][2]
    riding = election_data[0][0]
    winner = election_data[0][1]
    loser = "None"
    global formatted_line

    if winner_party == "Progressive-Conservative-Party":
        formatted_line = riding + " " + winner + " " + loser + " 1 0 0 0 0 0 0 0"
    elif winner_party == "Liberal-Party-of-Canada":
        formatted_line = riding + " " + winner + " " + loser + " 0 1 0 0 0 0 0 0"
    elif winner_party == "New-Democratic-Party":
        formatted_line = riding + " " + winner + " " + loser + " 0 0 1 0 0 0 0 0"
    elif winner_party == "Social-Credit-Party-of-Canada":
        formatted_line = riding + " " + winner + " " + loser + " 0 0 0 1 0 0 0 0"
    elif "Independent" in winner_party:
        formatted_line = riding + " " + winner + " " + loser + " 0 0 0 0 1 0 0 0"


def set_winner_votes(election_data):
    winner_party = election_data[0][2]
    winner_votes = election_data[0][3]
    riding = election_data[0][0]
    winner = election_data[0][1]
    loser = election_data[1][1]
    global formatted_line

    if winner_party == "Progressive-Conservative-Party":
        formatted_line = riding + " " + winner + " " + loser + " " + winner_votes + " 0 0 0 0 0 0 0"
    elif winner_party == "Liberal-Party-of-Canada":
        formatted_line = riding + " " + winner + " " + loser + " 0 " + winner_votes + " 0 0 0 0 0 0"
    elif winner_party == "New-Democratic-Party":
        formatted_line = riding + " " + winner + " " + loser + " 0 0 " + winner_votes + " 0 0 0 0 0"
    elif winner_party == "Social-Credit-Party-of-Canada":
        formatted_line = riding + " " + winner + " " + loser + " 0 0 0 " + winner_votes + " 0 0 0 0"
    elif "Independent" in winner_party:
        formatted_line = riding + " " + winner + " " + loser + " 0 0 0 0 " + winner_votes + " 0 0 0"
    else:
        ### False positive
        formatted_line = riding + " " + winner + " " + "FALSE_POSITIVE" + " 0 0 0 0 0 0 " + winner_votes


def set_other_votes(election_data, index):
    loser_party = election_data[index][2]
    loser_votes = election_data[index][3]
    winner_party = election_data[0][2]
    global formatted_line


    string_party_votes = formatted_line.split()
    party_winner_loser = string_party_votes[0:3]
    party_votes = list(string_party_votes[3:])
    updated_party_votes = []

    if loser_party == "Progressive-Conservative-Party" and int(party_votes[0]) == 0:
        updated_party_votes = loser_votes + ' ' +  party_votes[1] + ' ' +  party_votes[2] + ' ' + party_votes[3] + ' ' +  party_votes[4] + ' ' + party_votes[5] + ' ' + party_votes[6] + ' ' + party_votes[7]
    elif loser_party == "Liberal-Party-of-Canada" and int(party_votes[1]) == 0:
        updated_party_votes = party_votes[0] + ' ' +  loser_votes + ' ' +  party_votes[2] + ' ' +  party_votes[3] + ' ' +  party_votes[4] + ' ' + party_votes[5] + ' ' + party_votes[6] + ' ' + party_votes[7]
    elif loser_party == "New-Democratic-Party" and int(party_votes[2]) == 0:
        updated_party_votes = party_votes[0] + ' ' +  party_votes[1] + ' ' +  loser_votes + ' ' +  party_votes[3] + ' ' +  party_votes[4] + ' ' + party_votes[5] + ' ' + party_votes[6] + ' ' + party_votes[7]
    elif loser_party == "Social-Credit-Party-of-Canada" and int(party_votes[3]) == 0:
        updated_party_votes = party_votes[0] + ' ' +  party_votes[1] + ' ' +  party_votes[2] + ' ' +  loser_votes + ' ' + party_votes[4] + ' ' + party_votes[5] + ' ' + party_votes[6] + ' ' + party_votes[7]
    elif (loser_party == "Independent" or "Independent" in loser_party) and int(party_votes[4]) == 0:
        updated_party_votes = party_votes[0] + ' ' +  party_votes[1] + ' ' +  party_votes[2] + ' ' + party_votes[3] + ' ' + loser_votes + ' ' + party_votes[5] + ' ' + party_votes[6] + ' ' + party_votes[7]
    elif (loser_party == "Marxist-Leninist-Party-of-Canada") and int(party_votes[5]) == 0:
        updated_party_votes = party_votes[0] + ' ' +  party_votes[1] + ' ' +  party_votes[2] + ' ' + party_votes[3] + ' ' + party_votes[4] + ' ' + loser_votes + ' ' + party_votes[6] + ' ' + party_votes[7]
    elif (loser_party == "Communist-Party-of-Canada") and int(party_votes[6]) == 0:
        updated_party_votes = party_votes[0] + ' ' +  party_votes[1] + ' ' +  party_votes[2] + ' ' + party_votes[3] + ' ' + party_votes[4] + ' ' + party_votes[5] + ' ' + loser_votes + ' ' + party_votes[7]
    elif loser_party == "Unknown" or loser_party == winner_party or loser_party in winner_party or winner_party in loser_party:
        if int(party_votes[7]) == 0:
            updated_party_votes = party_votes[0] + ' ' + party_votes[1] + ' ' + party_votes[2] + ' ' +  party_votes[3] + ' ' + party_votes[4] + ' ' + party_votes[5] + ' ' + party_votes[6] + ' ' + loser_votes
        else:
            return
    else:
        if int(party_votes[7]) == 0:
            updated_party_votes = party_votes[0] + ' ' + party_votes[1] + ' ' + party_votes[2] + ' ' +  party_votes[3] + ' ' + party_votes[4] + ' ' + party_votes[5] + ' ' + party_votes[6] + ' ' +  loser_votes
        else:
            return
    
    ### Merge updated election data
    party_winner_loser = " ".join(party_winner_loser)
    updated_party_votes = "".join(updated_party_votes)

    formatted_line = party_winner_loser + " " + updated_party_votes


### Read ElectionData1974.txt, add voting data for a riding into 
# an array and check who the winner is, append formatted voting data to modified_lines, loop through all ridings
with open("./voting_data/ElectionData" + ELECTION_YEAR + ".txt", "r") as file:

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
                if len(election_data) == 1:
                    set_accilmation_votes(election_data)

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
with open("./voting_data/Canada" + ELECTION_YEAR + ".txt", "w") as file:
    file.writelines(modified_lines)

sort.sort(ELECTION_YEAR)