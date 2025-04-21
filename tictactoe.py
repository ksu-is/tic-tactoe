Print("Welcome to Tic Tac Toe!")
def tic_tac_toe():
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    p1_wins = 0
    p2_wins = 0
    
    def table():
        print("        |       |     ")
        print("   " + str([1]) + "  |  " + str(a[2]) + "  |  " + str(a[3]))
        print("________|_______|_______")
        print("        |       |     ")
        print("   " + str(a[4]) + "  |  " + str(a[5]) + "  |  " + str(a[6]))
        print("________|_______|_______")
        print("        |       |     ")
        print("   " + str(a[7]) + "  |  " + str(a[8]) + "  |  " + str(a[9]))
        print("        |       |     ")

    def place_mark(player, mark):
        while True:
            player_turn = 1
            position = input("player choose square (1-9): ")
            if position.isdigit() and int(position) in range(1, 10) and str(a[int(position)]) == position:
                a[int(position)] = mark
                break
            else:
                print("Invalid Entry, try again!")
        table()
    def check_winner():
        combos = [
            (1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
        for x, y, z in combos:
            if a[x] == a[y] == a[z]:
                return True
        return False

    print("Starting a new round...\n")
    table()
    """while True:
        p1 = input("player 1 choose: X or 0: ")
        p2 = input("player 2 choose: X or 0: ")
        if p1 == p2:
            print("INVALID ENTRY, both players chose the same option")
        elif p1.lower() == "X" and p2 == "0" or p1.lower() == "0" and p2.lower() == "X":
            break
        else:
            print("INVALID ENTRY, Choose 1 or 2")"""

    player1_mark = "X" if p1 == "1" else "O"
    player2_mark = "O" if player1_mark == "X" else "X"
    player1_mark = "X"
    player2_mark = "O"
    turn = 1

    while True:
        if turn % 2 != 0:
            place_mark("Player 1", player1_mark)
            if check_winner():
                print("PLAYER 1 WINS!!")
                break
        else:
            place_mark("Player 2", player2_mark)
            if check_winner():
                print("PLAYER 2 WINS!!")
                break
        if all(str(cell) not in "123456789" for cell in a[1:]):
            print("It's a DRAW?")
        turn += 1

    restart = input("Do you want to play again, choose Yes or No: ")
    if restart.lower() == "Yes":
        tic_tac_toe()
    elif restart == "no" or restart == "No":
        print("Thanks for playing!")
    else:
        restart = input("INVALID ENTRY, choose Yes or No: ")
        if restart == "yes" or restart == "Yes":
            tic_tac_toe()
        elif restart == "no" or restart == "No":
            print("Thanks for playing!")


tic_tac_toe()