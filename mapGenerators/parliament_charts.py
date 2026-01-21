def generateParliamentChart(total_seats, sorted_parliament_seats):
    parliament_chart = ''
    if total_seats <= 308:
        number_of_seats_per_row = int(round(total_seats / 2 / 5)) ### 5 rows
    else:
        number_of_seats_per_row = int(round(total_seats / 2 / 6)) ### 6 rows
    current_seat = 0
    future_seat = 0

    first_row = "<div class='first_row'>"
    second_row = "<div class='second_row'>"
    third_row = "<div class='third_row'>"
    fourth_row = "<div class='fourth_row'>"
    fifth_row = "<div class='fifth_row'>"
    sixth_row = "<div class='sixth_row'>"
    seventh_row = "<div class='seventh_row'>"
    eighth_row = "<div class='eighth_row'>"
    ninth_row = "<div class='ninth_row'>"
    tenth_row = "<div class='tenth_row'>"
    eleventh_row = "<div class='eleventh_row'>"
    twelfth_row = "<div class='twelfth_row'>"
    thirteenth_row = "<div class='thirteenth_row'>"
    speaker_row = "<div class='speaker_row'>"


    ### POPULATE SPEAKER ROW (SIXTH ROW)
    if total_seats <= 308:
        speaker_row += '<span class="' + sorted_parliament_seats[current_seat] +'_dot"></span></div>'
    else:
        speaker_row += '<span class="' + sorted_parliament_seats[current_seat] +'_dot"></span></div>'
    current_seat += 1


    ### POPULATE GOVERNING PARTY SECTION

    if total_seats <= 308:
        for i in range(number_of_seats_per_row):
            eleventh_row += '<span class="' + sorted_parliament_seats[current_seat] +'_dot"></span>'
            tenth_row += '<span class="' + sorted_parliament_seats[current_seat + 1] +'_dot"></span>'
            ninth_row += '<span class="' + sorted_parliament_seats[current_seat + 2] +'_dot"></span>'
            eighth_row += '<span class="' + sorted_parliament_seats[current_seat + 3] +'_dot"></span>'
            seventh_row += '<span class="' + sorted_parliament_seats[current_seat + 4] +'_dot"></span>'

            current_seat += 5
            future_seat = current_seat
        
        eleventh_row += "</div>"
        tenth_row += "</div>"
        ninth_row += "</div>"
        eighth_row += "</div>"
        seventh_row += "</div>"
    
    else:
        for i in range(number_of_seats_per_row):
            thirteenth_row += '<span class="' + sorted_parliament_seats[current_seat] +'_dot"></span>'
            twelfth_row += '<span class="' + sorted_parliament_seats[current_seat + 1] +'_dot"></span>'
            eleventh_row += '<span class="' + sorted_parliament_seats[current_seat + 2] +'_dot"></span>'
            tenth_row += '<span class="' + sorted_parliament_seats[current_seat + 3] +'_dot"></span>'
            ninth_row += '<span class="' + sorted_parliament_seats[current_seat + 4] +'_dot"></span>'
            eighth_row += '<span class="' + sorted_parliament_seats[current_seat + 5] +'_dot"></span>'

            current_seat += 6
            future_seat = current_seat
        
        thirteenth_row += "</div>"
        twelfth_row += "</div>"
        eleventh_row += "</div>"
        tenth_row += "</div>"
        ninth_row += "</div>"
        eighth_row += "</div>"


    ### POPULATE OPPOSITION SECTION
    if number_of_seats_per_row == 21 or number_of_seats_per_row == 24 \
        or number_of_seats_per_row == 26 \
        or number_of_seats_per_row == 28:
        number_of_seats_per_row += 1

    if total_seats <= 308:
        for i in range(number_of_seats_per_row):

            if (future_seat) < total_seats:
                fifth_row += '<span class="' + sorted_parliament_seats[future_seat] +'_dot"></span>'
            if (future_seat + 1) < total_seats:
                fourth_row += '<span class="' + sorted_parliament_seats[future_seat + 1] +'_dot"></span>'
            if (future_seat + 2) < total_seats:
                third_row += '<span class="' + sorted_parliament_seats[future_seat + 2] +'_dot"></span>'
            if (future_seat + 3) < total_seats:
                second_row += '<span class="' + sorted_parliament_seats[future_seat + 3] +'_dot"></span>'
            if (future_seat + 4) < total_seats:
                first_row += '<span class="' + sorted_parliament_seats[future_seat + 4] +'_dot"></span>'

            future_seat += 5

        fifth_row += "</div>"
        fourth_row += "</div>"
        third_row += "</div>"
        second_row += "</div>"
        first_row += "</div>"
        speaker_row += "</div>"

        parliament_chart = first_row + "\n" + second_row + "\n" + third_row + "\n" \
            + fourth_row + "\n" + fifth_row + "\n" + speaker_row + "\n" \
            + seventh_row + "\n" + eighth_row + "\n" + ninth_row + "\n" \
            + tenth_row + "\n" + eleventh_row + "\n"
    
    else:
        for i in range(number_of_seats_per_row):

            if (future_seat) < total_seats:
                sixth_row += '<span class="' + sorted_parliament_seats[future_seat] +'_dot"></span>'
            if (future_seat + 1) < total_seats:
                fifth_row += '<span class="' + sorted_parliament_seats[future_seat + 1] +'_dot"></span>'
            if (future_seat + 2) < total_seats:
                fourth_row += '<span class="' + sorted_parliament_seats[future_seat + 2] +'_dot"></span>'
            if (future_seat + 3) < total_seats:
                third_row += '<span class="' + sorted_parliament_seats[future_seat + 3] +'_dot"></span>'
            if (future_seat + 4) < total_seats:
                second_row += '<span class="' + sorted_parliament_seats[future_seat + 4] +'_dot"></span>'
            if (future_seat + 5) < total_seats:
                first_row += '<span class="' + sorted_parliament_seats[future_seat + 5] +'_dot"></span>'

            future_seat += 6

        sixth_row += "</div>"
        fifth_row += "</div>"
        fourth_row += "</div>"
        third_row += "</div>"
        second_row += "</div>"
        first_row += "</div>"
        speaker_row += "</div>"


        parliament_chart = first_row + "\n" + second_row + "\n" + third_row + "\n" \
            + fourth_row + "\n" + fifth_row + "\n" + sixth_row + "\n" \
            + speaker_row + "\n" + eighth_row + "\n" + ninth_row + "\n" \
            + tenth_row + "\n" + eleventh_row + "\n" + twelfth_row + "\n" \
            + thirteenth_row + "\n"
    

    return parliament_chart


