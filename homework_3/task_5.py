
first = input("Enter first string: ")
second = input("Enter second string: ")

first = first.lower()
second = second.lower()

if sorted(first) == sorted(second):
    print("YES")
else:
    print("NO")
