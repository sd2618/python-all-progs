a=[1,2,2,3,5,3,2]
d={}
for i in range(len(a)):
    if a[i] not in d:
        d[a[i]]=1
    else:
        d[a[i]]+=1
print(d)
for i in d:
    if d[i]>1:
        print(i)
