def c(str, shift):
    result = ""
    for char in str:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char
    return result
str = input("Enter a string: ")
shift = int(input("Enter shift value: "))
print("Encrypted str:", c(str, shift))