with open("./voting_data/Canada1874_copy.txt", "r+") as file:
    lines = file.readlines()
    lines.sort()
    file.seek(0)
    file.writelines(lines)