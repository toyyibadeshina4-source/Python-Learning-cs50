# while True:
#     print('Who are you?')
#     name = input('>')
#     if name != 'Toyyib':
#         continue
#     print('Hello, Toyyib. What is the password? (It is a fish.)')
#     password = input('>')
#     if password == 'swordfish':
#         break
# print('Acess granted')

# total = 0
# for num in range(101):
#     total = total+num
# print(total)

#total = 0
# for i in range(2,8,4):
#     print(i)
# for i in range(5,-1,-2):
#     print(i)

# def hello():
#     print('Good morning')
#     print('Good afternon')
#     print('Good evening')
# hello()
# hello()
# print('One more Time')
# hello()
#---- Code That is in a Local Scope can't use variables in other local scopes----
def spam():
    eggs = 'No Food'
    bacon()
    print(eggs) # prints 'No Food'

def bacon():
    water = 'There is water'
    eggs = 'There is food'
    print(eggs)
    print(water)
spam()

#----- Code That is in a Local Scope can use global Variables----

def spam():
   print(eggs) # prints 'Buy everyday'
eggs = "Buy everyday"
spam()
print()
print()
print()

# The Global Statement-- When you need modification. 
def spam():
  global eggs
  eggs = 'spam'
eggs = 'global'
spam()
print(eggs)
# Scope Identification
def spam():
   global eggs
   eggs = 'spam' # This is the global variable
def bacon():
   eggs ='bacon' # This is a local variable
def ham():
   print(eggs) # This is the global variable
eggs = 'global' # This is the global variable


