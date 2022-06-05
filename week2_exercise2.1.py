# DSC510
# Week 2
# Programming Assignment - 2.1
# Author: Ganesh Kale
# Date: 12/07/2020
# The purpose of this program is to provide fiber optic cable installation cost by getting details from customers.

# declare the variable for base cost
base_cost = 0.87
print("Welcome to the OPTIMA - the fiber optic cable installation company")  # welcome message
company_name = input("Please tell us your company name: ")   # save the company name given by user
cable_length = input("Now tell us length of cable to be installed in feet: ")  # save the cable length
total_cost = round(base_cost*float(cable_length), 2)   # round the total cost to 2 digits
# Create Receipt with all the details on it
print("\nThe Receipt for fiber optic cable installation cost details:")
print("Company Name: ", company_name)
print("Cable Length in feet: ", cable_length, "ft")
print("Calculated Cost: $", total_cost)
print("Total Cost: $", total_cost)
print("\nThank you from OPTIMA")
# end
