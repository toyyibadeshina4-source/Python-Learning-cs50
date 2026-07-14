#Documenting my progress through Harvard's CS50P, coming from a PHP background.

## Progress

Topics | Status |
Input, Strings, f-strings | Done|
Print parameters, split | Done|
Functions, return vs. print | Done |
Conditionals | Done
Taking note indentation
The use of Python Arithmetic Operators
Loops | Next

## Notes

## Coming from a PHP background, Python's indentation-based blocks took adjusting, but the code reads cleaner once it clicks. Learningin public tracking realpogress, notjust finished code. Just learning

## The explanation and secret behind the code of parity.py

If you type 6 :

1. main() runs, x= 6
2. is_even(x) is called- this jumps down to line 16, with n=6
3. inside is_even, 6 % 2 = 0 is True, so it hits return True
4. That True gets sent all the way back to line 11, replacing is_even(x) - so the line becomes if True:
5. Since It's True, print ("Even")
   In Summary: You don't see Line 16 working directly because it does'nt print
   anything - it quickly computes and answer and returns it to main() which then decides what to print. That is the whole point of return: it passes avalue back to the caller instead of displaying it.
   Why bother splitting it up like this intead of just doing if x % 2 ==0 directly in main()? Because now is_even is reusable- you call it from anywhere else in your program without repeating the modulus logic.

   def is_even(n) :
   if n % 2 == 0:
   return True
   else:
   return False
   The above code can be written in a shorter form:

   # return True if n % 2 == 0 else False

   or even I can even just say:
   # The use of case to replace the if statement
   Here we use what we call match and we use case_ when none is matched do this.The underscore means "anything else"

   # return n % 2 == 0 (this is very succint)

   ### Be careful that there is a great rule Under Loop
   When you type: x = 1 the equals to is an assignment operator that copies the vaue from the right to the left.
   The meaning of Loop is to repeat an action multiple times. It is like saying clap 3 times instead of saying clap!clap!clap!
   ### The Real difference between For and Whike Loops
   for loop- use when you know how many times to loop, or you're going through a known collection(list,dictionary,range)
Use the while loop when you don't know in advance how many times it'll run. It just keeps going as long as a condition stays True.
   Parallel journey: Cybersecurity under CSSF Academy.
