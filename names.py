# names = []
# for __ in range(3):
#     names.append(input("What's your name?"))
# for name in sorted(names):
#     print(f"hello, {name}")

# name = input("What's your name?")
# with open("names.txt", "a") as file:
#  file.write(f"{name}\n")
# with open("names.txt","r")as file:
#  for line in file:
#     print("Hello,",line.rstrip())
names =[]
with open("names.txt") as file:
    for line in file:
        names.append(line.strip())
for name in sorted(names):
    print(f"hello, {name}")
#The below is an example I formed myself
students = []
with open("students.txt") as file:
    for line in file:
        students.append(line.strip())
for student in sorted(students, reverse=True):
    print(f"You are welcome,{student}")