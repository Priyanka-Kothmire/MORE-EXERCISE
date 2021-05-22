string_list = ["Empathy", "Empathy", "Kindness", "Kindness", "Compassion", "Humble", "Humble"] 
l=[]
i=0
# count=0
while i<len(string_list):
    a=string_list[i]
    if a not in l:
        l.append(a)
        # count=count+1
    i=i+1
print(l)








