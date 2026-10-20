
number = int(input("Enter number: "))

if 1 <= number <= 1000:
    for i in range(1, number + 1):
        if number % i == 0:
            print(i, end=" ")
else:
    print("Invalid number")
