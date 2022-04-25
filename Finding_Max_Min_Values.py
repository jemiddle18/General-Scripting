#The purpose of this script is to take an list of numbers and find the largest/smallest values.

number_list = ['1' , '2' , '3' , '4', '5', '6', '7', '8', '9', '10']


#Print the largest number in the list
print("The largest number in the list is: " + max(number_list))

# Print the smallest number in the list.
print("The smallest number in the list is: " + min(number_list))

# Add values to your list.
insert = input("Add a number to the list: ")
number_list.append(insert)
print("Updated numbers list: " + str(number_list))
