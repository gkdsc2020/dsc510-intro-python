# DSC510
# Week 3
# Programming Assignment - 3.1
# Author: Ganesh Kale
# Date: 12/20/2020
# The purpose of this program is to provide cable installation cost with discount based on cable length.

# declare the variable for base cost
base_cost = 0.87
print("Welcome to the OPTIMA - the fiber optic cable installation company")  # welcome message
company_name = input("Please tell us your company name: \n")  # save the company name given by user
try:
    cable_length = float(input("Now tell us length of cable to be installed in feet: \n"))  # save the cable length
    total_cost = round(base_cost * cable_length, 2)  # round the total cost to 2 digits
    if 100 < cable_length <= 250:
        calculated_cost = round(0.80 * cable_length, 2)
    elif 250 < cable_length <= 500:
        calculated_cost = round(0.70 * cable_length, 2)
    elif cable_length > 500:
        calculated_cost = round(0.50 * cable_length, 2)
    else:
        calculated_cost = total_cost   # no discount for cable length less than 100ft
    # Create Receipt with all the details on it
    print("\nThe Receipt for fiber optic cable installation cost:")
    print("Company Name: ", company_name)
    print("Length of cable to be installed: ", cable_length, "ft")
    print("Total Cost: $", total_cost)
    if cable_length > 100:
        print("Final Cost: $", calculated_cost, "Discount given since length of cable is more than 100ft")
    else:
        print("Final Cost: $", calculated_cost, "No discount provided since cable length is less than or equal to 100ft")
    print("Our Discounts are:\nup to 100ft: No Discount \n101ft-250ft: $0.80/ft \n251ft-500ft: $0.70/ft \n501ft & More: $0.50/ft")
    print("\nThank you from OPTIMA")
except ValueError as error:
    print("Please provide valid cable length in feet")
    print("Error Received: ", error)   # this error info can be logged instead printing, here printed for information only
# end
