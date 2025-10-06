def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def exponential_search(arr, target):
    if len(arr) == 0:
        return -1
    if arr[0] == target:
        return 0
    i = 1
    while i < len(arr) and arr[i] <= target:
        i *= 2
    result = binary_search(arr[:min(i, len(arr))], target)
    return result

arr = list(map(int, input("Tveq masivi tvery" ).split()))
arr.sort()  
target = int(input("Tveq tivy voronelu hamar "))

result = exponential_search(arr, target)

if result != -1:
    print(f"elementi indeksy {result}")
else:
    print("Elementy chi gtnvel")