def create_parliament_seating_plan_1867(con_seats, lib_seats, anti_con_seats, empty_seats):
    parliament_seats = []

    for i in range(con_seats):
        parliament_seats.append('Conservative')
    for i in range(lib_seats):
        parliament_seats.append('Liberal')
    for i in range(anti_con_seats):
        parliament_seats.append('Anti-Confederation')
    for i in range(empty_seats):
        parliament_seats.append('Vacant')

    return parliament_seats


def create_parliament_seating_plan_1872(con_seats, lib_seats, independent_seats):
    parliament_seats = []

    for i in range(con_seats):
        parliament_seats.append('Conservative')
    for i in range(lib_seats):
        parliament_seats.append('Liberal')
    for i in range(independent_seats):
        parliament_seats.append('Independent')

    return parliament_seats


def create_parliament_seating_plan_1874(con_seats, lib_seats, independent_seats):
    parliament_seats = []

    for i in range(lib_seats):
        parliament_seats.append('Liberal')
    for i in range(con_seats):
        parliament_seats.append('Conservative')
    for i in range(independent_seats):
        parliament_seats.append('Independent')

    return parliament_seats

def create_parliament_seating_plan_1878(con_seats, lib_seats, independent_seats, nationalist_seats):
    parliament_seats = []

    for i in range(con_seats):
        parliament_seats.append('Conservative')
    for i in range(lib_seats):
        parliament_seats.append('Liberal')
    for i in range(independent_seats):
        parliament_seats.append('Independent')
    for i in range(independent_seats):
        parliament_seats.append('Nationalist-Conservative')

    return parliament_seats


def create_parliament_seating_plan_1896(con_seats, lib_seats, independent_seats, patrons_seats, mccarthy_seats):
    parliament_seats = []

    for i in range(lib_seats):
        parliament_seats.append('Liberal')
    for i in range(con_seats):
        parliament_seats.append('Conservative')
    for i in range(independent_seats):
        parliament_seats.append('Independent')
    for i in range(patrons_seats):
        parliament_seats.append('Patrons-of-Industry')
    for i in range(mccarthy_seats):
        parliament_seats.append('McCarthyite')

    return parliament_seats

