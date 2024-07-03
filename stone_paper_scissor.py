import customtkinter
import random

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
global players
players = {}


class Player:
    def __init__(self):
        self.player_no = 0
        self.ctk = customtkinter.CTk()
        self.ctk.iconbitmap("./rock-paper-scissors_icon.ico")
        self.button1 = self.button2 = self.button3 = None

    def choice1(self):
        players[f'Player {self.player_no}'] = self.button1._text
        self.ctk.destroy()

    def choice2(self):
        players[f'Player {self.player_no}'] = self.button2._text
        self.ctk.destroy()

    def choice3(self):
        players[f'Player {self.player_no}'] = self.button3._text
        self.ctk.destroy()

    def player(self, no):
        self.player_no = no
        self.ctk.title(f"Player {self.player_no} choice")
        width = 250
        height = 100
        screen_width = self.ctk.winfo_screenwidth()
        screen_height = self.ctk.winfo_screenheight()
        x_coordinate = (screen_width / 2) - (width / 2)
        y_coordinate = (screen_height / 2) - (height / 2)
        self.ctk.geometry("%dx%d+%d+%d" % (width, height, x_coordinate, y_coordinate))

        frame = customtkinter.CTkFrame(self.ctk, corner_radius=15, border_width=5, width=width, height=height)
        frame.pack(padx=10, pady=20)
        frame.rowconfigure((0, 1, 2), weight=1)
        frame.columnconfigure((0, 1, 2), weight=0)

        self.button1 = customtkinter.CTkButton(frame, text='Rock', corner_radius=10, width=5, command=self.choice1)
        self.button1.grid(column=0, row=1, sticky="nsew", padx=10, pady=15)

        self.button2 = customtkinter.CTkButton(frame, text='Paper', corner_radius=10, width=5, command=self.choice2)
        self.button2.grid(column=1, row=1, sticky="nsew", padx=10, pady=15)

        self.button3 = customtkinter.CTkButton(frame, text='Scissor', corner_radius=10, width=5, command=self.choice3)
        self.button3.grid(column=2, row=1, sticky='nsew', padx=10, pady=15)

        self.ctk.mainloop()


class Winner:
    def __init__(self):
        self.ctk = customtkinter.CTk()
        self.ctk.iconbitmap("./rock-paper-scissors_icon.ico")

    def close(self):
        self.ctk.destroy()
        exit(0)

    def show_winner(self, result):
        self.ctk.title(f"Result")
        width = 300
        height = 150
        screen_width = self.ctk.winfo_screenwidth()
        screen_height = self.ctk.winfo_screenheight()
        x_coordinate = (screen_width / 2) - (width / 2)
        y_coordinate = (screen_height / 2) - (height / 2)
        self.ctk.geometry("%dx%d+%d+%d" % (width, height, x_coordinate, y_coordinate))

        frame = customtkinter.CTkFrame(self.ctk, corner_radius=15, border_width=5, width=width, height=height)
        frame.pack(padx=10, pady=20)
        frame.rowconfigure((0, 1, 2), weight=0)
        frame.columnconfigure((0,), weight=0)

        label = customtkinter.CTkLabel(frame, text=result)
        label.grid(column=1, row=1, sticky="nsew", padx=15, pady=15)

        exit_button = customtkinter.CTkButton(self.ctk, text='OK', width=20, corner_radius=15, command=self.close)
        exit_button.pack(padx=10, pady=10)

        self.ctk.mainloop()


class Main:
    def __init__(self):
        self.ctk = customtkinter.CTk()
        self.ctk.iconbitmap("./rock-paper-scissors_icon.ico")

    def com_vs(self):
        result = ''
        self.ctk.destroy()
        Player().player("")
        players[f'Computer'] = random.choice(['Rock', 'Paper', 'Scissor'])

        if players[f'Computer'] == players[f'Player ']:
            result = 'Its a Draw !'
        elif players[f'Computer'] == 'Rock' and players[f'Player '] == 'Scissor' or players[f'Computer'] == 'Paper' and players[f'Player '] == 'Rock' or players[f'Computer'] == 'Scissor' and players[f'Player '] == 'Paper':
            result = f'Computer Won ! \n(having {players[f'Computer']})'
        else:
            result = f'You Won! \n(Computer have {players[f'Computer']})'
        Winner().show_winner(result)

    def two_plyr(self):
        result = ''
        self.ctk.destroy()
        Player().player(1)
        Player().player(2)

        if players[f'Player 1'] == players[f'Player 2']:
            result = 'Its a Draw !'
        elif players[f'Player 1'] == 'Rock' and players[f'Player 2'] == 'Scissor' or players[f'Player 1'] == 'Paper' and players[f'Player 2'] == 'Rock' or players[f'Player 1'] == 'Scissor' and players[f'Player 2'] == 'Paper':
            result = f'Player 1 Won ! \n(having {players[f'Player 1']})'
        else:
            result = f'Player 2 Won! \n(having {players[f'Player 2']})'
        Winner().show_winner(result)

    def main(self):
        self.ctk.title(f"Stone Paper Scissor Game")
        width = 400
        height = 200
        screen_width = self.ctk.winfo_screenwidth()
        screen_height = self.ctk.winfo_screenheight()
        x_coordinate = (screen_width / 2) - (width / 2)
        y_coordinate = (screen_height / 2) - (height / 2)
        self.ctk.geometry("%dx%d+%d+%d" % (width, height, x_coordinate, y_coordinate))

        frame = customtkinter.CTkFrame(self.ctk, corner_radius=15, border_width=5, width=width, height=height)
        frame.pack(padx=10, pady=40)
        frame.rowconfigure((0, 1, 2), weight=1)
        frame.columnconfigure((0, 1, 2), weight=0)

        button1 = customtkinter.CTkButton(frame, text="Player vs Computer", corner_radius=10, border_width=2, command=self.com_vs)
        button1.grid(row=1, column=1, sticky="nsew", padx=15, pady=15)

        button2 = customtkinter.CTkButton(frame, text="Player vs Player", corner_radius=10, border_width=2, command=self.two_plyr)
        button2.grid(row=2, column=1, sticky="nsew", padx=15, pady=15)

        self.ctk.mainloop()

Main().main()
