text = input("Enter a string: ")
sorted_chars = sorted(text)

counts = {}
for char in sorted_chars:
    counts[char] = counts.get(char, 0) + 1

print("Sorted String:", "".join(sorted_chars))
print("Character Counts:")
for char, count in counts.items():
    print(f"'{char}': {count}")