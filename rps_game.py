import random
import tkinter as tk

window = tk.Tk()
window.title('Rock Paper Scissors')
window.geometry('300x200')

results_text = tk.StringVar(window)


def tie_game():
    results_text.set('Tie :/')

def player_wins():
    results_text.set('You win :)')

def computer_wins():
    results_text.set('Computer wins :(')

def unknown_action():
    results_text.set('YOU BROKE THE GAME')


def play_game(user, computer):
    if user == computer:
        tie_game()
    elif user == 'rock':
        if computer == 'scissors':
            player_wins()
        elif computer == 'paper':
            computer_wins()
        else:
            unknown_action()
    elif user == 'paper':
        if computer == 'rock':
            player_wins()
        elif computer == 'scissors':
            computer_wins()
        else:
            unknown_action()
    elif user == 'scissors':
        if computer == 'paper':
            player_wins()
        elif computer == 'rock':
            computer_wins()
        else:
            unknown_action()

def computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])


def i_choose_rock():
    play_game('rock', computer_choice())

def i_choose_paper():
    play_game('paper', computer_choice())

def i_choose_scissors():
    play_game('scissors', computer_choice())


root = tk.Label(window)
root.pack(padx=10, pady=10)

# Setup the button choices
btnRock = tk.Button(root, text='Rock', command=i_choose_rock)
btnRock.pack(side='top', fill='both', expand='yes', padx='5', pady='5')

btnPaper = tk.Button(root, text='Paper', command=i_choose_paper)
btnPaper.pack(side='top', fill='both', expand='yes', padx='5', pady='5')

btnScissors = tk.Button(root, text='Scissors', command=i_choose_scissors)
btnScissors.pack(side='top', fill='both', expand='yes', padx='5', pady='5')

resultLabel = tk.Label(root, textvariable=results_text)
resultLabel.pack(side='top', fill='both', expand='yes', padx='5', pady='5')

window.mainloop()
