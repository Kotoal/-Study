def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

n = int(input('Tveq tveri qanaky: '))
l1 = []
for i in range(n):
    num = int(input(f'Tveq element {i + 1}: '))
    l1.append(num)

selection_sort(l1)
print('Dasavorvac list@: ', l1)
