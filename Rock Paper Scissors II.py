#################################################################################
# Author(s): Silas Fair
# Username(s): fairs
#
# Assignment:FINAL PROJECT: rock paper scissors 2
##################################################################################
# Acknowledgements:
#
#
##################################################################################
import random
import turtle


class Weapons:

    hand_shapes = ["rock.gif", "paper.gif", "scissors.gif", "lizard.gif", "spock.gif"]
    weapon = ["rock", "paper", "scissors", "lizard", "spock"]


class Player:
    weapon = 0


class Computer:
    weapon = 0


def player_choose_hand_sign(wn):
    # Get key presses
    wn.onkeypress(h1, "1")
    wn.onkeypress(h2, "2")
    wn.onkeypress(h3, "3")
    wn.onkeypress(h4, "4")
    wn.onkeypress(h5, "5")

    wn.listen()


def h1():
    global player_hand
    Player.weapon = 0
    player_hand.shape(Weapons.hand_shapes[Player.weapon])


def h2():
    global player_hand
    Player.weapon = 1
    player_hand.shape(Weapons.hand_shapes[Player.weapon])



def h3():
    global player_hand
    Player.weapon = 2
    player_hand.shape(Weapons.hand_shapes[Player.weapon])


def h4():
    global player_hand
    Player.weapon = 3
    player_hand.shape(Weapons.hand_shapes[Player.weapon])


def h5():
    global player_hand
    Player.weapon = 4
    player_hand.shape(Weapons.hand_shapes[Player.weapon])

def get_winner(user, computer):
    global player_history
    player_history += Weapons.weapon[user]

    u = Weapons.weapon[user]
    c = Weapons.weapon[computer]


def main():
    global player_history
    global player_hand
    global player_weapon
    player_history = []
    player_weapon = 0
    player_hand = turtle.Turtle()  # Create a turtle to draw the player's hand
    player_hand.penup()
    wn = turtle.Screen()  # Get a reference to the window
    wn.setup(800, 600)  # Determine the window size
    wn.title("Rock Paper Scissors II")  # Change the window title
    wn.bgcolor("lightgreen")  # Set the background color
    player_choose_hand_sign(wn)
    for i in range(len(Weapons.hand_shapes)):  # import images
        wn.addshape(Weapons.hand_shapes[i])
    get_winner(Player.weapon, Computer.weapon)
    player_hand.setposition(-80,-20)
    player_hand.penup()
    wn.mainloop()

if __name__ == "__main__":
    main()
