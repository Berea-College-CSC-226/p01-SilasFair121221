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


class Stats:
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.turtle.penup()
        self.turtle.setpos(-100, -120)


class Weapons:
    player_images = ["gifs/rock.gif", "gifs/paper.gif", "gifs/scissors.gif", "gifs/lizard.gif", "gifs/spock.gif"]
    computer_images = ["gifs/computer_rock.gif", "gifs/computer_paper.gif", "gifs/computer_scissors.gif",
                       "gifs/computer_lizard.gif", "gifs/computer_spock.gif"]
    weapon = ["rock", "paper", "scissors", "lizard", "spock"]


class Player:
    wn = turtle.Screen()  # create the window
    weapon = Weapons.weapon[0]
    wins = 0  # stats
    history = []  # history of moves the player has made
    def __init__(self):
        self.wn.setup(800, 600)  # Determine the window size
        self.wn.title("Rock Paper Scissors II")  # Change the window title
        self.wn.bgcolor("lightgreen")  # Set the background color
        self.wn.bgpic("gifs/final_project_background.gif")
        self.turtle = turtle.Turtle() #set up turtle
        self.turtle.penup()
        self.turtle.setpos(-100, -120)

        self.choose_hand_sign()
        for i in range(len(Weapons.player_images)):  # import images
            self.wn.addshape(Weapons.player_images[i])
        self.turtle.shape("gifs/rock.gif")



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
        self.weapon = Weapons.weapon[0]
        self.turtle.shape(Weapons.player_images[0])

    def h2(self):
        self.weapon = Weapons.weapon[1]
        self.turtle.shape(Weapons.player_images[1])

    def h3(self):
        self.weapon = Weapons.weapon[2]
        self.turtle.shape(Weapons.player_images[2])

    def h4(self):
        self.weapon = Weapons.weapon[3]
        self.turtle.shape(Weapons.player_images[3])

    def h5(self):
        self.weapon = Weapons.weapon[4]
        self.turtle.shape(Weapons.player_images[4])
    def h6(self):
        print(get_winner(self.weapon, Computer.weapon))
        print(self.weapon)
        print(Computer.weapon)

class Computer:
    wins = 0
    history = []
    weapon = Weapons.weapon[0]
    wn = Player.wn  # create the window
    def __init__(self):
        self.c_turtle = turtle.Turtle()
        self.c_turtle.penup()
        self.c_turtle.setpos(50, -100)
        self.weapon = 0
        for i in range(len(Weapons.computer_images)):  # import images
            self.wn.addshape(Weapons.computer_images[i])
        self.c_turtle.shape("gifs/computer_rock.gif")
        self.c_turtle.resizemode("auto")







def get_winner(user, computer):
    Player.history += user

    #Weapons.weapon[user]
    #Weapons.weapon[computer]
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
    Computer()
    Player()
    Player.wn.mainloop()




    rounds_played = 0
    get_winner(Player.weapon, Computer.weapon)



if __name__ == "__main__":
    main()
