list1 = [1, 342, 75, 23, 98]
list2 = [75, 23, 98, 12, 78, 10, 1] 
list3=[]
i=0
while i<len(list1):
    c=list1[i]
    if c  in list2:
        list3.append(c)
    i=i+1
print(list3)













