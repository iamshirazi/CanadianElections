# Copyright (c) 2026 Matthew Shirazi

import generateParliamentChartFiles
import generateHtmlMapFiles

def createParliamentChartFile(parliament_chart: str, election_year: int):
     with open(f"pages/main/parliament_charts/parl_chart{election_year}.html", "w") as file:
        generic_lines = "<!DOCTYPE html>\n<html>\n<head>\n\t<link rel='stylesheet' href='/main/elections_style.css'>\n</head>\n</head>\n<body>\n"
        file.writelines(generic_lines)
        file.writelines(parliament_chart)
        file.writelines("</body>\n</html>")


def election1867():
    ELECTION_YEAR = 1867

    CON_SEATS = 100
    LIB_SEATS = 62
    ANTI_CON_SEATS = 18
    EMPTY_SEATS = 1


    total_seats = (CON_SEATS + LIB_SEATS + ANTI_CON_SEATS + EMPTY_SEATS)

    sorted_parliament_seats = generateParliamentChartFiles.create_parliament_seating_plan_1867(CON_SEATS, LIB_SEATS, ANTI_CON_SEATS, EMPTY_SEATS)

    parliament_chart = generateParliamentChartFiles.generateParliamentChart(total_seats, sorted_parliament_seats)

    createParliamentChartFile(parliament_chart, ELECTION_YEAR)


    ### Generate election page in main folder
    generateHtmlMapFiles.generateElectionMapFile(ELECTION_YEAR)


def election1872():
    ELECTION_YEAR = 1872

    CON_SEATS = 101
    LIB_SEATS = 93
    INDEPENDENT_SEATS = 6


    total_seats = (CON_SEATS + LIB_SEATS + INDEPENDENT_SEATS)

    sorted_parliament_seats = generateParliamentChartFiles.create_parliament_seating_plan_1872(CON_SEATS, LIB_SEATS, INDEPENDENT_SEATS)

    parliament_chart = generateParliamentChartFiles.generateParliamentChart(total_seats, sorted_parliament_seats)

    createParliamentChartFile(parliament_chart, ELECTION_YEAR)


    ### Generate election page in main folder
    generateHtmlMapFiles.generateElectionMapFile(ELECTION_YEAR)


def election1874():
    ELECTION_YEAR = 1874

    CON_SEATS = 63
    LIB_SEATS = 131
    INDEPENDENT_SEATS = 12


    total_seats = (CON_SEATS + LIB_SEATS + INDEPENDENT_SEATS)

    sorted_parliament_seats = generateParliamentChartFiles.create_parliament_seating_plan_1874(CON_SEATS, LIB_SEATS, INDEPENDENT_SEATS)

    parliament_chart = generateParliamentChartFiles.generateParliamentChart(total_seats, sorted_parliament_seats)

    createParliamentChartFile(parliament_chart, ELECTION_YEAR)


    ### Generate election page in main folder
    generateHtmlMapFiles.generateElectionMapFile(ELECTION_YEAR)


def election1878():
    ELECTION_YEAR = 1878

    CON_SEATS = 135
    LIB_SEATS = 62
    INDEPENDENT_SEATS = 8
    NATIONALIST_SEATS = 1


    total_seats = (CON_SEATS + LIB_SEATS + INDEPENDENT_SEATS + NATIONALIST_SEATS)

    sorted_parliament_seats = generateParliamentChartFiles.create_parliament_seating_plan_1878(CON_SEATS, LIB_SEATS, INDEPENDENT_SEATS, NATIONALIST_SEATS)

    parliament_chart = generateParliamentChartFiles.generateParliamentChart(total_seats, sorted_parliament_seats)

    createParliamentChartFile(parliament_chart, ELECTION_YEAR)


    ### Generate election page in main folder
    generateHtmlMapFiles.generateElectionMapFile(ELECTION_YEAR)


def election1882():
    ELECTION_YEAR = 1882

    CON_SEATS = 134
    LIB_SEATS = 72
    INDEPENDENT_SEATS = 4
    NATIONALIST_SEATS = 1


    total_seats = (CON_SEATS + LIB_SEATS + INDEPENDENT_SEATS + NATIONALIST_SEATS)

    sorted_parliament_seats = generateParliamentChartFiles.create_parliament_seating_plan_1878(CON_SEATS, LIB_SEATS, INDEPENDENT_SEATS, NATIONALIST_SEATS)

    parliament_chart = generateParliamentChartFiles.generateParliamentChart(total_seats, sorted_parliament_seats)

    createParliamentChartFile(parliament_chart, ELECTION_YEAR)


    ### Generate election page in main folder
    generateHtmlMapFiles.generateElectionMapFile(ELECTION_YEAR)


