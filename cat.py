#  print ("meow")
# # print ("meow")
# # print ("meow")

# x = 3
# while x != 0:
#     print("meow")
#     x = x -1
# y = 1
# while y <=3:
#     print("woof")
#     y = y + 1
# w = 0
# while w < 3:
#     print("meeee")
#     w += 1

#or y in [0,1,2,3]:
  # print("meow") 
# Instead of writing the above code like this it is best if you use a function called "range" . This prevents maual typing when you have a lot to type like 999,999..

# for y in range(4):
#     print("How are you doing")
# print("I am fine\n"* 4,end="")

# while True:
#     n = int(input("What's n?"))
#     if n > 0:
#         break
# for _ in range(n):
#     print("meow")
def main():
    number = get_number()
    meow(number)
def get_number():
    while True:
       n = int(input("What's n? "))
       if n > 0:
           break
    return n
def meow(n):
    for _ in range(n):
        print("meow")
main()