def create_parliament_seating_plan_1908(con_seats, lib_seats, independent_seats, labour_seats):
    parliament_seats = []

    for i in range(lib_seats):
        parliament_seats.append('Liberal')
    for i in range(con_seats):
        parliament_seats.append('Conservative')
    for i in range(independent_seats):
        parliament_seats.append('Independent')
    for i in range(labour_seats):
        parliament_seats.append('Labour')

    return parliament_seats

def create_parliament_seating_plan_1911(con_seats, lib_seats, independent_seats, labour_seats):
    parliament_seats = []

    for i in range(con_seats):
        parliament_seats.append('Conservative')
    for i in range(lib_seats):
        parliament_seats.append('Liberal')
    for i in range(independent_seats):
        parliament_seats.append('Independent')
    for i in range(labour_seats):
        parliament_seats.append('Labour')
        
    return parliament_seats

def create_parliament_seating_plan_1917(unionist_seats, opposition_seats):
    parliament_seats = []

    for i in range(unionist_seats):
        parliament_seats.append('Unionist')
    for i in range(opposition_seats):
        parliament_seats.append('Opposition')

    return parliament_seats

def create_parliament_seating_plan_1921(con_seats, lib_seats, progressive_seats, uf_alberta_seats, labour_seats, independent_seats, uf_ontario_seats):
    parliament_seats = []

    for i in range(lib_seats):
        parliament_seats.append('Liberal')
    for i in range(con_seats):
        parliament_seats.append('Conservative')
    for i in range(progressive_seats):
        parliament_seats.append('Progressive')
    for i in range(independent_seats):
        parliament_seats.append('Independent')
    for i in range(labour_seats):
        parliament_seats.append('Labour')
    for i in range(uf_alberta_seats):
        parliament_seats.append('United-Farmers-of-Alberta')
    for i in range(uf_ontario_seats):
        parliament_seats.append('United-Farmers-of-Ontario')

    return parliament_seats

def create_parliament_seating_plan_1925(con_seats, lib_seats, progressive_seats, uf_alberta_seats, labour_seats, independent_seats):
    parliament_seats = []

    for i in range(lib_seats):
        parliament_seats.append('Liberal')
    for i in range(progressive_seats):
        parliament_seats.append('Progressive')
    for i in range(uf_alberta_seats):
        parliament_seats.append('United-Farmers-of-Alberta')
    for i in range(labour_seats):
        parliament_seats.append('Labour')
    for i in range(con_seats):
        parliament_seats.append('Conservative')
    for i in range(independent_seats):
        parliament_seats.append('Independent')

    return parliament_seats

def create_parliament_seating_plan_1926(con_seats, lib_seats, progressive_seats, uf_alberta_seats, liberal_progressive_seats, labour_seats, independent_seats, uf_ontario_seats):
    parliament_seats = []

    for i in range(lib_seats):
        parliament_seats.append('Liberal')
    for i in range(liberal_progressive_seats):
        parliament_seats.append('Liberal-Progressive')
    for i in range(independent_seats):
        parliament_seats.append('Independent')
    for i in range(con_seats):
        parliament_seats.append('Conservative')
    for i in range(progressive_seats):
        parliament_seats.append('Progressive')
    for i in range(uf_alberta_seats):
        parliament_seats.append('United-Farmers-of-Alberta')
    for i in range(labour_seats):
        parliament_seats.append('Labour')
    for i in range(uf_ontario_seats):
        parliament_seats.append('United-Farmers-of-Ontario')

    return parliament_seats

def create_parliament_seating_plan_1930(con_seats, lib_seats, progressive_seats, uf_alberta_seats, liberal_progressive_seats, labour_seats, independent_seats):
    parliament_seats = []

    for i in range(con_seats):
        parliament_seats.append('Conservative')
    for i in range(lib_seats):
        parliament_seats.append('Liberal')
    for i in range(uf_alberta_seats):
        parliament_seats.append('United-Farmers-of-Alberta')
    for i in range(liberal_progressive_seats):
        parliament_seats.append('Liberal-Progressive')
    for i in range(independent_seats):
        parliament_seats.append('Independent')
    for i in range(progressive_seats):
        parliament_seats.append('Progressive')
    for i in range(labour_seats):
        parliament_seats.append('Labour')

    return parliament_seats

