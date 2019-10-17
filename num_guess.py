# Author: Brian Hoang
# Date: 10/16/2019
# Description: asks user to enter number to be guessed. then asks user/player for a guess at original number and prints out if it is too low, too high, or is correct. then it will print out number of tries it took to guess
print("Enter the number for the player to guess: ")
num1=int(input())                                 #variable for actual number
print("Enter your guess.")
guess=int(input())                                #variable for player guess
start=0                                           #begins tally at 0
while True:
    if(guess==num1):                              #condition for if guess is correct
        start+=1                                    #adds 1 tally
        print("You guessed it in ",int(start),"tries.")        #prints how many tries player guessed it in
        break                                       #ends loop
    elif(guess>num1):                             #condition for if guess is too high
        start+=1                                    #adds tally
        print("Too high - try again:")              #prints out that guess is too high and to try again
        guess=int(input())                          #takes in another input
    elif(guess<num1):                             #condition for if guess is too low
        start+=1                                    #adds tally
        print("Too low - try again:")               #prints out that guess is too low and to try again
        guess=int(input())                          #takes in another input