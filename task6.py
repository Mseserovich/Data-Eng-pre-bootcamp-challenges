def max_number(a, b, c, *args):
    """Function that takes in three or more
        nums and returns max"""
    list1 = [a, b, c]
    list2 = [*args]
    full_list = list1 + list2

    max = full_list[0]
    for i in range(len(full_list) - 1):
        if full_list[i + 1] > max:
            max = full_list[i + 1]
    
    return max

print(max_number(1, 2, 3, 100, 4, 5, 6, 101, 102))