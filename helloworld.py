#A program to check wheteher a given number is odd or even
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

#also test for negative numbers
num = int(input("Enter a number: "))
if num < 0:
    print("The number is negative")
elif num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
    