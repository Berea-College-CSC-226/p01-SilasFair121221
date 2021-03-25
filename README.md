# ❗CSC226 Project

**Term**: Spring 2021

**Author(s)**: Silas Fair

indicates action items; you should remove these emoji as you complete/update the items which they accompany. (This means that your final README should have no in it!)

---

**References**: 
Throughout this project, you have likely used outside resources. Reference all ideas which are not your own, and describe how you integrated the ideas or code into your program. This includes online sources, people who have helped you, and any other resources that are not solely your own contribution. Update as you go.

Python winsound - Sound playing interface for windows.
https://docs.python.org/3/library/winsound.html

Python turtle - change displayed background image
https://stackoverflow.com/questions/41664941/python-turtle-change-displayed-background-image

Music by Eric Matyas
www.soundimage.org
---

## Milestone 1: Setup, Planning, Design

**Title**: Rock Paper Scissors II

**Purpose**: Play a game of rock paper scissors lizard spock with the user

**Sources**:  Rock Paper Scissors Lizard Spock A06.

**Kanban Board**: https://trello.com/b/YKLXx2Ed/fairs-kanban-board

**CRC Card**:
  - Please write a CRC card for a class that your project will implement.
  - See this link for a sample CRC card and a template to
  use for your own cards (you will have to make a copy to edit): https://docs.google.com/document/d/1JE_3Qmytk_JGztRqkPXWACJwciPH61VCx3idIlBCVFY/edit?usp=sharing
  - Tables in markdown are not easy, so we suggest saving your CRC card
  as an image and including the image(s) in the README. You can do this
  by saving an image in the repository and linking to it. See the sample CRC card below - and replace it with your own.
  
![image](https://user-images.githubusercontent.com/78548914/110878955-20b95480-82aa-11eb-8629-b97a63d7e4f9.png)


---

## Milestone 2: Code

No README action items. Keep your Kanban board up to date, and focus on your code. 🙃

---

## Milestone 3: Virtual Check-in

Indicates what percentage of the project you have left to complete, and how confident you are feeling. 

**Completion Percentage**: 95%

**Confidence**: I am confident that I will have the project finished by the deadline. I have made a working rock paper scissors spock game using classes. The code needs some cleaning up and I need to add two more simple functions for when the player or computer gets the score above 10 to show that they won. I need to make sure my code is a little cleaner and easier to parse.

---

## Milestone 4: Final Code, Presentation, Demo

### User Instructions
The program tells the user how to use the program within the program so this explenation should not be neccessary, but just in case. 
Press keys 1 2 3 4 5 to choose between the five options of hand signs. 
Use space to start the round, and to go back to starting position after round is over.
If the user gets the score above 10, they win the game. If the computer gets a score over 10, the user losos.
 

### Errors and Constraints
Every program has bugs or features that had to be scrapped for time. Use this section to create a bullet list of all known errors and deficiencies that remain in your code. Bugs found that aren't acknowledged here will be penalized.

 If the user presses the spacebar too quickly the robot arm starts shaking and then does all the hand signs very quickly.
 I was not able to prevent the player from choosing a hand sign before resetting the position. I think this is an issue with loops and the order in which the classes are initialized and, but I could not figure out how to fix this issue.

### Reflection
In three to four well-written paragraphs, address the following (at a minimum):

- Why did you select the project that you did?
  I have experience making games in other languages so I knew a game was something I could do well and enjoy making. I chose to expand on the Rock Paper Scissors homework t16, because it was familiar to me and I understood how it worked. I also wanted to be able to work on a project that I could draw some pixel art for. This project seemed to me like it would be fun to draw the pixel art for. 
  
- How closely did your final project reflect your initial design?
  The output of the project was exactly how I had wanted it, but the CRC cards and idea of the code ended up being very different from the classes and code in the final. I had to make changes to fix bugs and change code as I learned more about how to use the turtle library, classes, and data storage. I had a much neater initial design for my code, but as I discovered that some of my plans were based on assumptions about python that were false. My lack of understanding meant that I had to make a lot of changes to the code, and resulted in a more untidy and confusing code than I had hoped for.
  
- What did you learn from this process?
  I learned that class attributes cannot be accessed outside the class unless the class has been initialized. This caused a lot of confusion in the beggining of my project, but eventually I discovered how it worked and could resumed making the project without errors. I also learned how to import gif files into the python directory, set the turtle's shape to a gif, and import and play sounds using winsound library. I also greatly improved my understanding of classes.
  
- What was the hardest part of the final project?
  When I made my CRC cards and plan for my project, I did not know exactly how Classes and turtle.Screens, and screen loops worked. After figuring out how these things worked through testing and faliure, I had to make so many changes to the code that it started to get confusing. Debigging and fixing the code when I did not know exactly what was wrong was the hardest part of the proccess of making my final project.
  
- What would you do differently next time, knowing what you know now?
  I would debug and test how functions work using print statements before adding too much to my project. I think the reason I had so much trouble with the ordering of my code was because I added too muvh to the code without testing each line. Next time I sould test my understanding of everything I use in the project if am not completely sure how it works. I assumed some things in python worked a certain way and planned my project around them working that way, but I ended up changing my entire plan because I had been mistaken on how some things worked. To avoid making this mistake in the future, I will test that all methods, classes, and libraries work how they need to in my project.
