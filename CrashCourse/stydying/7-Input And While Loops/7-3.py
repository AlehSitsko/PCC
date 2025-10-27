#Multiple of ten
#User input for a number
number = input("Please enter the number: ")
number = int(number)
#Checking if the number is a multipication of ten
if number %10 == 0:
    print(f"\nThe number {number} is multiplication of ten")
else:
    print(f"\nThe numbere {number} is not a multiplication of ten")