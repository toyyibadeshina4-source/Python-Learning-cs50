# x = int(input("What's your x? "))
# print("x is", x)
 #Do not forget the f string if you want to naturally write the variable instead of using commas:
# print(f"x is {x}")
#The code below explains the difference of using the print function immediately after a variable and not. If you use print in a else block it will definetely not catch any error if your user uses something you did not ask for. What I mean here is that the except block will not operate at all. So also if you use print as a new block not in try block, there will be the "NameError" in your terminal.
#So in Summary take note of the difference between "code that may fail and I am handling" from "code that should run only after success but not monitored for errors"

try:
   x = int(input("What's x?"))
  
   print(f"x is {x}")

except ValueError:
 print("x is not an integer")
print("Program continues normally")
try:
   y = int(input("What is y?"))
except ValueError:
  print("y is not an integer")  