def election1887():
    ELECTION_YEAR = 1887

    CON_SEATS = 123
    LIB_SEATS = 79
    INDEPENDENT_SEATS = 10
    NATIONALIST_SEATS = 2


    total_seats = (CON_SEATS + LIB_SEATS + INDEPENDENT_SEATS + NATIONALIST_SEATS)

    sorted_parliament_seats = generateParliamentChartFiles.create_parliament_seating_plan_1878(CON_SEATS, LIB_SEATS, INDEPENDENT_SEATS, NATIONALIST_SEATS)

    parliament_chart = generateParliamentChartFiles.generateParliamentChart(total_seats, sorted_parliament_seats)

    createParliamentChartFile(parliament_chart, ELECTION_YEAR)


    ### Generate election page in main folder
    generateHtmlMapFiles.generateElectionMapFile(ELECTION_YEAR)


def election1891():
    ELECTION_YEAR = 1891

    CON_SEATS = 117
    LIB_SEATS = 90
    INDEPENDENT_SEATS = 6
    NATIONALIST_SEATS = 2


    total_seats = (CON_SEATS + LIB_SEATS + INDEPENDENT_SEATS + NATIONALIST_SEATS)

    sorted_parliament_seats = generateParliamentChartFiles.create_parliament_seating_plan_1878(CON_SEATS, LIB_SEATS, INDEPENDENT_SEATS, NATIONALIST_SEATS)

    parliament_chart = generateParliamentChartFiles.generateParliamentChart(total_seats, sorted_parliament_seats)

    createParliamentChartFile(parliament_chart, ELECTION_YEAR)


    ### Generate election page in main folder
    generateHtmlMapFiles.generateElectionMapFile(ELECTION_YEAR)


def election1896():
    ELECTION_YEAR = 1896

    CON_SEATS = 86
    LIB_SEATS = 117
    INDEPENDENT_SEATS = 6
    PATRONS_SEATS = 2
    MCCARTHY_SEATS = 2


    total_seats = (CON_SEATS + LIB_SEATS + INDEPENDENT_SEATS + PATRONS_SEATS + MCCARTHY_SEATS)

    sorted_parliament_seats = generateParliamentChartFiles.create_parliament_seating_plan_1896(CON_SEATS, LIB_SEATS, INDEPENDENT_SEATS, PATRONS_SEATS, MCCARTHY_SEATS)

    parliament_chart = generateParliamentChartFiles.generateParliamentChart(total_seats, sorted_parliament_seats)

    createParliamentChartFile(parliament_chart, ELECTION_YEAR)


    ### Generate election page in main folder
    generateHtmlMapFiles.generateElectionMapFile(ELECTION_YEAR)


def election1900():
    ELECTION_YEAR = 1900

    CON_SEATS = 79
    LIB_SEATS = 128
    INDEPENDENT_SEATS = 6


    total_seats = (CON_SEATS + LIB_SEATS + INDEPENDENT_SEATS)

    ### Used 1874 function (same parties)
    sorted_parliament_seats = generateParliamentChartFiles.create_parliament_seating_plan_1874(CON_SEATS, LIB_SEATS, INDEPENDENT_SEATS)

    parliament_chart = generateParliamentChartFiles.generateParliamentChart(total_seats, sorted_parliament_seats)

    createParliamentChartFile(parliament_chart, ELECTION_YEAR)


    ### Generate election page in main folder
    generateHtmlMapFiles.generateElectionMapFile(ELECTION_YEAR)


def election1904():
    ELECTION_YEAR = 1904

    CON_SEATS = 75
    LIB_SEATS = 137
    INDEPENDENT_SEATS = 2


    total_seats = (CON_SEATS + LIB_SEATS + INDEPENDENT_SEATS)

    ### Used 1874 function (same parties)
    sorted_parliament_seats = generateParliamentChartFiles.create_parliament_seating_plan_1874(CON_SEATS, LIB_SEATS, INDEPENDENT_SEATS)

    parliament_chart = generateParliamentChartFiles.generateParliamentChart(total_seats, sorted_parliament_seats)

    createParliamentChartFile(parliament_chart, ELECTION_YEAR)


    ### Generate election page in main folder
    generateHtmlMapFiles.generateElectionMapFile(ELECTION_YEAR)


def election1908():
    ELECTION_YEAR = 1908

    CON_SEATS = 85
    LIB_SEATS = 133
    INDEPENDENT_SEATS = 2
    LABOUR_SEATS = 1


    total_seats = (CON_SEATS + LIB_SEATS + INDEPENDENT_SEATS + LABOUR_SEATS)

    sorted_parliament_seats = generateParliamentChartFiles.create_parliament_seating_plan_1908(CON_SEATS, LIB_SEATS, INDEPENDENT_SEATS, LABOUR_SEATS)

    parliament_chart = generateParliamentChartFiles.generateParliamentChart(total_seats, sorted_parliament_seats)

    createParliamentChartFile(parliament_chart, ELECTION_YEAR)


    ### Generate election page in main folder
    generateHtmlMapFiles.generateElectionMapFile(ELECTION_YEAR)


