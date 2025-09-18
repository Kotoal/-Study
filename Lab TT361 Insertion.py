n = int(input('Tveq qanaky: '))
list1 = []
for i in range(n):
    num = int(input(f'Tveq tivy {i + 1}: '))
    list1.append(num)

def hashvark(list1):
    for i in range(1, len(list1)):
        a = list1[i]
        j = i - 1
        while j >= 0 and int(list1[j]) > a:
            list1[j + 1] = list1[j]
            j -= 1
        list1[j + 1] = a

hashvark(list1)
print(list1)