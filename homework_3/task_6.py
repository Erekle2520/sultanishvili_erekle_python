
fib = int(input("Enter number: "))

if 1 <= fib <= 100:
    fibonacci = []

    a = 0
    b = 1

    for i in range(fib):
        fibonacci.append(a)
        a, b = b, a + b

    print(fibonacci)
else:
    print("Invalid number")
