def luhn(num):
    num = num.replace(" ", "").replace("-", "")
    total = 0
    rev = num[::-1]
    for i in range(len(rev)):
        digit = int(rev[i])
        if i % 2 == 1:
           digit = digit * 2
           if digit > 9:
              digit = digit - 9
        total += digit
    return total % 10 == 0
num = input("Enter credit card number: ")
if luhn(num):
    print("Valid credit card number")
else:
    print("Invalid credit card number")