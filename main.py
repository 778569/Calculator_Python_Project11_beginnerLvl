# Calculator

#Add
def add(n1,n2):
  return n1 + n2

#Subtract
def sub(n1, n2):
  return n1 - n2

#Mulriply
def mul(n1, n2):
  return n1 * n2

#Divide
def div(n1, n2):
  return n1/n2

# Exponentiation
def exp(n1, n2):
    return n1 ** n2

# Integer Division
def int_div(n1, n2):
    if n2 != 0:
        return n1 // n2
    else:
        return "Cannot divide by zero"

# Modulo
def mod(n1, n2):
    if n2 != 0:
        return n1 % n2
    else:
        return "Cannot divide by zero"


operations = { 
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
    "**": exp,
    "//": int_div,
    "%": mod
      }
 
faction = operations["+"]
faction(2,3)

from art import logo

def calculator():
  print(logo)
  num1 = float(input("What is the first Number?: "))
  
  
  for symbol in operations:
    print(symbol)
    
  Should_continue = True
  while Should_continue:
    operation_symbol = input("Pick an Operation: ")
    num2 = float(input("What is the Second Number?: "))
    function = operations[operation_symbol]
    answer = function(num1, num2)
    
    
    print(f"{num1} {operation_symbol} {num2}  = {answer}")
    choise = input(f"Type 'y' to continues calculation with {answer}, or type 'n' to exit : ")
    if choise == 'y':
      num1 = answer 
    else:
      Should_continue = False;
      calculator()



calculator()