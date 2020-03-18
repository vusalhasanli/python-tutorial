  
try:
    opernads = {"/", "+", "*", "/"}
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))
    operand = input("Enter operand: ")
    # print(a, b, operand)
    # print(a, b, operand)
    if operand == '+':
        print("{0} + {1} = ".format(a, b) + str(a + b))
    elif operand == '-':
        print("{0} - {1} = ".format(a, b) + str(a - b))
    elif operand == '/':
        print("{0} / {1} = ".format(a, b) + str(a / b))
    elif operand == '*':
        print("{0} * {1} = ".format(a, b) + str(a * b))
    #else: print("Something went wrong...")
except ValueError:
    print("That was not a number...")
except KeyError:
    print("Key Error")
except:
    if operand not in operands.keys():
        print("I do not know what is wrong")






    
