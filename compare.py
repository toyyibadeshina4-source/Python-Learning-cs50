x = int(input("What's x?"))
y = int(input("What's y?"))
if x == y:
    print("x is equal to y")
else:
    print("x is not equal to y")


    #Summary
    #Do not forget that the if statement is the one that actually connects everything together. Then we have the logical equals to and the opposite represented by ! symbol. ALso do not forget that Python requires indentation.
    
    # We have what we call flow chart. This helps you to trace your code logic and allows you make fewer mistakes.
    # the elif is a conjuction of else and if.
    # Be careful of bug indentation. Python uses indentation not braces like other languages to know what belongs inside a block versus what comes after it. Every statement that starts a block_ if, elif, for, while,etc. must be followed by an indented block underneath it, and the block ends when the indentation goes back to the previous level. If you do otherwise you will get an indentation error!
    #So think of indentation like nested boxes:whatever is indented is the box above it.