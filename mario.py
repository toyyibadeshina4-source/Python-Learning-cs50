def main():
   print_column(8)

def print_column(height):
    for _ in range(height):
        print("#")

# The below code is for printing a row of characters. The function is called print_row and it takes in a parameter called width. The function prints a row of characters that is the width of the parameter passed in.

main()
def main():
    print_row(4)

def print_row(width):
        
        print("?" * width)
#The below code is for printing a square of characters. The function is called print_square and it takes in a parameter called size. The function prints a square of characters that is the size of the parameter passed in.

main()
def main():
     print_square(3)
def print_square(size): 
    for _ in range(size):
        print("#" * size)
main()

#Summary 
#You can use functions to print a column, row, or square of characters. The functions take in parameters that determine the height, width, or size of the shapes. The main function calls these functions with specific values to demonstrate their functionality.