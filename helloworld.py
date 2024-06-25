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

#also test for prime numbers
num = int(input("Enter a number: "))
if num < 0:
    print("The number is negative")
elif num == 0:
    print("The number is zero")
elif num == 1:
    print("The number is one")
else:
    for i in range(2, num):
        if num % i == 0:
            print("The number is not prime")
            break
    else:
        print("The number is prime")
