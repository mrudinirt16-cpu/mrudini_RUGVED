t = input("Enter the t: ")
l = 0
w = 1
s = 0
for char in t:
    if char.isalpha():
        l += 1
    if char == ' ':
        w += 1
    if char == '.' or char == '!' or char == '?':
        s += 1

L = (l / w) * 100
S = (s / w) * 100
grade = 0.0588 * L - 0.296 * S - 15.8
print("Grade level:", round(grade))