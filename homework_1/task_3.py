
while True:
    number = input("Enter a number: ")

    if number == "":
        number = 0
    else:
        number = float(number)

    if number == 2520:
        print("Program finished")
        break

    print("Square:", number ** 2)
