# Author: Tony Rahman | trseattle@outlook.com | www.flyingsalmon.net | October 2023 | Version: 1.0.1
# Permissions: Non-commercial use only. Modifications allowed if modified code is made available to public domain with no additional restrictions.
# Attribution: Original author: Tony Rahman | trseattle@outlook.com | www.flyingsalmon.net | Edited by: <author_name><date>

''' Rules:
A BINGO (American version) card is a 5x5 grid where each column has 5 rows and column B will have the random digits 1 to 15,
column I will have digits 16-30, N will have 31-45 , G will have 46-60, and column O will have 61-75;
and no column should have the same number repeated, and the center cell (cell N3) will be marked 'X'.

Game over conditions: Win (Bingo is hit), or all 75 balls drawn.

Win conditions: Game is win (bingo!) when a pattern is filled with any of these patterns:
 horizontal lines (any row with 5 matches side by side including Free cell)
 vertical lines (any column with 5 matches up and down including Free cell)
 diagonal lines (top-left to bottom-right; or top-right to bottom-left: 5 cells matched including Free cell)

'''

import random

B_range = range(1, 16)
I_range = range(16, 31)
N_range = range(31, 46)
G_range = range(46, 61)
O_range = range(61, 76)

def generate_number(range, used):
    '''
    Generates one number at a time for the card, and updates the passed parameter 'used' range which updates the numbers already drawn/used for a specific column.
    Called by: generate_card()
    Calls: none
    parameters: range (range object. One for each column per call), used (range object containing numbers already used for the column).
    returns: number (integer)

    '''    

    while True:

        number = random.choice(range)

        if number not in used:

            used.add(number) 

            return number

def generate_card():
    '''
    Generates all 25 numbers in a 5x5 card for all columns per call. Poplulates local 'row' list to get valid numbers in  a column within its range.
    Updates card[] list with the final numbers.
    Called by: main.
    Calls: generate_number()
    returns: card (list object)

    '''

    card = []

    used_B = set()
    used_I = set()
    used_N = set()
    used_G = set()
    used_O = set()

    for i in range(5):

        row = []

        row.append(generate_number(B_range, used_B))

        row.append(generate_number(I_range, used_I))

        if i == 2: 
            row.append("X") 
        else:
            row.append(generate_number(N_range, used_N))

        row.append(generate_number(G_range, used_G))

        row.append(generate_number(O_range, used_O))

        card.append(row)

    return card

def print_card(card):
    '''
    prints on display the generate card in a grid with column headers.
    Called by: main
    Calls: none
    parameters: card (list object. Holds all generated numbers for a card.)
    returns: nothing

    '''        

    print("B\tI\tN\tG\tO")
    print('-' * 35) 

    for row in card:

        print("\t".join(map(str, row)))

def draw_ball(pool):

    if not pool:
        return None

    ball = random.choice(pool)

    pool.remove(ball)

    return ball

def check_match(card, ball):

    for i in range(5):

        for j in range(5):
            if card[i][j] == ball: 
                card[i][j] = "X" 

                return True

    return False

def check_bingo(card):

    for i in range(5):

        row_count = 0

        for j in range(5):

            if card[i][j] == "X":

                row_count += 1

        if row_count == 5:

            return True, "Horizontal line." 

    for j in range(5):

        col_count = 0

        for i in range(5):

            if card[i][j] == "X":

                col_count += 1

        if col_count == 5:

            return True, "Vertical line." 

    diag1_count = 0

    for i in range(5):

        if card[i][i] == "X":

            diag1_count += 1

    if diag1_count == 5:

        return True, "Diagonal (primary)." 

    diag2_count = 0

    for i in range(5):

        if card[i][4-i] == "X":

            diag2_count += 1

    if diag2_count == 5:

        return True, "Diagonal (secondary)." 

    return False, ""

def play_bingo(card, pool):
    print("Welcome to Bingo!")    
    print("Here is your card:")

    print_card(card)

    print("Let's begin!")

    while True:

        input("* Press enter to draw a ball.")

        ball = draw_ball(pool)

        if ball is None:
            print("*** No more balls left. Game over.")
            break

        print(f"==> Ball drawn is: {ball}.")

        match = check_match(card, ball)

        if match:
            print("** You have a match!")

            print("Here is your updated card:")

            print_card(card)

            bingo, pattern = check_bingo(card)

            if bingo:
                print("*** BINGO! You win! *** ", end=' ') 
                print("Pattern:", pattern) 
                break

        else:
            print("* No match.")

card = generate_card()
pool = list(range(1,76)) 

play_bingo(card, pool)

###

