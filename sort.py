with open("./voting_data/Canada1887.txt", "r+") as file:
    lines = file.readlines()
    lines.sort()
    file.seek(0)
    file.writelines(lines)