def election1911():
    ELECTION_YEAR = 1911

    CON_SEATS = 132
    LIB_SEATS = 85
    INDEPENDENT_SEATS = 3
    LABOUR_SEATS = 1


    total_seats = (CON_SEATS + LIB_SEATS + INDEPENDENT_SEATS + LABOUR_SEATS)

    sorted_parliament_seats = generateParliamentChartFiles.create_parliament_seating_plan_1911(CON_SEATS, LIB_SEATS, INDEPENDENT_SEATS, LABOUR_SEATS)

    parliament_chart = generateParliamentChartFiles.generateParliamentChart(total_seats, sorted_parliament_seats)

    createParliamentChartFile(parliament_chart, ELECTION_YEAR)


    ### Generate election page in main folder
    generateHtmlMapFiles.generateElectionMapFile(ELECTION_YEAR)


def election1917():
    ELECTION_YEAR = 1917
    
    UNIONIST_SEATS = 153
    OPPOSITION_SEATS = 82


    total_seats = (UNIONIST_SEATS + OPPOSITION_SEATS)

    sorted_parliament_seats = generateParliamentChartFiles.create_parliament_seating_plan_1917(UNIONIST_SEATS, OPPOSITION_SEATS)

    parliament_chart = generateParliamentChartFiles.generateParliamentChart(total_seats, sorted_parliament_seats)

    createParliamentChartFile(parliament_chart, ELECTION_YEAR)


    ### Generate election page in main folder
    generateHtmlMapFiles.generateElectionMapFile(ELECTION_YEAR)


def election1921():
    ELECTION_YEAR = 1921

    CONSERVATIVE_SEATS = 49
    LIBERAL_SEATS = 118
    PROGRESSIVE_SEATS = 58
    UF_ALBERTA_SEATS = 2
    LABOUR_SEATS = 3
    INDEPENDENT_SEATS = 4
    UF_ONTARIO_SEATS = 1


    total_seats = (CONSERVATIVE_SEATS + LIBERAL_SEATS + PROGRESSIVE_SEATS + UF_ALBERTA_SEATS + LABOUR_SEATS + INDEPENDENT_SEATS + UF_ONTARIO_SEATS)

    sorted_parliament_seats = generateParliamentChartFiles.create_parliament_seating_plan_1921(CONSERVATIVE_SEATS, LIBERAL_SEATS, PROGRESSIVE_SEATS, UF_ALBERTA_SEATS, LABOUR_SEATS, INDEPENDENT_SEATS, UF_ONTARIO_SEATS)

    parliament_chart = generateParliamentChartFiles.generateParliamentChart(total_seats, sorted_parliament_seats)

    createParliamentChartFile(parliament_chart, ELECTION_YEAR)


    ### Generate election page in main folder
    generateHtmlMapFiles.generateElectionMapFile(ELECTION_YEAR)


def election1925():
    ELECTION_YEAR = 1925

    CONSERVATIVE_SEATS = 115
    LIBERAL_SEATS = 100
    PROGRESSIVE_SEATS = 22
    UF_ALBERTA_SEATS = 2
    LABOUR_SEATS = 2
    INDEPENDENT_SEATS = 4


    total_seats = (CONSERVATIVE_SEATS + LIBERAL_SEATS + PROGRESSIVE_SEATS + UF_ALBERTA_SEATS + LABOUR_SEATS + INDEPENDENT_SEATS)

    sorted_parliament_seats = generateParliamentChartFiles.create_parliament_seating_plan_1925(CONSERVATIVE_SEATS, LIBERAL_SEATS, PROGRESSIVE_SEATS, UF_ALBERTA_SEATS, LABOUR_SEATS, INDEPENDENT_SEATS)

    parliament_chart = generateParliamentChartFiles.generateParliamentChart(total_seats, sorted_parliament_seats)

    createParliamentChartFile(parliament_chart, ELECTION_YEAR)


    ### Generate election page in main folder
    generateHtmlMapFiles.generateElectionMapFile(ELECTION_YEAR)


