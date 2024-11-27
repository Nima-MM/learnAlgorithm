def bubbleSort(list):
    n = len(list)
    for i_outer_loop in range(n, 1, -1):
        for i in range(i_outer_loop - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
    return list

unsorted_list = [64, 34, 25, 12, 22, 11, 30]
sorted_list = bubbleSort(unsorted_list)
print("Sortierte Liste:", sorted_list)