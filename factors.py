# Author: Brian Hoang
# Date: 10/16/2019
# Description: asks user for a positive integer then ouputs all positive integers that divide that number evenly besides itself and 1 in ascending order

print("Please enter a positive integer:")
num1=int(input())                               #takes in user integer to be factored
print("The factors of ",int(num1), "are:")
start=2                                       #starts with 2 as number to be checked as factor and as tally

while(start<num1):                           #runs loop until tally reaches number before the user integer
    if(num1%start==0):                      #checks if remainder of user_int and start is 0
        print(int(start))                       #if so, program prints out int and adds tally
        start+=1
    else:
        start+=1                                #if there is a remainder(not a factor) then loop adds tally
