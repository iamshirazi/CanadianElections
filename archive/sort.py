def sort(electionYear):
    with open("./voting_data/Canada" + electionYear + ".txt", "r+") as file:
        lines = file.readlines()
        lines.sort()
        file.seek(0)
        file.writelines(lines)