def create_parliament_seating_plan_1935(con_seats, lib_seats, social_credit_seats, cc_federation_seats, liberal_progressive_seats, independent_seats, reconstruction_seats, uf_ontario_seats):
    parliament_seats = []

    for i in range(lib_seats):
        parliament_seats.append('Liberal')
    for i in range(con_seats):
        parliament_seats.append('Conservative')
    for i in range(social_credit_seats):
        parliament_seats.append('Social-Credit')
    for i in range(cc_federation_seats):
        parliament_seats.append('Co-operative-Commonwealth-Federation')
    for i in range(liberal_progressive_seats):
        parliament_seats.append('Liberal-Progressive')
    for i in range(independent_seats):
        parliament_seats.append('Independent')
    for i in range(reconstruction_seats):
        parliament_seats.append('Reconstruction-Party')
    for i in range(uf_ontario_seats):
        parliament_seats.append('United-Farmers-of-Ontario')

    return parliament_seats

def create_parliament_seating_plan_1940(con_seats, lib_seats, social_credit_seats, cc_federation_seats, liberal_progressive_seats, independent_seats, new_democracy_seats, united_reform_seats):
    parliament_seats = []

    for i in range(lib_seats):
        parliament_seats.append('Liberal')
    for i in range(con_seats):
        parliament_seats.append('National-Government')
    for i in range(cc_federation_seats):
        parliament_seats.append('Co-operative-Commonwealth-Federation')
    for i in range(social_credit_seats):
        parliament_seats.append('Social-Credit')
    for i in range(new_democracy_seats):
        parliament_seats.append('New-Democracy')
    for i in range(liberal_progressive_seats):
        parliament_seats.append('Liberal-Progressive')
    for i in range(independent_seats):
        parliament_seats.append('Independent')
    for i in range(united_reform_seats):
        parliament_seats.append('United-Reform')

    return parliament_seats

def create_parliament_seating_plan_1945(prog_con_seats, lib_seats, cc_federation_seats, independent_seats, social_credit_seats, bloc_populaire_seats, labor_progressive_seats, liberal_progressive_seats):
    parliament_seats = []

    for i in range(lib_seats):
        parliament_seats.append('Liberal')
    for i in range(prog_con_seats):
        parliament_seats.append('Progressive-Conservative')
    for i in range(cc_federation_seats):
        parliament_seats.append('Co-operative-Commonwealth-Federation')
    for i in range(independent_seats):
        parliament_seats.append('Independent')
    for i in range(social_credit_seats):
        parliament_seats.append('Social-Credit')
    for i in range(bloc_populaire_seats):
        parliament_seats.append('Bloc-populaire')
    for i in range(labor_progressive_seats):
        parliament_seats.append('Labor-Progressive')
    for i in range(liberal_progressive_seats):
        parliament_seats.append('Liberal-Progressive')

    return parliament_seats

def create_parliament_seating_plan_1949(prog_con_seats, lib_seats, cc_federation_seats, social_credit_seats, independent_seats, liberal_progressive_seats, liberal_labor_seats):
    parliament_seats = []

    for i in range(lib_seats):
        parliament_seats.append('Liberal')
    for i in range(prog_con_seats):
        parliament_seats.append('Progressive-Conservative')
    for i in range(cc_federation_seats):
        parliament_seats.append('Co-operative-Commonwealth-Federation')
    for i in range(social_credit_seats):
        parliament_seats.append('Social-Credit')
    for i in range(independent_seats):
        parliament_seats.append('Independent')
    for i in range(liberal_progressive_seats):
        parliament_seats.append('Liberal-Progressive')
    for i in range(liberal_labor_seats):
        parliament_seats.append('Liberal-Labour')

    return parliament_seats

def create_parliament_seating_plan_1957(prog_con_seats, lib_seats, cc_federation_seats, social_credit_seats, independent_seats, liberal_labor_seats):
    parliament_seats = []

    for i in range(prog_con_seats):
        parliament_seats.append('Progressive-Conservative')
    for i in range(social_credit_seats):
        parliament_seats.append('Social-Credit')
    for i in range(lib_seats):
        parliament_seats.append('Liberal')
    for i in range(cc_federation_seats):
        parliament_seats.append('Co-operative-Commonwealth-Federation')
    for i in range(independent_seats):
        parliament_seats.append('Independent')
    for i in range(liberal_labor_seats):
        parliament_seats.append('Liberal-Labour')

    return parliament_seats

