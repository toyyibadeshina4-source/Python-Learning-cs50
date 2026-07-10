name =input("What is your name? ") 
#if name=="Toyyib" or name=="Adeshina" or name=="Adewale":
    #print("You are welcome to the white house")
#The line 5 and 6 below can be replaced with line 2
# elif name =="Adeshina":
#      print("You are not welcome to the white house")
# elif name =="Adewale":
#     print("You are welcome to the white house but you will be monitored")
# elif name =="Adebayo":
#     print("You are welcome to the white house but you will be monitored")
# else:
#     print("Wetin you come do for here? You are not welcome to the white house")
# The below explains that the match statement is a better way to write the above code
match name:
    case "Toyyib":  
        print("You are welcome to the white house")
    case "Adeshina":
        print("You are not welcome to the white house")
    case "Adewale":
        print("You are not welcome to the white house but you will be monitored")
    case "Adebayo" | "Kayode" | "Akin":
        print("You are welcome to the white house but you will be monitored")
    case _:
        print("Wetin you come do for here? You are not welcome to the white house")