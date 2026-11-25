
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
    P = a + b + c
    p = P / 2
    S = (p * (p - a) * (p - b) * (p - c)) ** 0.5

    print("Perimeter:", P)
    print("Area:", S)
else:
    print("Invalid triangle")
