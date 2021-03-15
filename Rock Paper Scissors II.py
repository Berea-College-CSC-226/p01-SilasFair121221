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
    player_images = ["gifs/rock.gif", "gifs/paper.gif", "gifs/scissors.gif", "gifs/lizard.gif", "gifs/spock.gif"]
    computer_images = ["gifs/computer_rock.gif", "gifs/computer_paper.gif", "gifs/computer_scissors.gif",
                       "gifs/computer_lizard.gif", "gifs/computer_spock.gif"]
    weapon = ["rock", "paper", "scissors", "lizard", "spock"]


class Player:
    wins = 0
    history = []
    weapon = Weapons.weapon[0]
    wn = turtle.Screen()  # create the window
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.turtle.penup()
        self.turtle.setpos(-50, -90)
        self.weapon = 0
        self.wn.setup(800, 600)  # Determine the window size
        self.wn.title("Rock Paper Scissors II")  # Change the window title
        self.wn.bgcolor("lightgreen")  # Set the background color

        self.choose_hand_sign()
        for i in range(len(Weapons.player_images)):  # import images
            self.wn.addshape(Weapons.player_images[i])
        self.turtle.shape("gifs/rock.gif")
        self.wn.mainloop()


    def choose_hand_sign(self,wn):
        pass

    def choose_hand_sign(self):
        # Get key presses
        self.wn.onkeypress(self.h1, "1")
        self.wn.onkeypress(self.h2, "2")
        self.wn.onkeypress(self.h3, "3")
        self.wn.onkeypress(self.h4, "4")
        self.wn.onkeypress(self.h5, "5")
        self.wn.onkeypress(self.h6, "space")

        self.wn.listen()

    def h1(self):
        weapon = Weapons.weapon[0]
        self.turtle.shape(Weapons.player_images[0])

    def h2(self):
        weapon = Weapons.weapon[1]
        self.turtle.shape(Weapons.player_images[1])

    def h3(self):
        weapon = Weapons.weapon[2]
        self.turtle.shape(Weapons.player_images[2])

    def h4(self):
        weapon = Weapons.weapon[3]
        self.turtle.shape(Weapons.player_images[3])

    def h5(self):
        weapon = Weapons.weapon[4]
        self.turtle.shape(Weapons.player_images[4])
    def h6(self):
        get_winner()

class Computer:
    wins = 0
    history = [] # the history of choices the computer has made
    weapon = 0

    def __init__(self):
        self.turtle = turtle.Turtle()
        #self.turtle.penup()
        self.turtle.setpos(50, -90)
        self.weapon = 0

        Computer.weapon = self.choose_hand_sign()
        for i in range(len(Weapons.computer_images)):  # import images
            self.wn.addshape(Weapons.computer_images[i])
        self.turtle.shape(Weapons.computer_images[0])
        self.wn.mainloop()
    def choose_hand_sign(self):
        self.weapon_index = 0
        self.weapon = "rock"
        if "rock" in Player.history:
            self.weapon = "paper"
        self.turtle.shape(Weapons.computer_images[self.weapon_indexweapon])     # set the image for the computer hand
        return self.weapon







def get_winner(user, computer):
    Player.history += Weapons.weapon[user]

    Weapons.weapon[user]
    Weapons.weapon[computer]
    if user == "scissors" and computer == "paper":
        return "winner"
    elif user == "paper" and computer == "spock":
        return "winner"
    elif user == "paper" and computer == "rock":
        return "winner"
    elif user == "lizard" and computer == "spock":
        return "winner"
    elif user == "spock" and computer == "scissors":
        return "winner"
    elif user == "scissors" and computer == "lizard":
        return "winner"
    elif user == "lizard" and computer == "paper":
        return "winner"
    elif user == "spock" and computer == "rock":
        return "winner"
    elif user == "rock" and computer == "scissors":
        return "winner"
    elif user == "egg":     # EASTER EGG
        return "egg"
    elif user == computer:  # if the user and computer choose the same thing declare a TIE!
        return "tie"
    else:   # if the computer wins return loser
        return "loser"



def main():
    global rounds_played
    Player()
    Computer()
    rounds_played = 0
    get_winner(Player.weapon, Computer.weapon)



if __name__ == "__main__":
    main()