def election1926():
    ELECTION_YEAR = 1926

    CONSERVATIVE_SEATS = 91
    LIBERAL_SEATS = 116
    PROGRESSIVE_SEATS = 11
    UF_ALBERTA_SEATS = 11
    LIBERAL_PROGRESSIVE_SEATS = 8
    LABOUR_SEATS = 4
    INDEPENDENT_SEATS = 3
    UF_ONTARIO_SEATS = 1


    total_seats = (CONSERVATIVE_SEATS + LIBERAL_SEATS + PROGRESSIVE_SEATS + UF_ALBERTA_SEATS + LIBERAL_PROGRESSIVE_SEATS + LABOUR_SEATS + INDEPENDENT_SEATS + UF_ONTARIO_SEATS)

    sorted_parliament_seats = generateParliamentChartFiles.create_parliament_seating_plan_1926(CONSERVATIVE_SEATS, LIBERAL_SEATS, PROGRESSIVE_SEATS, UF_ALBERTA_SEATS, LIBERAL_PROGRESSIVE_SEATS, LABOUR_SEATS, INDEPENDENT_SEATS, UF_ONTARIO_SEATS)

    parliament_chart = generateParliamentChartFiles.generateParliamentChart(total_seats, sorted_parliament_seats)

    createParliamentChartFile(parliament_chart, ELECTION_YEAR)

    ### Generate election page in main folder
    generateHtmlMapFiles.generateElectionMapFile(ELECTION_YEAR)


def election1930():
    ELECTION_YEAR = 1930

    CONSERVATIVE_SEATS = 137
    LIBERAL_SEATS = 88
    PROGRESSIVE_SEATS = 2
    UF_ALBERTA_SEATS = 9
    LIBERAL_PROGRESSIVE_SEATS = 3
    LABOUR_SEATS = 2
    INDEPENDENT_SEATS = 3


    total_seats = (CONSERVATIVE_SEATS + LIBERAL_SEATS + PROGRESSIVE_SEATS + UF_ALBERTA_SEATS + LIBERAL_PROGRESSIVE_SEATS + LABOUR_SEATS + INDEPENDENT_SEATS)

    sorted_parliament_seats = generateParliamentChartFiles.create_parliament_seating_plan_1930(CONSERVATIVE_SEATS, LIBERAL_SEATS, PROGRESSIVE_SEATS, UF_ALBERTA_SEATS, LIBERAL_PROGRESSIVE_SEATS, LABOUR_SEATS, INDEPENDENT_SEATS)

    parliament_chart = generateParliamentChartFiles.generateParliamentChart(total_seats, sorted_parliament_seats)

    createParliamentChartFile(parliament_chart, ELECTION_YEAR)

    ### Generate election page in main folder
    generateHtmlMapFiles.generateElectionMapFile(ELECTION_YEAR)

def election1935():
    ELECTION_YEAR = 1935

    CONSERVATIVE_SEATS = 39
    LIBERAL_SEATS = 173
    SOCIAL_CREDIT_SEATS = 17
    CC_FEDERATION_SEATS = 7
    LIBERAL_PROGRESSIVE_SEATS = 4
    INDEPENDENT_SEATS = 3
    RECONSTRUCTION_SEATS = 1
    UF_ONTARIO_SEATS = 1


    total_seats = (CONSERVATIVE_SEATS + LIBERAL_SEATS + SOCIAL_CREDIT_SEATS + CC_FEDERATION_SEATS + LIBERAL_PROGRESSIVE_SEATS + INDEPENDENT_SEATS + RECONSTRUCTION_SEATS + UF_ONTARIO_SEATS)

    sorted_parliament_seats = generateParliamentChartFiles.create_parliament_seating_plan_1935(CONSERVATIVE_SEATS, LIBERAL_SEATS, SOCIAL_CREDIT_SEATS, CC_FEDERATION_SEATS, LIBERAL_PROGRESSIVE_SEATS, INDEPENDENT_SEATS, RECONSTRUCTION_SEATS, UF_ONTARIO_SEATS)

    parliament_chart = generateParliamentChartFiles.generateParliamentChart(total_seats, sorted_parliament_seats)

    createParliamentChartFile(parliament_chart, ELECTION_YEAR)

    ### Generate election page in main folder
    generateHtmlMapFiles.generateElectionMapFile(ELECTION_YEAR)


def election1940():
    ELECTION_YEAR = 1940

    CONSERVATIVE_SEATS = 39
    LIBERAL_SEATS = 179
    SOCIAL_CREDIT_SEATS = 7
    CC_FEDERATION_SEATS = 8
    LIBERAL_PROGRESSIVE_SEATS = 3
    INDEPENDENT_SEATS = 4
    NEW_DEMOCRACY = 3
    UNITED_REFORM = 2


    total_seats = (CONSERVATIVE_SEATS + LIBERAL_SEATS + SOCIAL_CREDIT_SEATS + CC_FEDERATION_SEATS + LIBERAL_PROGRESSIVE_SEATS + INDEPENDENT_SEATS + NEW_DEMOCRACY + UNITED_REFORM)

    sorted_parliament_seats = generateParliamentChartFiles.create_parliament_seating_plan_1940(CONSERVATIVE_SEATS, LIBERAL_SEATS, SOCIAL_CREDIT_SEATS, CC_FEDERATION_SEATS, LIBERAL_PROGRESSIVE_SEATS, INDEPENDENT_SEATS, NEW_DEMOCRACY, UNITED_REFORM)

    parliament_chart = generateParliamentChartFiles.generateParliamentChart(total_seats, sorted_parliament_seats)

    createParliamentChartFile(parliament_chart, ELECTION_YEAR)

    ### Generate election page in main folder
    generateHtmlMapFiles.generateElectionMapFile(ELECTION_YEAR)


