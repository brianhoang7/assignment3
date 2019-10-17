# Author: Brian Hoang
# Date: 10/16/2019
# Description: Asks the user how many integers they want to enter and outputs the minimum and maximum numbers in that list
print("How many integers would you like to enter?")
user_input=int(input())                     #user input for how many integers program will enter
print("Please enter",int(user_input),"integers.")
start=1                             #sets starting tally for loop
num1=int(input())                   #takes first user integer input
min=num1                            #sets min as first int as base
max=num1                            #sets max as first int as base
while(start<user_input):           #keeps loop running until reaches user desired number of integers
    num1=int(input())               #will take in a new integer everytime loop is ran
    if(num1< min):                   #if integer is smaller than previously stored min, it will replace
        min=num1                    #if integer is larger than previously stored max, it will replace
    elif(num1>max):
        max=num1
    start+=1                          #adds 1 to start to increase loop tally. once tally reaches user_input, loop will stop
print("min: ",int(min))               #prints out min and max
print("max: ",int(max))
