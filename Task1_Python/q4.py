def sort(str):
    arr = list(str)
    n = len(arr)
    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return "".join(arr)
str = input("Enter a string: ")
print("Sorted string:", sort(str))