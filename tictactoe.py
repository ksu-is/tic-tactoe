import tkinter as tk
from tkinter import messagebox

class TicTacToe(tk.Frame):
    """
    A simple Tic Tac Toe app developed using the Tkinter GUI.
    Matches layout and structure of calculator app.
    """

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.grid()
        self.board = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.turn = 1
        self.mark = {1: "X", 0: "O"}
        self.create_widgets()

    def create_widgets(self):
        self.status = tk.Label(self, text="Player X's Turn", font=("Arial", 16), fg="white", bg="black")
        self.status.grid(row=0, column=0, columnspan=3, pady=10)

        self.one_btn = tk.Button(self, text="", width=9, height=4, font=("Arial", 24), fg="black", bg="white", command=lambda: self.play(1))
        self.one_btn.grid(row=1, column=0, padx=5, pady=5)

        self.two_btn = tk.Button(self, text="", width=9, height=4, font=("Arial", 24), fg="black", bg="white", command=lambda: self.play(2))
        self.two_btn.grid(row=1, column=1, padx=5, pady=5)

        self.three_btn = tk.Button(self, text="", width=9, height=4, font=("Arial", 24), fg="black", bg="white", command=lambda: self.play(3))
        self.three_btn.grid(row=1, column=2, padx=5, pady=5)

        self.four_btn = tk.Button(self, text="", width=9, height=4, font=("Arial", 24), fg="black", bg="white", command=lambda: self.play(4))
        self.four_btn.grid(row=2, column=0, padx=5, pady=5)

        self.five_btn = tk.Button(self, text="", width=9, height=4, font=("Arial", 24), fg="black", bg="white", command=lambda: self.play(5))
        self.five_btn.grid(row=2, column=1, padx=5, pady=5)

        self.six_btn = tk.Button(self, text="", width=9, height=4, font=("Arial", 24), fg="black", bg="white", command=lambda: self.play(6))
        self.six_btn.grid(row=2, column=2, padx=5, pady=5)

        self.seven_btn = tk.Button(self, text="", width=9, height=4, font=("Arial", 24), fg="black", bg="white", command=lambda: self.play(7))
        self.seven_btn.grid(row=3, column=0, padx=5, pady=5)

        self.eight_btn = tk.Button(self, text="", width=9, height=4, font=("Arial", 24), fg="black", bg="white", command=lambda: self.play(8))
        self.eight_btn.grid(row=3, column=1, padx=5, pady=5)

        self.nine_btn = tk.Button(self, text="", width=9, height=4, font=("Arial", 24), fg="black", bg="white", command=lambda: self.play(9))
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
    root.configure(bg="black")
    root.geometry("300x400")
    root.title("Tic Tac Toe")
    app = TicTacToe(root)
    root.mainloop()
