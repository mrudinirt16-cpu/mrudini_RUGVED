def is_hill_number(n):
    s = str(n)
    if len(s) < 3:
        return False
    peak = s.index(max(s))
    if peak == 0 or peak == len(s) - 1:
        return False
    for i in range(peak):
        if s[i] >= s[i + 1]:
            return False
    for i in range(peak, len(s) - 1):
        if s[i] <= s[i + 1]:
            return False
    return True
num = int(input("Enter a number: "))
if is_hill_number(num):
    print(f"{num} is a Hill Number")
else:
    print(f"{num} is NOT a Hill Number")