def election1945():
    ELECTION_YEAR = 1945

    PROGRESSIVE_CONSERVATIVE_SEATS = 66
    LIBERAL_SEATS = 118
    CC_FEDERATION_SEATS = 28
    INDEPENDENT_SEATS = 16
    SOCIAL_CREDIT_SEATS = 13
    BLOC_POPULAIRE = 2
    LABOR_PROGRESSIVE = 1
    LIBERAL_PROGRESSIVE_SEATS = 1


    total_seats = (PROGRESSIVE_CONSERVATIVE_SEATS + LIBERAL_SEATS + CC_FEDERATION_SEATS + INDEPENDENT_SEATS + SOCIAL_CREDIT_SEATS + BLOC_POPULAIRE + LABOR_PROGRESSIVE + LIBERAL_PROGRESSIVE_SEATS)

    sorted_parliament_seats = generateParliamentChartFiles.create_parliament_seating_plan_1945(PROGRESSIVE_CONSERVATIVE_SEATS, LIBERAL_SEATS, CC_FEDERATION_SEATS, INDEPENDENT_SEATS, SOCIAL_CREDIT_SEATS, BLOC_POPULAIRE, LABOR_PROGRESSIVE, LIBERAL_PROGRESSIVE_SEATS)

    parliament_chart = generateParliamentChartFiles.generateParliamentChart(total_seats, sorted_parliament_seats)

    createParliamentChartFile(parliament_chart, ELECTION_YEAR)

    ### Generate election page in main folder
    generateHtmlMapFiles.generateElectionMapFile(ELECTION_YEAR)


def election1949():
    ELECTION_YEAR = 1949

    PROGRESSIVE_CONSERVATIVE_SEATS = 41
    LIBERAL_SEATS = 191
    CC_FEDERATION_SEATS = 13
    SOCIAL_CREDIT_SEATS = 10
    INDEPENDENT_SEATS = 5
    LIBERAL_PROGRESSIVE_SEATS = 1
    LIBERAL_LABOUR_SEATS = 1


    total_seats = (PROGRESSIVE_CONSERVATIVE_SEATS + LIBERAL_SEATS + CC_FEDERATION_SEATS + SOCIAL_CREDIT_SEATS + INDEPENDENT_SEATS + LIBERAL_PROGRESSIVE_SEATS + LIBERAL_LABOUR_SEATS)

    sorted_parliament_seats = generateParliamentChartFiles.create_parliament_seating_plan_1949(PROGRESSIVE_CONSERVATIVE_SEATS, LIBERAL_SEATS, CC_FEDERATION_SEATS, SOCIAL_CREDIT_SEATS, INDEPENDENT_SEATS, LIBERAL_PROGRESSIVE_SEATS, LIBERAL_LABOUR_SEATS)

    parliament_chart = generateParliamentChartFiles.generateParliamentChart(total_seats, sorted_parliament_seats)

    createParliamentChartFile(parliament_chart, ELECTION_YEAR)

    ### Generate election page in main folder
    generateHtmlMapFiles.generateElectionMapFile(ELECTION_YEAR)


def election1953():
    ELECTION_YEAR = 1953

    PROGRESSIVE_CONSERVATIVE_SEATS = 51
    LIBERAL_SEATS = 169
    CC_FEDERATION_SEATS = 23
    SOCIAL_CREDIT_SEATS = 15
    INDEPENDENT_SEATS = 5
    LIBERAL_PROGRESSIVE_SEATS = 1
    LIBERAL_LABOUR_SEATS = 1


    total_seats = (PROGRESSIVE_CONSERVATIVE_SEATS + LIBERAL_SEATS + CC_FEDERATION_SEATS + SOCIAL_CREDIT_SEATS + INDEPENDENT_SEATS + LIBERAL_PROGRESSIVE_SEATS + LIBERAL_LABOUR_SEATS)

    sorted_parliament_seats = generateParliamentChartFiles.create_parliament_seating_plan_1949(PROGRESSIVE_CONSERVATIVE_SEATS, LIBERAL_SEATS, CC_FEDERATION_SEATS, SOCIAL_CREDIT_SEATS, INDEPENDENT_SEATS, LIBERAL_PROGRESSIVE_SEATS, LIBERAL_LABOUR_SEATS)

    parliament_chart = generateParliamentChartFiles.generateParliamentChart(total_seats, sorted_parliament_seats)

    createParliamentChartFile(parliament_chart, ELECTION_YEAR)

    ### Generate election page in main folder
    generateHtmlMapFiles.generateElectionMapFile(ELECTION_YEAR)


