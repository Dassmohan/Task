def highest_and_lowest(sublists):
    high = float('-inf')
    low = float('inf')
    sublist1 = None
    sublist2 = None
    for sublist in sublists:
        total = sum(sublist)
        if total > high:
            high = total
            sublist1 = sublist
        if total < low:
            low = total
            sublist2 = sublist
    return sublist1, sublist2
sublists = [[1, 2, 3], [4, 5, 6], [10, 20, 30], [7, 8, 9]]
highest_total_sublist, lowest_total_sublist = highest_and_lowest(sublists)
print("Sublist with the highest total value:", highest_total_sublist)
print("Sublist with the lowest total value:", lowest_total_sublist)
