
while True:
    year = input("Enter year: ")

    if year.isdecimal() and int(year) > 0:
        year = int(year)
        break
    else:
        print("Invalid year. Try again.")

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not a leap year")
