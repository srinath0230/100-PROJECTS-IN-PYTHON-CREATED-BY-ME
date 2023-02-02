from art import logo
from replit import clear
#add
def add(n1,n2):
  return n1+n2
#subract 
def subract(n1,n2):
  return n1-n2
#multiply
def multiply(n1,n2):
  return n1*n2
#divide
def divide(n1,n2):
  return n1/n2

operations = {
  "+" : add,
  "-" : subract,
  "*" : multiply,
  "/" : divide
}
def calculator():
  print(logo)
  num1 = float(input("what's your first number: "))
  for symbols in operations:
    print(symbols)
  should_continue = True
  
  while should_continue:
    symbol = input("Enter the operation to be performed: ")
    num2 = float(input("what's the next number: "))
    calculation = operations[symbol]
    answer = calculation(num1,num2)
    print(f"{num1} {symbol} {num2} = {answer}")
    prompt = input(f"Type 'y' to continue the calculation with {answer}, type 'n' to start new calculation or type 'e' to exit: ").lower()
    if prompt == "y":
      num1 = answer
    elif prompt == "e":
      clear()
      return None
    else:
      should_continue = False
      clear()
      calculator()
calculator()
