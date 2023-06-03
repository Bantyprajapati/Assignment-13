# Write a Python script to create a list, where each element of the list is a digit of agiven number.
number = int(input("Enter a number: "))
digit_list = [int(digit) for digit in str(number)]

print("Digit list:", digit_list)
