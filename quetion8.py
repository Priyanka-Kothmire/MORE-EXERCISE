list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16] 
b=[]
i=0
while i<len(list1):
    c=list1[i]
    if c is not list2:
        b.append(c)
    i=i+1
print(b)


