def create_parliament_seating_plan_1958(prog_con_seats, lib_seats, cc_federation_seats, liberal_labor_seats):
    parliament_seats = []

    for i in range(prog_con_seats):
        parliament_seats.append('Progressive-Conservative')
    for i in range(lib_seats):
        parliament_seats.append('Liberal')
    for i in range(cc_federation_seats):
        parliament_seats.append('Co-operative-Commonwealth-Federation')
    for i in range(liberal_labor_seats):
        parliament_seats.append('Liberal-Labour')

    return parliament_seats

def create_parliament_seating_plan_1962(prog_con_seats, lib_seats, social_credit_seats, new_democratic_seats, liberal_labor_seats):
    parliament_seats = []

    for i in range(prog_con_seats):
        parliament_seats.append('Progressive-Conservative')
    for i in range(new_democratic_seats):
        parliament_seats.append('New-Democratic')
    for i in range(lib_seats):
        parliament_seats.append('Liberal')
    for i in range(social_credit_seats):
        parliament_seats.append('Social-Credit')
    for i in range(liberal_labor_seats):
        parliament_seats.append('Liberal-Labour')

    return parliament_seats

def create_parliament_seating_plan_1963(prog_con_seats, lib_seats, social_credit_seats, new_democratic_seats, liberal_labor_seats):
    parliament_seats = []

    for i in range(lib_seats):
        parliament_seats.append('Liberal')
    for i in range(prog_con_seats):
        parliament_seats.append('Progressive-Conservative')
    for i in range(social_credit_seats):
        parliament_seats.append('Social-Credit')
    for i in range(new_democratic_seats):
        parliament_seats.append('New-Democratic')
    for i in range(liberal_labor_seats):
        parliament_seats.append('Liberal-Labour')

    return parliament_seats

def create_parliament_seating_plan_1965(prog_con_seats, lib_seats, social_credit_seats, new_democratic_seats, ralliement_seats, independent_seats):
    parliament_seats = []

    for i in range(lib_seats):
        parliament_seats.append('Liberal')
    for i in range(prog_con_seats):
        parliament_seats.append('Progressive-Conservative')
    for i in range(new_democratic_seats):
        parliament_seats.append('New-Democratic')
    for i in range(ralliement_seats):
        parliament_seats.append('Ralliement')
    for i in range(social_credit_seats):
        parliament_seats.append('Social-Credit')
    for i in range(independent_seats):
        parliament_seats.append('Independent')

    return parliament_seats

def create_parliament_seating_plan_1968(prog_con_seats, lib_seats, new_democratic_seats, ralliement_seats, independent_seats, liberal_labor_seats):
    parliament_seats = []

    for i in range(lib_seats):
        parliament_seats.append('Liberal')
    for i in range(prog_con_seats):
        parliament_seats.append('Progressive-Conservative')
    for i in range(new_democratic_seats):
        parliament_seats.append('New-Democratic')
    for i in range(ralliement_seats):
        parliament_seats.append('Ralliement')
    for i in range(independent_seats):
        parliament_seats.append('Independent')
    for i in range(liberal_labor_seats):
        parliament_seats.append('Liberal-Labour')

    return parliament_seats

def create_parliament_seating_plan_1972(prog_con_seats, lib_seats, new_democratic_seats, social_credit_seats, independent_seats, no_affiliation_seats):
    parliament_seats = []

    for i in range(lib_seats):
        parliament_seats.append('Liberal')
    for i in range(social_credit_seats):
        parliament_seats.append('Social-Credit')
    for i in range(prog_con_seats):
        parliament_seats.append('Progressive-Conservative')
    for i in range(new_democratic_seats):
        parliament_seats.append('New-Democratic')
    for i in range(independent_seats):
        parliament_seats.append('Independent')
    for i in range(no_affiliation_seats):
        parliament_seats.append('No-Affiliation')

    return parliament_seats

def create_parliament_seating_plan_2019(con_seats, lib_seats, ndp_seats, green_seats, bloq_seats, independent_seats):
    parliament_seats = []

    for i in range(lib_seats):
        parliament_seats.append('Liberal')
    for i in range(con_seats):
        parliament_seats.append('Conservative')
    for i in range(ndp_seats):
        parliament_seats.append('NDP')
    for i in range(bloq_seats):
        parliament_seats.append('Bloq-Quebecois')
    for i in range(green_seats):
        parliament_seats.append('Green')
    for i in range(independent_seats):
        parliament_seats.append('Independent')

    return parliament_seats