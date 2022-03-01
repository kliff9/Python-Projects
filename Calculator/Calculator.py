
from CalculatorArt import logo

def add(n1, n2):                                                   #Addition Function
  return n1 + n2

def subtract(n1, n2):                                              #Subtract Function
  return n1 - n2

def multiply(n1, n2):                                              #Multiply Function
  return n1 * n2

def divide(n1, n2):                                                 #Divide Function
  return n1 / n2

operations = {                                                       #Dictionaries that matches the opperator with the function
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)

  num1 = float(input("What's the first number?: "))                                                 #User inputs the first number
  for symbol in operations:                                                                         #Prints Each Symbol
    print(symbol)
  should_continue = True                                                                            #Trigger
 
  while should_continue:
    operation_symbol = input("Pick an operation: ")                                                 #The Symbol gets entered
    num2 = float(input("What's the next number?: "))                                                #The 2nd number gets entered
    calculation_function = operations[operation_symbol]                                             #Based on symbol the Right function gets executed
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")                                           #Final result is printed

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':           #User can continue or start over
      num1 = answer
    else:
      should_continue = False
      calculator()

calculator()
