
list_1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]

list_2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]


# set_list_1 = set(list_1)

# set_list_2 = set(list_2)

# set_list_3 = set_list_1 & set_list_2

# print(list(set_list_3))


# set_list_3 = set_list_1.intersection(set_list_2)

# print(set(set_list_3))

def intersect_lst(lst1, lst2):
    
    set_lst1 = set(lst1)
    
    set_lst2 = set(lst2)
    
    set_lst3 = set_lst1 & set_lst2
    
    return list(set_lst3)


print(intersect_lst(list_1,list_2))