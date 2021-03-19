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
import winsound



class Wn:
    wn = turtle.Screen()  # create the window
    wn.setup(800, 600)  # Determine the window size
    wn.title("Rock Paper Scissors II")  # Change the window title
    wn.bgcolor("lightgreen")  # Set the background color
    wn.bgpic("gifs/final_project_background.gif")


class Tutorial:
    # this text pops up on the screen and shows the user how to play
    # when the player presses a button it disappears
    turtle = turtle.Turtle()
    turtle.pencolor("white")
    turtle.penup()
    turtle.setpos(0,-290)
    turtle.write("Press 1, 2, 3, 4, or 5 to select your hand sign. \n           Press space to start the round", move=False, align="center", font=("Arial", 20, "normal"))
    turtle.hideturtle()


class Weapons:
    player_images = ["gifs/rock.gif", "gifs/paper.gif", "gifs/scissors.gif", "gifs/lizard.gif", "gifs/spock.gif"]
    computer_images = ["gifs/computer_rock.gif", "gifs/computer_paper.gif", "gifs/computer_scissors.gif",
                       "gifs/computer_lizard.gif", "gifs/computer_spock.gif"]
    weapon = ["rock", "paper", "scissors", "lizard", "spock"]


class Player:
    choosing = True
    wn = turtle.Screen()  # create the window
    weapon = Weapons.weapon[0]
    score = 0
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
        if self.choosing == True:
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
        Tutorial.turtle.clear()

    def h2(self):
        self.weapon = Weapons.weapon[1]
        self.turtle.shape(Weapons.player_images[1])
        Tutorial.turtle.clear()

    def h3(self):
        self.weapon = Weapons.weapon[2]
        self.turtle.shape(Weapons.player_images[2])
        Tutorial.turtle.clear()

    def h4(self):
        self.weapon = Weapons.weapon[3]
        self.turtle.shape(Weapons.player_images[3])
        Tutorial.turtle.clear()

    def h5(self):
        self.weapon = Weapons.weapon[4]
        self.turtle.shape(Weapons.player_images[4])
        Tutorial.turtle.clear()

    def h6(self): # this keypress enters your choice or sets the state to the next round
        if self.choosing == True: # is the choosing is true it lets you enter your choice
            self.choosing = False
            # set make the hands move
            self.turtle.setpos(-100+30, -120-40)  # move player hand back to start position
            Computer.turtle.setpos(70-30, -100-40)  # move computer hand back to start position

            self.turtle.setpos(-100, -120)  # move player hand back to start position
            Computer.turtle.setpos(70, -100)  # move computer hand back to start position

            self.turtle.setpos(-100+30, -120-40)  # move player hand back to start position
            Computer.turtle.setpos(70-30, -100-40)  # move computer hand back to start position

            self.turtle.setpos(-100, -120)  # move player hand back to start position
            Computer.turtle.setpos(70, -100)  # move computer hand back to start position

            self.turtle.setpos(-100+30, -120-40)  # move player hand back to start position
            Computer.turtle.setpos(70-30, -100-40)  # move computer hand back to start position

            self.turtle.setpos(-100, -120)  # move player hand back to start position
            Computer.turtle.setpos(70, -100)  # move computer hand back to start position

            self.turtle.setpos(-100 + 30, -120 - 40)  # move player hand back to start position
            Computer.turtle.setpos(70 - 30, -100 - 40)  # move computer hand back to start position


            # Choose a hand for the computer
            choose_hand(Computer)
            if get_winner(self.weapon, Computer.weapon) == "winner":
                Player.score +=1
                Score()
                Scorekeeper.turtle.shape(Scorekeeper.shapes[1])
            elif get_winner(self.weapon, Computer.weapon) == "tie":
                Scorekeeper.turtle.shape(Scorekeeper.shapes[2])
            else :
                Scorekeeper.turtle.shape(Scorekeeper.shapes[3])
                Computer.score += 1
                Score()
        else: #reset the hands for the next round
            self.turtle.setpos(-100, -120)  # move player hand back to start position
            Computer.turtle.setpos(70, -100)  # move computer hand back to start position
            self.choosing = True
            self.history.append(self.weapon) # add the choice to the Player.history list
            Scorekeeper.turtle.shape(Scorekeeper.shapes[0])
            Computer.turtle.shape(Weapons.computer_images[0])
            self.weapon = Weapons.weapon[0]
            self.turtle.shape(Weapons.player_images[0])

            return

class Computer:
    score = 0
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

class Score:
    turtle = turtle.Turtle()
    turtle.penup()
    turtle.setpos(0, 110)
    turtle.hideturtle()
    def __init__(self):
        """Refresh the score"""
        self.turtle.clear()
        #self.turtle.pencolor("white")
        self.turtle.write(str(Player.score)+"                "+str(Computer.score), move=False, align="center",
                font=("Arial", 20, "normal"))

def choose_hand(self):
    """
    choose a weapon and shape for an object
    :param self: an object with variables shape and weapon
    """

    w = random.randint(0, 4)
    if len(Player.history) > 0:
        if Player.history[len(Player.history)-1] == "rock":
            w = 4
    self.weapon = Weapons.weapon[w]
    self.turtle.shape(Weapons.computer_images[w])


def announce_overall_winner():
    """
    Announce the overall winner if the user gets a score over 10 or the
    computer gets a score over 10
    """
    global has_won
    if Player.score >= 9:
        has_won = True
        new_wn = turtle.Screen()
        Wn.wn.clear()
        new_wn.addshape("gifs/winner.gif")
        new_wn.bgpic("gifs/winner.gif") #set the background to the winner image
        winsound.PlaySound("sounds/win song.wav", winsound.SND_ASYNC)
        new_wn.mainloop()
    elif Computer.score >= 9:
        has_won = True
        Wn.wn.clear()
        new_wn = turtle.Screen()
        new_wn.addshape("gifs/loser.gif")
        new_wn.bgpic("gifs/loser.gif") # set the background to loser image
        winsound.PlaySound("sounds/machine wins.wav", winsound.SND_ASYNC)
        new_wn.mainloop()


def get_winner(self, computer):
    """
    return whether the player beat the computer tied or lost
    :param self
    :param computer
    :return "winner", "loser" or "tie".
    """
    announce_overall_winner()
    user = self
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
        Scorekeeper.turtle.shape(Scorekeeper.shapes[1])
        return "winner"
    elif user == computer:  # if the user and computer choose the same thing declare a TIE!
        Scorekeeper.turtle.shape(Scorekeeper.shapes[2])
        return "tie"
    else:   # if the computer wins return loser
        Scorekeeper.turtle.shape(Scorekeeper.shapes[3])
        return "loser"



def main():
    global has_won
    has_won = False
    # play a song
    winsound.PlaySound("sounds/RPS music.wav", winsound.SND_ASYNC)
    if (has_won == False):
        Score()
        Computer()
        Scorekeeper()
        Player()
        Tutorial()
        get_winner(Player.weapon,Computer.weapon)
    Wn.wn.mainloop()





if __name__ == "__main__":
    main()
