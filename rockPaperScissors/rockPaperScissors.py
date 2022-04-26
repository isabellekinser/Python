'''
The objective of this program is to make a rock, paper, scissors game for
the user to play against the computer. 
@author: Isabelle Kinser 
'''

#import random 
import random

#make a boolean variable called keepPlaying to track weather they want to 
#keep playing and set it to True. 
keepPlaying = True 

#LOOP ONE: Make a loop that continues while keepPlaying is True. 
    #Print out a statement that welcomes the user to the game.
while(keepPlaying):
    print("Welcome to rock, paper, scissors!")
    print("Best two out of three. Press 'q' to quit")
    if(userChoice == "q")
        break 
    #Make variables called userScore and cpuScore to track scores, set to 0.
userScore = 0
cpuScore = 0
    
    #LOOP TWO: Make a round loop that continues while the userScore and cpuScore
    #is less than 2. Use .lower() to make the users choice all lower case. 
    
                        #x = input("promt").lower()
    while(userScore < 2 and cpuScore < 2):
        #Use input() to get choice from user (rock, paper, scissors, q). 
        choice = input("Please choose (rock, paper, scissors): ")
        print(choice)
        #Store that choice in a variable
        
        #Make a list of choices, then use random.choice() to get a random 
        #choice from the cpu. Store the choice in a variable. 
        choiceList = ["rock", "paper", "scissors"]
        cpuChoice = random.choice(choiceList)
        
        #Make a if/elif/else statement to check the users input against
        #the cpu's choice.
        
        #NOTE: You will have to compare the users choice and the cpu's choice to
        #"rock", "paper", and "scissors" separately and combine with logical 
        #operators. EXAMPLE of a tie:
        '''
        if((user == "rock" and cpu == "rock") or (user == "paper" and cpu == "paper") 
        or (user == "scissors" and cpu == "scissors")):
        
            print("DRAW")
            print("User: " + str(userScore) + "CPU: " + str(cpuScore))
        '''
        #If the user won, add one to the users score, then print out the scores
        #"User: (#), CPU: (#)".
        if((user == "rock" and cpuChoice == "scissors") or (user == "paper" and cpuChoice  == "rock") 
        or (user == "scissors" and cpuChoice  == "paper")):
         
            print("You won!")
            print("User: " + str(userScore) + "CPU: " + str(cpuScore))
        #else if (elif) the computer won, add one to the computer's score, then'
        #print out the scores...
        elif((user == "scissors" and cpuChoice  == "rock") or (user == "paper" and cpuChoice  == "scissors") 
        or (user == "rock" and cpuChoice  == "paper")):
        
            print("CPU won!")
            print("User: " + str(userScore) + "CPU: " + str(cpuScore))
        #else if it is a draw, print "DRAW", then print out the scores...
        elif((user == "rock" and cpuChoice  == "rock") or (user == "paper" and cpuChoice  == 
            "paper") or (user == "scissors" and cpuChoice  == "scissors")):
        
            print("DRAW!")
            print("User: " + str(userScore) + "CPU: " + str(cpuScore))
        #else if the user entered "q", then end the round, and the game loop. 
        #Use the break statement to end the round. Make keepPlaying equal False. 
if(choice.lower() == "q"):
    keepPlaying == False
    
        #else the user didn't enter an accepted input, print(Not an option, try
        #again". 

    #print out the thank you message.
print("Thank you for playing!")
    #print out who won.
    
    #if the userScore is 2, then the user won.
        #code
if(userScore == 2):
    print("You won!")
    
    #elif the cpuScore is 2, then the cpu won. 
        #code
if(cpuScore == 2):
    print("CPU won!")
    #print out the final scores.
print("User: " + str(userScore) + "CPU: " + str(cpuScore))
