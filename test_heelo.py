from heelo import hello
def test_default():
   assert hello() == "hello, world"

   
def test_argument():
   assert hello("Toyyib") == "hello, Toyyib"