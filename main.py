import random
from tkinter import *
a = Tk()
def dice_roll():
    diceroll = random.randint(1,6)
    return diceroll
rounds=1
while rounds!=10:
    player1 = dice_roll()
    player2=dice_roll
    label_1=Label(a,text="Score of player 1" +str(dice_roll()))
    label_1.pack()
    label_2 = Label(a, text="Score of player 2" + str(dice_roll()))
    label_2.pack()
    if player1==player2:
        label_3=Label(a,text="It's a tie")
    label_3.pack()
    elif player2>player2:
    x=Label(a,text="Player 1 won")
    x.pack
    else
    x=Label(a,text="Player2 won")
    x.pack
rounds=rounds+ 1