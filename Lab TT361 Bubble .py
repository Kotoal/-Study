n = int(input('Tveq qanaky: '))
list1 = []
for i in range(n):
    num = int(input(f'Tveq tivy {i + 1}: '))
    list1.append(num)

def hashvark(list1):
    list2 = len(list1)
    for i in range(list2):
        for j in range(0, list2 - i - 1):
            if list1[j] > list1[j + 1]:
                list1[j], list1[j + 1] = list1[j + 1], list1[j]

hashvark(list1)
print(list1)
