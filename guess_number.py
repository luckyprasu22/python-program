#python program to create game "guess the number"
#import random
#mynum = random. randint(0,9)
mynum = 8
print("Ihave a Number in my mind (0-9) can you guess it?")
while True:
    usernum = int(input("Enter your guess: "))
    if(mynum == usernum):
        print("yes you are right")
        break
    elif(mynum>usernum):
        print("mynumber is greater than usernumber")
    else:
        print("mynumber is smaller than user number")
        
