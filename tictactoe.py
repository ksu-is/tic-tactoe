import tkinter as tk
from tkinter import messagebox

class TicTacToe(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.grid()
        self.board = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.turn = 1
        self.mark = {1: "X", 0: "O"}
        self.create_widgets()

    def create_widgets(self):
        self.status = tk.Label(self, text="Player X's Turn", font=("Arial", 16))
        self.status.grid(row=0, column=0, columnspan=3, pady=10)

        self.one_btn = tk.Button(self, text="", width=9, height=4, font=("Arial", 24), command=lambda: self.play(1))
        self.one_btn.grid(row=1, column=0, padx=5, pady=5)

        self.two_btn = tk.Button(self, text="", width=9, height=4, font=("Arial", 24),  command=lambda: self.play(2))
        self.two_btn.grid(row=1, column=1, padx=5, pady=5)

        self.three_btn = tk.Button(self, text="", width=9, height=4, font=("Arial", 24),  command=lambda: self.play(3))
        self.three_btn.grid(row=1, column=2, padx=5, pady=5)

        self.four_btn = tk.Button(self, text="", width=9, height=4, font=("Arial", 24),command=lambda: self.play(4))
        self.four_btn.grid(row=2, column=0, padx=5, pady=5)

        self.five_btn = tk.Button(self, text="", width=9, height=4, font=("Arial", 24), command=lambda: self.play(5))
        self.five_btn.grid(row=2, column=1, padx=5, pady=5)

        self.six_btn = tk.Button(self, text="", width=9, height=4, font=("Arial", 24), command=lambda: self.play(6))
        self.six_btn.grid(row=2, column=2, padx=5, pady=5)

        self.seven_btn = tk.Button(self, text="", width=9, height=4, font=("Arial", 24), command=lambda: self.play(7))
        self.seven_btn.grid(row=3, column=0, padx=5, pady=5)

        self.eight_btn = tk.Button(self, text="", width=9, height=4, font=("Arial", 24), command=lambda: self.play(8))
        self.eight_btn.grid(row=3, column=1, padx=5, pady=5)

        self.nine_btn = tk.Button(self, text="", width=9, height=4, font=("Arial", 24),command=lambda: self.play(9))
        self.nine_btn.grid(row=3, column=2, padx=5, pady=5)

        self.buttons = {
            1: self.one_btn, 2: self.two_btn, 3: self.three_btn,
            4: self.four_btn, 5: self.five_btn, 6: self.six_btn,
            7: self.seven_btn, 8: self.eight_btn, 9: self.nine_btn
        }

        self.reset_btn = tk.Button(self, text="Restart", width=28, height=2, font=("Arial", 14), command=self.reset)
        self.reset_btn.grid(row=4, column=0, columnspan=3, pady=10)

    def play(self, pos):
        if str(self.board[pos]) == str(pos):
            self.board[pos] = self.mark[self.turn % 2]
            self.buttons[pos].config(text=self.board[pos], state="disabled")
            if self.check_winner():
                self.status.config(text=f"Player {self.board[pos]} Wins!")
                messagebox.showinfo("Game Over", f"Player {self.board[pos]} Wins!")
                self.disable_all()
            elif all(isinstance(x, str) for x in self.board[1:]):
                self.status.config(text="It's a draw!")
                messagebox.showinfo("Game Over", "It's a draw!")
                self.disable_all()
            else:
                self.turn += 1
                self.status.config(text=f"Player {self.mark[self.turn % 2]}'s Turn")

    def check_winner(self):
        wins = [
            (1, 2, 3), (4, 5, 6), (7, 8, 9),
            (1, 4, 7), (2, 5, 8), (3, 6, 9),
            (1, 5, 9), (3, 5, 7)
        ]
        for x, y, z in wins:
            if self.board[x] == self.board[y] == self.board[z]:
                return True
        return False

    def disable_all(self):
        for btn in self.buttons.values():
            btn.config(state="disabled")

    def reset(self):
        self.board = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.turn = 1
        for i in range(1, 10):
            self.buttons[i].config(text="", state="normal")
        self.status.config(text="Player X's Turn")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x400")
    root.title("Tic Tac Toe")
    app = TicTacToe(root)
    root.mainloop()
"""this is our code we used to make the outline for the game:
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
"""
"""
def tic_tac_toe():
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def table():
        print("\n     |     |     ")
        print(f"  {a[1]}  |  {a[2]}  |  {a[3]}")
        print("_____|_____|_____")
        print("     |     |     ")
        print(f"  {a[4]}  |  {a[5]}  |  {a[6]}")
        print("_____|_____|_____")
        print("     |     |     ")
        print(f"  {a[7]}  |  {a[8]}  |  {a[9]}")
        print("     |     |     \n")

    def X1():
        b = input("Player 1 Choose Square: ")
        if b in map(str, range(1, 10)):
            a[int(b)] = "X"
        else:
            print("INVALID ENTRY, enter number: ")
        table()

    def X2():
        b = input("Player 2 Choose Square: ")
        if b in map(str, range(1, 10)):
            a[int(b)] = "X"
        else:
            print("INVALID ENTRY, enter number: ")
        table()

    def O1():
        b = input("Player 1 Choose Square: ")
        if b in map(str, range(1, 10)):
            a[int(b)] = "O"
        else:
            print("INVALID ENTRY, enter number: ")
        table()

    def O2():
        b = input("Player 2 Choose Square: ")
        if b in map(str, range(1, 10)):
            a[int(b)] = "O"
        else:
            print("INVALID ENTRY, enter number: ")
        table()

    table()
    while True:
        p1 = input("Player 1 choose: 1 for X or 2 for O: ")
        p2 = input("Player 2 choose: 1 for X or 2 for O: ")
        if p1 == p2:
            print("INVALID ENTRY, both players chose the same option")
        elif (p1, p2) in [("1", "2"), ("2", "1")]:
            break
        else:
            print("INVALID ENTRY, Choose 1 or 2")

    def mark1(p1):
        while True:
            if p1 == "1":
                X1()
            elif p1 == "2":
                O1()
            if (a[1] == a[2] == a[3]) or (a[4] == a[5] == a[6]) or (a[7] == a[8] == a[9]) or \
               (a[1] == a[4] == a[7]) or (a[2] == a[5] == a[8]) or (a[3] == a[6] == a[9]) or \
               (a[1] == a[5] == a[9]) or (a[3] == a[5] == a[7]):
                print("PLAYER 1 WIN'S!!")
                break

    def mark2(p2):
        while True:
            if p2 == "1":
                X2()
            elif p2 == "2":
                O2()
            if (a[1] == a[2] == a[3]) or (a[4] == a[5] == a[6]) or (a[7] == a[8] == a[9]) or \
               (a[1] == a[4] == a[7]) or (a[2] == a[5] == a[8]) or (a[3] == a[6] == a[9]) or \
               (a[1] == a[5] == a[9]) or (a[3] == a[5] == a[7]):
                print("PLAYER 2 WIN'S!!")
                break

    mark1(p1)
    mark2(p2)

    restart = input("Do you want to play again, choose Yes or No: ")
    if restart.lower() == "yes":
        tic_tac_toe()
    elif restart.lower() == "no":
        print("Thanks for playing!")
    else:
        restart = input("INVALID ENTRY, choose Yes or No: ")
        if restart.lower() == "yes":
            tic_tac_toe()
        elif restart.lower() == "no":
            print("Thanks for playing!")

# Start the game
tic_tac_toe()
"""