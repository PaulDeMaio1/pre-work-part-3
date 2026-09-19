
Number_1 = int(input("Enter number 1: "))
try:
    Number_2 = int(input("Enter number 2: "))
except ValueError:
    print("That's not a valid number. Using 0 instead")
    Number_2 = 0

Number_3 = int(input("Enter number 3:    "))
print()
print(f"your numbers: {Number_1}, {Number_2}, {Number_3}")
sum = Number_1 + Number_2 + Number_3
average = sum / 3
print(f"sum: {int(sum)}")
print(f"average: {average:.2f}")