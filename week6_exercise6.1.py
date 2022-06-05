# DSC510
# Week 6
# Programming Assignment - 6.1
# Author: Ganesh Kale
# Date: 01/22/2021
# The purpose of this program is find the largest and smallest values from the list.

# function to sort the given list in descending order
def sort_list(unsorted_list):
    for i in range(len(unsorted_list)):
        for j in range(i+1, len(unsorted_list)):
            if unsorted_list[i] < unsorted_list[j]:
                unsorted_list[i], unsorted_list[j] = unsorted_list[j], unsorted_list[i]
    return unsorted_list


temperatures = []
sentinel = 0
count = 0
# largest_temp = 0
# smallest_temp = 0
message = 'Please enter the temperature, 0 to stop\n'
try:
    temp = float(input(message))
    while temp != sentinel:
        temperatures.append(temp)
        count = count + 1
        temp = float(input(message))
except Exception as ex:
    print('Error Received, ', ex)
print('Thank you!!')
if count > 0:
    print('The list of entered temperatures is: ', temperatures)
    print('The number of entered temperatures are: ', count)

    # sorted_temp = sorted(temperatures, reverse=True)  # save the sorted list in descending order using built-in sorted() function

    # since this is assignment so created function rather using built-in function to sort list.
    sorted_temp = sort_list(temperatures)   # save the sorted list in descending order from the function
    print('The largest temperature from the entered list is: ', sorted_temp[0])
    print('The smallest temperature from the entered list is: ', sorted_temp[-1])
else:
    print('Please enter valid temperature')
