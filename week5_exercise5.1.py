# DSC510
# Week 5
# Programming Assignment - 5.1
# Author: Ganesh Kale
# Date: 01/15/2021
# The purpose of this program is to perform different math operations using loops and functions.

# function to calculate addition, subtraction, multiplication and division
def performCalculation(num):
    try:
        val1 = float(input('Please enter first number:\n'))
        val2 = float(input('Please enter second number:\n'))
        if num == 1:
            calc = val1 + val2
            print("Addition of given numbers", val1, " & ", val2, "is :", calc)
        elif num == 2:
            calc = val1 - val2
            print("Subtraction of given numbers", val1, " & ", val2, "is :", calc)
        elif num == 3:
            calc = val1 * val2
            print("Multiplication of given numbers", val1, " & ", val2, "is :", calc)
        elif num == 4:
            if val2 != 0:
                calc = round(val1 / val2, 2)
                print("Division of given numbers", val1, " & ", val2, "is :", calc)
            else:
                print('Please provide second non-zero number')
    except Exception as ex:
        print('Error occurred: ', ex)


# function to calculate average of given numbers
def calculateAverage():
    try:
        max_val = int(input('How many numbers you wish to enter\n'))
        count = 0
        total = 0
        if max_val > 0:
            for value in range(max_val):
                print('Please enter number', value + 1, ":")
                number = float(input())
                count = count + 1
                total = total + number
            print('Average of given numbers is: ', round(total / count, 2))
        else:
            print('Please enter valid non-zero number')
    except Exception as ex:
        print('Error occurred: ', ex)


# main section of program where user input asked for math operations

user_input = 'Yes'
try:
    while user_input.lower() == 'yes':
        user_input = input("Would like to perform math operations? enter Yes or No\n")
        if user_input.lower() == 'yes':
            user_choice = int(input(
                'Please enter the appropriate number 1:Addition, 2:Substraction, 3:Multiplication, 4:Division, 5:Average\n'))
            if user_choice in [1, 2, 3, 4]:
                performCalculation(user_choice)
            elif user_choice == 5:
                calculateAverage()
            else:
                print('Please enter valid number from given options')
        else:
            print('Thank you!!')
            break
except Exception as ex:
    print('Error occurred: ', ex)
