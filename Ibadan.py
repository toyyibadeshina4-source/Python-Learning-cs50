# students = ["Toyyib","Aisha", "Yusuf"]
# for i in range(len(students)):
#     print(i+1,students[i])

#students = ["Toyyib","Aisha", "Yusuf", "Habeeb"]
#houses = ["Agbowo", "Oke-Ado", "Bodija","Olodo"]
students= {
    "Toyyib": "Agbowo",
     "Aisha": "Oke-Ado",
      "Yusuf": "Bodija", 
      "Habeeb": "Olodo"
      }
# print(students["Toyyib"])
# print(students["Aisha"])
# print(students["Yusuf"])
# print(students["Habeeb"])
#for student in students:
   # print( student,students[student], sep=" lives in ")
          
# What if we had more information? It is better to create multiple dictionaries
graduands = [
 {"name": "Toyyib", "house": "Agbowo", "age": 20},
 {"name": "Aisha", "house": "Oke-Ado", "age": 19},
 {"name": "Yusuf", "house": "Bodija", "age":16},
 {"name": "Habeeb", "house": "Olodo", "age": None}                

]
for graduand in graduands:
    print(graduand["name"],graduand["house"], graduand["age"], sep="," )
          
