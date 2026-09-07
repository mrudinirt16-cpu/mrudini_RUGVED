def ana(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
if ana(str1, str2):
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")