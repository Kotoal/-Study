def hashvark (arr):
    if len(arr) <= 1 :
        return arr

    ptuyp = arr[len(arr) // 2]
    left = [x for x in arr if x < ptuyp]
    middle =  [x for x in arr if x == ptuyp]
    right = [x for x in arr if x > ptuyp]
    return hashvark(left) + middle + hashvark(right)


l = [12,55,87,52,42,68,1,45]
print ("skzbnakan " , l)
print ("sortavorat" , hashvark(l))
            

