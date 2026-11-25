
import random

numbers = []

for i in range(5):
    numbers.append(random.randint(1, 4))

result = []

for number in numbers:
    for i in range(number):
        result.append(number)

print("Original list:", numbers)
print("List:", result)
print("Length:", len(result))
