def modify_list(l):
    lst[:] = [int(i/2) for i in l if i%2 == 0]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)               # [5, 4]