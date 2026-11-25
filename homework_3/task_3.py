
text = input("Enter text: ")

clean_text = ""

for letter in text:
    if "a" <= letter.lower() <= "z":
        clean_text += letter.lower()

if clean_text == clean_text[::-1]:
    print("Is palindrome")
else:
    print("Is not palindrome")
