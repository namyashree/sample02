num = int(input("Enter a non-negative integer: "))
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is {factorial}")
    print("factorial problem completed")