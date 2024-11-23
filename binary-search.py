print("Hello World")

def binarySeearch(list, target):
    first = 0
    last = len(list) - 1
    while first <= last:
        midpoint = (first + last) // 2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None

myList = [1, 3, 5, 7, 9]
print(binarySeearch(myList, 7)) # 1