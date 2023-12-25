
def linear_merge(list1, list2):
    list3 = list2+list1
    list3.sort()
    return list3

linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])