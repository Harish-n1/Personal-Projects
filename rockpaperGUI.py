import random
from tkinter import *

choices = ['Rock','Paper','Scissors']
def play():
    global choices
    computer=random.randrange(0,2,1)

    if x.get() == computer:
        #print('player: ',x.get())
        #print("computer:",computer)
        print("Tie!\n")

    elif x.get() == 0:
        if computer == 1:
            print("you: Rock")
            print("Jarvis: Paper")
            print("You lost! :( \n")
        if computer == 2:
            print("you: Rock")
            print("Jarvis: Scissors")
            print("you win! :) \n")

    elif x.get() == 1:
        if computer == 0:
            print("you: Paper")
            print("Jarvis: Rock")
            print("You win :) \n")
        if computer ==  2:
            print("you: Paper")
            print("Jarvis: Scissors")
            print("You lost! :( \n")

    elif x.get() == 2:
        if computer == 0:
            print("you: Scissors")
            print("Jarvis: Rock")
            print("You lost! :( \n")
        if computer ==1:
            print("you: Scissors")
            print("Jarvis: Paper")
            print("You win! :) \n")

window = Tk()
computer=random.choice(choices)
rockimage=PhotoImage(file="C:\\Users\\Asus\\Pictures\\Saved Pictures\\rock.png")
paperimage=PhotoImage(file="C:\\Users\\Asus\\Pictures\\Saved Pictures\\paper.png")
scissorsimage=PhotoImage(file="C:\\Users\\Asus\\Pictures\\Saved Pictures\\scissors.png")
choicesimage=[rockimage,paperimage,scissorsimage]

x=IntVar()

for index in range(len(choices)):
       radiobutton = Radiobutton(window,
                                 text=choices[index],
                                 variable=x,
                                 value=index,
                                 indicatoron=0,
                                 image=choicesimage[index],
                                 command=play,
                                 compound="left",
                                 font=('arial',25),
                                 width=220,
                                 fg="green",
                                 bg="black")
       radiobutton.pack(anchor=W)

window.mainloop()