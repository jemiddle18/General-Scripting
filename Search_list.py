#Writing a program that will search through a list of numbers

numbers_list = ['1','2','3','4','5','6','7','8','9','10']

guess = input("Guess a number ")

if guess in numbers_list:
    print("This number is in the list.")
else:
    print("This number is not found.")

for x in numbers_list:
    print("Full list of numbers: " + str(numbers_list))
    break


