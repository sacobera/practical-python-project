import random #imports the random module 

roll = random.randint(1, 6)  #this function would save a random number between 1 and 6 to the variable roll

# print("the computer rolled a " + str(roll))  simulation of rolling a dice 


#SIMULATING A GUESSING GAME 
guess = int(input("guess the dice roll: \n"))

if guess == roll:
    print("Correct! they rolled a " + str(roll))
else: 
    print("Wrong, they rolled a " + str(roll))