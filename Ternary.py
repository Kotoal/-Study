def ternary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        one_third = left + (right - left) // 3
        two_third = right - (right - left) // 3
        if arr[one_third] == target:
            return one_third
        if arr[two_third] == target:
            return two_third
        if target < arr[one_third]:
            right = one_third - 1
        elif target > arr[two_third]:
            left = two_third + 1
        else:
            left, right = one_third + 1, two_third - 1
    return -1
arr = list(map(int, input().split()))
target = int(input(" "))

result = ternary_search(sorted(arr), target)

if result != -1:
    print(result)
else:
    print("Aetpisi tiv chka cucakum")