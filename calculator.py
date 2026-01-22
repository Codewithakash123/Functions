def add(a,b):
    c = a + b
    """This Function gives sum of two numbers"""
    print(c)
add(10,5)

def sub(a,b):
    c = a - b
    """This Function gives difference of two numbers"""
    print(c)
sub(10,5)

def mul(a,b):
    c = a * b
    """This Function gives product of two numbers"""
    print(c)
mul(10,5)

def div(a =0,b =1):
    """Returns the division of two numbers"""
    if b == 0:
        print("Error")
    c = a/b
    print(c)
div()

def Calculator():
  choice = int(input("Enter the Choice(1,2,3,4):"))
  num1 =  int(input("Enter the First number:"))
  num2 =  int(input("Enter the second number:"))
  if choice == 1:
          print("Result:", (num1 + num2))
  elif choice == 2:
          print("Result:", (num1 - num2))
  elif choice == 3:
          print("Result:", (num1 * num2))
  elif choice == 4:
          print("Result:", (num1 / num2))
  else:
          print("Invalid Choice")

Calculator()
