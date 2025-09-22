def hashvark (arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = hashvark(arr[:mid])
    right = hashvark(arr[mid:])
    return merge(left , right)
def merge (left , right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


l = [12,55,87,52,42,68,1,45]
print ("skzbnakan ", l)
print ("dasavorvat" , hashvark(l))        