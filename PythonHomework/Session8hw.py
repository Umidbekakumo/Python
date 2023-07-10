def merge(list1, list2):
    merged = list1 + list2
    sorted_list = sorted(merged)
    return sorted_list
list1 = [10,11,12,13,14,15,16,17,18,19]
list2 = [20,21,22,23,24,25]
merged = merge(list1, list2)
print(merged)


