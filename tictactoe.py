def tic_tac_toe():
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def table():
        print("        |       |     ")
        print("   ", a[1], "  |  ", a[2], "  |  ", a[3])
        print("________|_______|_______")
        print("        |       |     ")
        print("   ", a[4], "  |  ", a[5], "  |  ", a[6])
        print("________|_______|_______")
        print("        |       |     ")
        print("   ", a[7], "  |  ", a[8], "  |  ", a[9])
        print("        |       |     ")

    def place_mark(player, mark):
        while True:
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
    table()
    while True:
        p1 = input("player 1 choose: 1 for X or 2 for 0: ")
        p2 = input("player 2 choose: 1 for X or 2 for 0: ")
        if p1 == p2:
            print("INVALID ENTRY, both players chose the same option")
        elif p1 == "1" and p2 == "2" or p1 == "2" and p2 == "1":
            break
        else:
            print("INVALID ENTRY, Choose 1 or 2")

    player1_mark = "X" if p1 == "1" else "0"
    player2_mark = "O" if player1_mark == "X" else "X"
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
    if restart == "yes" or restart == "Yes":
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
#random
