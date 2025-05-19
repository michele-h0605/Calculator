#Initialize variables
result = float(0)
summation = 0
count = 0
average = 0

#import math functions
import math

#Display Menu
print(f'Current Result: {result}')
def display_menu():
    print("Calculator Menu")
    print("---------------")
    print("0. Exit Program")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Logarithm")
    print("7. Display Average\n")

display_menu()

#Creates a loop to ensure that the game runs until option 0 is selected
while True:
    menu = int(input("Enter Menu Selection: "))
    #Establish the outcomes for each condition
    if menu == 0:
        #Ensures that the loop is exited after the message is displayed
        print("Thanks for using this calculator. Goodbye!")
        break
    elif menu == 1:
        operand1 = (input("Enter first operand: "))
        if str(operand1) == "RESULT":
            operand1 = result
        else:
            operand1 = float(operand1)
        operand2 = float(input("Enter second operand: "))
        if str(operand2) == "RESULT":
            operand2 = result
        else:
            operand2 = float(operand2)
        result = operand1 + operand2
        summation += result
        count += 1
    elif menu == 2:
        operand1 = (input("Enter first operand: "))
        if str(operand1) == "RESULT":
            operand1 = result
        else:
            operand1 = float(operand1)
        operand2 = float(input("Enter second operand: "))
        if str(operand2) == "RESULT":
            operand2 = result
        else:
            operand2 = float(operand2)
        result = operand1 - operand2
        summation += result
        count += 1
    elif menu == 3:
        operand1 = (input("Enter first operand: "))
        if str(operand1) == "RESULT":
            operand1 = result
        else:
            operand1 = float(operand1)
        operand2 = float(input("Enter second operand: "))
        if str(operand2) == "RESULT":
            operand2 = result
        else:
            operand2 = float(operand2)
        result = operand1 * operand2
        summation += result
        count += 1
    elif menu == 4:
        operand1 = (input("Enter first operand: "))
        if str(operand1) == "RESULT":
            operand1 = result
        else:
            operand1 = float(operand1)
        operand2 = float(input("Enter second operand: "))
        if str(operand2) == "RESULT":
            operand2 = result
        else:
            operand2 = float(operand2)
        if operand2 != 0:
            result = operand1 / operand2
            summation += result
            count += 1
        else:
            print("Error: invalid input!")
            continue
    elif menu == 5:
        operand1 = (input("Enter first operand: "))
        if str(operand1) == "RESULT":
            operand1 = result
        else:
            operand1 = float(operand1)
        operand2 = float(input("Enter second operand: "))
        if str(operand2) == "RESULT":
            operand2 = result
        else:
            operand2 = float(operand2)
        result = operand1 ** operand2
        summation += result
        count += 1
    elif menu == 6:
        operand1 = (input("Enter first operand: "))
        if str(operand1) == "RESULT":
            operand1 = result
        else:
            operand1 = float(operand1)
        operand2 = float(input("Enter second operand: "))
        if str(operand2) == "RESULT":
            operand2 = result
        else:
            operand2 = float(operand2)
        if operand1 > 0 and operand1 != 1 and operand2 > 0:
            result = math.log(operand2, operand1)
            summation += result
            count += 1
        else:
            print("Error: invalid input!")
            continue
    elif menu == 7:
        if count > 0:
            average = summation / count
            print(f'Sum of calculations: {summation}')
            print(f'Number of calculations: {count}')
            print(f'Average of calculations: {average:.2f}')
            continue
        else:
            print("Error: No calculations yet to average!")
            continue
            #Does not prompt user for menu selection again, just continue to the next loop iteration
    else:
        print("Error: Invalid selection!")
        continue
    if menu != 0:
        print(f'Current Result: {result}')
        display_menu()

