#Building of my first project with python 
import random
number = random.randint(1, 10)
#print(number) This is my cheat line to check if my "if block works really"
attempts = 0

while True:
   attempts +=1
   userguess = int(input("Can you guess a number between 1 and 10?"))
   if userguess == number:
       print(f"Good of you! You guessed it in {attempts} tries")
       break
   elif userguess < number:
       print("Too low,guess higher")
  
   else:
    print("Too high,guess lower")
       

