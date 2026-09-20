import sys 

# if len(sys.argv) < 2:
#     sys.exit("Too few arguements")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguements")

# print("hello, my name is",sys.argv[1])
if len(sys.argv) < 2:
    sys.exit("Too few arguements")
for arg in sys.argv[1:]:
    print("My name is",arg)