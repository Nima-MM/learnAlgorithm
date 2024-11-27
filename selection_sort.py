from find_smallest import findSmallestInArr

def selectionSort(list):
    newArr = []
    for i in range(len(list)):
        smallest = findSmallestInArr(list)
        newArr.append(list.pop(smallest))
    return newArr

print(selectionSort([5, 3, 6, 2, 10]))