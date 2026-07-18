import sys 
#Check for errors
if len(sys.argv) < 2:
    print("Too few arguements")
elif len(sys.argv) > 3:
    print("Too many arguements")
else:
#Print name tags
    print("hello, my name is",sys.argv[1])
