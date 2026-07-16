# while True:
#     try:
#         x = int(input("What's your age?"))
#     except ValueError:
#         print("Your age is not a number.Type figure instead!!!")
#     else:
#       break
# print(f"Your age is {x}")
def main():
 x = get_int("How many times do you eat a day?")
 print(f"You eat {x} times a day?")
def get_int(prompt):        try:
          return int(input(prompt))
        except ValueError:
           pass
main()