def election1957():
    ELECTION_YEAR = 1957

    PROGRESSIVE_CONSERVATIVE_SEATS = 111
    LIBERAL_SEATS = 103
    CC_FEDERATION_SEATS = 25
    SOCIAL_CREDIT_SEATS = 19
    INDEPENDENT_SEATS = 5
    LIBERAL_LABOUR_SEATS = 1


    total_seats = (PROGRESSIVE_CONSERVATIVE_SEATS + LIBERAL_SEATS + CC_FEDERATION_SEATS + SOCIAL_CREDIT_SEATS + INDEPENDENT_SEATS + LIBERAL_LABOUR_SEATS)

    sorted_parliament_seats = generateParliamentChartFiles.create_parliament_seating_plan_1957(PROGRESSIVE_CONSERVATIVE_SEATS, LIBERAL_SEATS, CC_FEDERATION_SEATS, SOCIAL_CREDIT_SEATS, INDEPENDENT_SEATS, LIBERAL_LABOUR_SEATS)

    parliament_chart = generateParliamentChartFiles.generateParliamentChart(total_seats, sorted_parliament_seats)

    createParliamentChartFile(parliament_chart, ELECTION_YEAR)

    ### Generate election page in main folder
    generateHtmlMapFiles.generateElectionMapFile(ELECTION_YEAR)


def election1958():
    ELECTION_YEAR = 1958

    PROGRESSIVE_CONSERVATIVE_SEATS = 208
    LIBERAL_SEATS = 48
    CC_FEDERATION_SEATS = 8
    LIBERAL_LABOUR_SEATS = 1


    total_seats = (PROGRESSIVE_CONSERVATIVE_SEATS + LIBERAL_SEATS + CC_FEDERATION_SEATS + LIBERAL_LABOUR_SEATS)

    sorted_parliament_seats = generateParliamentChartFiles.create_parliament_seating_plan_1958(PROGRESSIVE_CONSERVATIVE_SEATS, LIBERAL_SEATS, CC_FEDERATION_SEATS, LIBERAL_LABOUR_SEATS)

    parliament_chart = generateParliamentChartFiles.generateParliamentChart(total_seats, sorted_parliament_seats)

    createParliamentChartFile(parliament_chart, ELECTION_YEAR)

    ### Generate election page in main folder
    generateHtmlMapFiles.generateElectionMapFile(ELECTION_YEAR)


def election1962():
    ELECTION_YEAR = 1962

    PROGRESSIVE_CONSERVATIVE_SEATS = 116
    LIBERAL_SEATS = 99
    SOCIAL_CREDIT_SEATS = 30
    NEW_DEMOCRATIC_SEATS = 19
    LIBERAL_LABOUR_SEATS = 1


    total_seats = (PROGRESSIVE_CONSERVATIVE_SEATS + LIBERAL_SEATS + SOCIAL_CREDIT_SEATS + NEW_DEMOCRATIC_SEATS + LIBERAL_LABOUR_SEATS)

    sorted_parliament_seats = generateParliamentChartFiles.create_parliament_seating_plan_1962(PROGRESSIVE_CONSERVATIVE_SEATS, LIBERAL_SEATS, SOCIAL_CREDIT_SEATS, NEW_DEMOCRATIC_SEATS, LIBERAL_LABOUR_SEATS)

    parliament_chart = generateParliamentChartFiles.generateParliamentChart(total_seats, sorted_parliament_seats)

    createParliamentChartFile(parliament_chart, ELECTION_YEAR)

    ### Generate election page in main folder
    generateHtmlMapFiles.generateElectionMapFile(ELECTION_YEAR)


