def bubbleSort(list):
    for i in range(len(list) - 1):
        for j in range(len(list) - 1 - i):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list


data1 = [41, 4, 23, 67, 12, 13, 99, 98]

print(bubbleSort(data1))


def selectSort(list):
    for i in range(len(list) - 1):
        index = i
        for j in (i + 1, len(list) - 1):
            if list[index] > list[j]:
                index = j
        list[i], list[index] = list[index], list[i]
    return list


data2 = [41, 4, 23, 67, 12, 13, 99, 98]

print(selectSort(data2))
