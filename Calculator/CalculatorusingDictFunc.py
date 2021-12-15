# add
def add(n1, n2):
  return n1 + n2

# subtract
def subtract(n1, n2):
  return n1-n2

# multiply
def multiply(n1, n2):
  return n1 * n2

# divide
def divide(n1 , n2):
  return n1/n2

operations = {
              "+" : add,
               "-" : subtract,
               "*" : multiply,
               "/" : divide
              }
def calculator():
    num1 = float(input("What's the first number? "))

    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        next_num = float(input ("What's the next number "))
        calculation_function= operations[operation_symbol]
        result = calculation_function(num1,next_num)
        print(f"{num1} {operation_symbol} {next_num} = {result}")

        continue_calculating = input(f"Type 'y' to continue calculating  with {result} or type 'n' to start a new calculation ")
        if continue_calculating == 'n':
            should_continue = False
            calculator()  # recursive function
        else:
            num1 = result


calculator()