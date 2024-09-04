elements=[1,1,2,3,4,4,4,5,6,7,10,11,10,5]
dupl=[]
for i in elements:
    if elements.count(i)>1 and i not in dupl:
        dupl.append(i)
print(dupl)