def election1963():
    ELECTION_YEAR = 1963

    PROGRESSIVE_CONSERVATIVE_SEATS = 95
    LIBERAL_SEATS = 128
    SOCIAL_CREDIT_SEATS = 24
    NEW_DEMOCRATIC_SEATS = 17
    LIBERAL_LABOUR_SEATS = 1


    total_seats = (PROGRESSIVE_CONSERVATIVE_SEATS + LIBERAL_SEATS + SOCIAL_CREDIT_SEATS + NEW_DEMOCRATIC_SEATS + LIBERAL_LABOUR_SEATS)

    sorted_parliament_seats = generateParliamentChartFiles.create_parliament_seating_plan_1963(PROGRESSIVE_CONSERVATIVE_SEATS, LIBERAL_SEATS, SOCIAL_CREDIT_SEATS, NEW_DEMOCRATIC_SEATS, LIBERAL_LABOUR_SEATS)

    parliament_chart = generateParliamentChartFiles.generateParliamentChart(total_seats, sorted_parliament_seats)

    createParliamentChartFile(parliament_chart, ELECTION_YEAR)

    ### Generate election page in main folder
    generateHtmlMapFiles.generateElectionMapFile(ELECTION_YEAR)


def election1965():
    ELECTION_YEAR = 1965

    PROGRESSIVE_CONSERVATIVE_SEATS = 97
    LIBERAL_SEATS = 131
    RALLIEMENT_SEATS = 9
    SOCIAL_CREDIT_SEATS = 5
    NEW_DEMOCRATIC_SEATS = 21
    INDEPENDENT_SEATS = 2


    total_seats = (PROGRESSIVE_CONSERVATIVE_SEATS + LIBERAL_SEATS + SOCIAL_CREDIT_SEATS + NEW_DEMOCRATIC_SEATS + RALLIEMENT_SEATS + INDEPENDENT_SEATS)

    sorted_parliament_seats = generateParliamentChartFiles.create_parliament_seating_plan_1965(PROGRESSIVE_CONSERVATIVE_SEATS, LIBERAL_SEATS, SOCIAL_CREDIT_SEATS, NEW_DEMOCRATIC_SEATS, RALLIEMENT_SEATS, INDEPENDENT_SEATS)

    parliament_chart = generateParliamentChartFiles.generateParliamentChart(total_seats, sorted_parliament_seats)

    createParliamentChartFile(parliament_chart, ELECTION_YEAR)

    ### Generate election page in main folder
    generateHtmlMapFiles.generateElectionMapFile(ELECTION_YEAR)


def election1968():
    ELECTION_YEAR = 1968

    PROGRESSIVE_CONSERVATIVE_SEATS = 72
    LIBERAL_SEATS = 154
    RALLIEMENT_SEATS = 14
    NEW_DEMOCRATIC_SEATS = 22
    INDEPENDENT_SEATS = 1
    LIBERAL_LABOUR_SEATS = 1


    total_seats = (PROGRESSIVE_CONSERVATIVE_SEATS + LIBERAL_SEATS + NEW_DEMOCRATIC_SEATS + RALLIEMENT_SEATS + INDEPENDENT_SEATS + LIBERAL_LABOUR_SEATS)

    sorted_parliament_seats = generateParliamentChartFiles.create_parliament_seating_plan_1968(PROGRESSIVE_CONSERVATIVE_SEATS, LIBERAL_SEATS, NEW_DEMOCRATIC_SEATS, RALLIEMENT_SEATS, INDEPENDENT_SEATS, LIBERAL_LABOUR_SEATS)

    parliament_chart = generateParliamentChartFiles.generateParliamentChart(total_seats, sorted_parliament_seats)

    createParliamentChartFile(parliament_chart, ELECTION_YEAR)

    ### Generate election page in main folder
    generateHtmlMapFiles.generateElectionMapFile(ELECTION_YEAR)


def election1972():
    ELECTION_YEAR = 1972
    
    PROGRESSIVE_CONSERVATIVE_SEATS = 107
    LIBERAL_SEATS = 109
    NEW_DEMOCRATIC_SEATS = 31
    SOCIAL_CREDIT_SEATS = 15
    INDEPENDENT_SEATS = 1
    NO_AFFILIATION_SEATS = 1


    total_seats = (PROGRESSIVE_CONSERVATIVE_SEATS + LIBERAL_SEATS + NEW_DEMOCRATIC_SEATS + SOCIAL_CREDIT_SEATS + INDEPENDENT_SEATS + NO_AFFILIATION_SEATS)

    sorted_parliament_seats = generateParliamentChartFiles.create_parliament_seating_plan_1972(PROGRESSIVE_CONSERVATIVE_SEATS, LIBERAL_SEATS, NEW_DEMOCRATIC_SEATS, SOCIAL_CREDIT_SEATS, INDEPENDENT_SEATS, NO_AFFILIATION_SEATS)

    parliament_chart = generateParliamentChartFiles.generateParliamentChart(total_seats, sorted_parliament_seats)

    createParliamentChartFile(parliament_chart, ELECTION_YEAR)

    ### Generate election page in main folder
    generateHtmlMapFiles.generateElectionMapFile(ELECTION_YEAR)


