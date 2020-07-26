list1 = [3, 7, 9, 12, 30, 85, 96, 131, 133, 134, 136, 150, 163]
# list1 = (3, 14)
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]

result = []
tmp = []
print(type(list1))

# for i in list2:
#     for j in list1:
#         if i !=j:
#             tmp.append(j)
#         else:
#             tmp.append(j)
#             result.append(tmp)
#             tmp=[]
# result.append(tmp)
# print(result)

def split_list(iterable, splitters):
    #Find index of each splitter value in the list
    indexes = []
    for splitter in sorted(splitters):
        try:
            split = iterable.index(splitter)
            indexes.append(split)
        except ValueError:
            #Splitter not found in list
            pass
    #Split the iterable into sublists based on indices
    split_lists = []
    start = 0
    for index in sorted(indexes):
        split_lists.append(iterable[start:index+1])
        start = index+1
    split_lists.append(iterable[start:])

    return split_lists

result = split_list(list2, list1)

print(result)
     

