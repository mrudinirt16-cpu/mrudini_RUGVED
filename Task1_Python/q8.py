str = input("Enter a string: ")
n = int(input("Enter number of characters in each part: "))

if len(str) % n != 0:
    print("Error: str cannot be divided into equal parts.")
else:
    parts = []
    for i in range(0, len(str), n):
        parts.append(str[i:i+n])
    same = True
    for part in parts:
        if part != parts[0]:
            same = False
            break
    if same:
        print("Parts:")
        for part in parts:
            print(part)
    else:
        print("Error")