#Guess the Right number!
#import emoji
import random
computer=random.randint(1,10)
guess=False
chance=0
print("Let's Start!")
print("Hello,What's your name?")
name=input()
print("Nice name! Okay",name,"Iam guessing a number between 1 and 10")
while guess==False and chance<5:
    guess=int(input(print("Guess a number")))
    if guess<computer:
        print("Your guess is too low",name,"!")
        chance=chance+1
    if guess>computer:
        print("Your guess is too large",name,"!")
        chance=chance+1
    if guess==computer:
        break
    guess=False
if guess==computer:
    print("EXCELLANT!Your guess is correct")
    print("You guessed in",chance,"tries!")
else:
    print("No more guess")
   
