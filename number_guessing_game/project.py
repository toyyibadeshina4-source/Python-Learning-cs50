#Buiding of my first project with python 
import random
number = random.randint(1, 10)
#print(number) This is my cheat line to check if my "if block works really"
attempts = 0

while True:
   attempts +=1
   user_guess = int(input("Can you guess a number between 1 and 10?"))
   if user_guess == number:
       print(f"Good of you! You guessed it in {attempts} tries")
       break
   elif user_guess < number:
       print("Too low,guess higher")
  
   else:
    print("Too high,guess lower")
       

