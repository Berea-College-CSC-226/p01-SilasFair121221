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

class Wn:
    wn = turtle.Screen()  # create the window
    wn.setup(800, 600)  # Determine the window size
    wn.title("Rock Paper Scissors II")  # Change the window title
    wn.bgcolor("lightgreen")  # Set the background color
    wn.bgpic("gifs/final_project_background.gif")

class State: # the state machine object
    choosing = True
    player_won = False
    computer_won = False

class Weapons:
    player_images = ["gifs/rock.gif", "gifs/paper.gif", "gifs/scissors.gif", "gifs/lizard.gif", "gifs/spock.gif"]
    computer_images = ["gifs/computer_rock.gif", "gifs/computer_paper.gif", "gifs/computer_scissors.gif",
                       "gifs/computer_lizard.gif", "gifs/computer_spock.gif"]
    weapon = ["rock", "paper", "scissors", "lizard", "spock"]


class Player:
    choosing = True
    wn = turtle.Screen()  # create the window
    weapon = Weapons.weapon[0]
    wins = 0  # stats
    history = []  # history of moves the player has made
    win_loss_history = []

    def __init__(self):
        """create a player object"""
        Wn.wn.setup(800, 600)  # Determine the window size
        Wn.wn.title("Rock Paper Scissors II")  # Change the window title
        Wn.wn.bgcolor("lightgreen")  # Set the background color
        Wn.wn.bgpic("gifs/final_project_background.gif")
        self.turtle = turtle.Turtle()   # set up turtle
        self.turtle.penup()
        self.turtle.setpos(-100, -120)
        self.choose_hand_sign()     # run the choose hand sign function
        for i in range(len(Weapons.player_images)):  # import images
            self.wn.addshape(Weapons.player_images[i])
        self.turtle.shape("gifs/rock.gif")

    def choose_hand_sign(self):
        Wn.wn.onkeypress(self.h1, "1")
        Wn.wn.onkeypress(self.h2, "2")
        Wn.wn.onkeypress(self.h3, "3")
        Wn.wn.onkeypress(self.h4, "4")
        Wn.wn.onkeypress(self.h5, "5")
        Wn.wn.onkeypress(self.h6, "space")
        Wn.wn.listen()

    # key handlers for the player
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

    def h6(self): # this keypress enters your choice or sets the state to the next round
        if self.choosing == True: # is the choosing is true it lets you enter your choice
            self.choosing = False
            # set make the hands move
            self.turtle.seth(270+50)
            Computer.turtle.seth(270-50)
            self.turtle.fd(60)
            Computer.turtle.fd(30)
            # Choose a hand for the computer
            choose_hand(Computer)
            print(Player.weapon + Computer.weapon)
            if get_winner(self.weapon, Computer.weapon) == "winner":
                Scorekeeper.turtle.shape(Scorekeeper.shapes[1])
            elif get_winner(self.weapon, Computer.weapon) == "tie":
                Scorekeeper.turtle.shape(Scorekeeper.shapes[2])
            else :
                Scorekeeper.turtle.shape(Scorekeeper.shapes[3])
        else:
            self.turtle.setpos(-100, -120)  # move player hand back
            Computer.turtle.setpos(70, -100)  # move computer hand back
            self.choosing = True
            Scorekeeper.turtle.shape(Scorekeeper.shapes[0])
            Computer.turtle.shape(Weapons.computer_images[0])
            self.turtle.shape(Weapons.player_images[0])
            self.weapon = Weapons.weapon[0]
            self.history.append(self.weapon)
            return

class Computer:
    wins = 0
    weapon = Weapons.weapon[0]
    wn = Wn.wn  # create the window
    turtle = turtle.Turtle()

    def __init__(self):
        self.turtle.penup()
        self.turtle.setpos(70, -100)
        for i in range(len(Weapons.computer_images)):  # import images
            self.wn.addshape(Weapons.computer_images[i])
        self.turtle.shape("gifs/computer_rock.gif")
        self.turtle.resizemode("auto")

def choose_hand(self):
    print(Player.history[:])
    w = random.randint(0, 4)
    self.weapon = Weapons.weapon[w]
    self.turtle.shape(Weapons.computer_images[w])

class Scorekeeper:
    shapes = ["gifs/score_man.gif","gifs/score_man_win.gif","gifs/score_man_tie.gif","gifs/score_man_lose.gif"]
    wn = Wn.wn
    shape = "gifs/score_man.gif"
    turtle = turtle.Turtle()  # create turtle for dapper fellow holding the win/loss/tie sign

    def __init__(self):
        """
        Create a dapper fellow who tells who won the round.
        """
        self.turtle.penup()
        self.turtle.setpos(180, 80)
        # add the possible images for the fine gentleman to Player.wn
        for i in range(len(self.shapes)):
            self.wn.addshape(self.shapes[i])
        self.turtle.shape(self.shape)



def get_winner(self, computer):
    user = self
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
        Scorekeeper.turtle.shape(Scorekeeper.shapes[1])
    elif user == computer:  # if the user and computer choose the same thing declare a TIE!
        return "tie"
        Scorekeeper.turtle.shape(Scorekeeper.shapes[2])
    else:   # if the computer wins return loser
        return "loser"
        Scorekeeper.turtle.shape(Scorekeeper.shapes[3])


def main():
    global rounds_played
    State()
    Computer()
    Scorekeeper()
    Player()
    get_winner(Player.weapon,Computer.weapon)
    Wn.wn.mainloop()
    rounds_played = 0




if __name__ == "__main__":
    main()
