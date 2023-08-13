s=input("Enter string")
d=dict()
p=dict()
for i in s:
    for j in i:
        if j not in d:
            d[j]=1
        else:
            d[j]=d[j]+1
k=list(d.values())
print(k)
t=k.sort(reverse=True)
for i in k:
    for j in d:
        if d[j]==i:
            p[j]=i
print(p)
            
