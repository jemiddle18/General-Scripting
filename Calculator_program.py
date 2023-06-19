# Value for the first number
value1 = input("Please enter in first number ")
mathsign = input("What operate you wish to use? Note: Only the following are accepted '+, -, *, /' ")
# If statement to determine if the operator selected is correct.
if mathsign in ['+', '-', '*', '/']:
    print("Operator selected is correct")
else:
    print("Invalid Operator, Please try again")

#Value for the second number
value2 = input("Please enter in second number ")

# Conduct calculations based on what was entered in by the user.
if mathsign == '+':
    print(float(value1) + float(value2))

if mathsign == '-':
    print(float(value1) - float(value2))

if mathsign == '*':
    print(float(value1) * float(value2))

if mathsign == '/':
    print(float(value1) / float(value2))



