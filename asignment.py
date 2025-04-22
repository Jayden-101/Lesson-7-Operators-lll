char = input("Enter a character: ")

if len(char) == 1:
    ascii_value = ord(char)
    print(f"the ASCII of the '{char}' is {ascii_value}.")
else:
    print("Please enter a=only a single character")