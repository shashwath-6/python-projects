def list_seq(val : list ) -> list:
    return val if isinstance(val, list) else [val]

def remove_dup(lst : list) -> list:
    dup_coll=set()
    org_list=[]
    for item in lst:

        if item not in dup_coll:
               dup_coll.add(item)
               org_list.append(item)
    return org_list
list_1 = [x for x in range(10)]

print(list_1[0:9])

list1 = list_1.copy()

list1[2:5] = [x**2 for x in range(2,5)]
print(list1)

print(list_seq(list_1))
print(list_seq(list1))

list2 = [1,1,2,3,4,4,5,6,7,8,8,9,0,1,]
print(remove_dup(list2))

