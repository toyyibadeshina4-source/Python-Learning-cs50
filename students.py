# import csv
# students = []
# with open("students.csv") as file:
#    reader= csv.DictReader(file)
  
#    for row in reader:
#       students.append(row)
    
# for student in sorted(students, key=lambda student: student["name"]):
#    print(f"{student['name']} is from {student['home']} and {student['school']}")
import csv
name = input("What's your name?")
home = input("Where's your home?")
school = input("What is your school name?")
with open("students.csv","a", newline="") as file:
 writer = csv.DictWriter(file, fieldnames=["home","name","school"])
 writer.writerow({"home":home,"name":name,"school":school})