def election1974():
    ELECTION_YEAR = 1974

    PROGRESSIVE_CONSERVATIVE_SEATS = 95
    LIBERAL_SEATS = 141
    NEW_DEMOCRATIC_SEATS = 16
    SOCIAL_CREDIT_SEATS = 11
    INDEPENDENT_SEATS = 1


    total_seats = (PROGRESSIVE_CONSERVATIVE_SEATS + LIBERAL_SEATS + NEW_DEMOCRATIC_SEATS + SOCIAL_CREDIT_SEATS + INDEPENDENT_SEATS)

    sorted_parliament_seats = generateParliamentChartFiles.create_parliament_seating_plan_1974(PROGRESSIVE_CONSERVATIVE_SEATS, LIBERAL_SEATS, NEW_DEMOCRATIC_SEATS, SOCIAL_CREDIT_SEATS, INDEPENDENT_SEATS)

    parliament_chart = generateParliamentChartFiles.generateParliamentChart(total_seats, sorted_parliament_seats)

    createParliamentChartFile(parliament_chart, ELECTION_YEAR)

    ### Generate election page in main folder
    generateHtmlMapFiles.generateElectionMapFile(ELECTION_YEAR)


def election1979():
    ELECTION_YEAR = 1979

    PROGRESSIVE_CONSERVATIVE_SEATS = 136
    LIBERAL_SEATS = 114
    NEW_DEMOCRATIC_SEATS = 26
    SOCIAL_CREDIT_SEATS = 6


    total_seats = (PROGRESSIVE_CONSERVATIVE_SEATS + LIBERAL_SEATS + NEW_DEMOCRATIC_SEATS + SOCIAL_CREDIT_SEATS)

    sorted_parliament_seats = generateParliamentChartFiles.create_parliament_seating_plan_1979(PROGRESSIVE_CONSERVATIVE_SEATS, LIBERAL_SEATS, NEW_DEMOCRATIC_SEATS, SOCIAL_CREDIT_SEATS)

    parliament_chart = generateParliamentChartFiles.generateParliamentChart(total_seats, sorted_parliament_seats)

    createParliamentChartFile(parliament_chart, ELECTION_YEAR)

    ### Generate election page in main folder
    generateHtmlMapFiles.generateElectionMapFile(ELECTION_YEAR)


def election2019():
    ELECTION_YEAR = 2019
    
    CON_SEATS = 121
    LIB_SEATS = 157
    NDP_SEATS = 24
    GREEN_SEATS = 3
    BLOQ_SEATS = 32
    INDEPENDENT_SEATS = 1


    total_seats = (CON_SEATS + LIB_SEATS + NDP_SEATS + GREEN_SEATS + BLOQ_SEATS + INDEPENDENT_SEATS)

    sorted_parliament_seats = generateParliamentChartFiles.create_parliament_seating_plan_2019(CON_SEATS, LIB_SEATS, NDP_SEATS, GREEN_SEATS, BLOQ_SEATS, INDEPENDENT_SEATS)

    parliament_chart = generateParliamentChartFiles.generateParliamentChart(total_seats, sorted_parliament_seats)

    createParliamentChartFile(parliament_chart, ELECTION_YEAR)

    ### Generate election page in main folder
    generateHtmlMapFiles.generateElectionMapFile(ELECTION_YEAR)


def election2021():
    ELECTION_YEAR = 2021

    CON_SEATS = 119
    LIB_SEATS = 160
    NDP_SEATS = 25
    GREEN_SEATS = 2
    BLOQ_SEATS = 32
    INDEPENDENT_SEATS = 0


    total_seats = (CON_SEATS + LIB_SEATS + NDP_SEATS + GREEN_SEATS + BLOQ_SEATS + INDEPENDENT_SEATS)

    sorted_parliament_seats = generateParliamentChartFiles.create_parliament_seating_plan_2019(CON_SEATS, LIB_SEATS, NDP_SEATS, GREEN_SEATS, BLOQ_SEATS, INDEPENDENT_SEATS)

    parliament_chart = generateParliamentChartFiles.generateParliamentChart(total_seats, sorted_parliament_seats)

    createParliamentChartFile(parliament_chart, ELECTION_YEAR)

    ### Generate election page in main folder
    generateHtmlMapFiles.generateElectionMapFile(ELECTION_YEAR)


def main():
    elections = [election1867, election1872, election1874, election1878, election1882,
                 election1887, election1891, election1896, election1900, election1904,
                 election1908, election1911, election1917, election1921, election1925,
                 election1926, election1930, election1935, election1940, election1945,
                 election1949, election1953, election1957, election1958, election1962,
                 election1963, election1965, election1968, election1972, election1974,
                 election1979, election2019, election2021]
    
    for election_function in elections:
        election_function()

if __name__ == "__main__":
    main()