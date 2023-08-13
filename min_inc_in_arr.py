l=[4,7,19,16]
m=[]
n=4
max=l[0]
s=0
for i in range (n):
    if max<l[i]:
        max=l[i]
for i in range(n):
    m.append(max-l[i])
k=l[1]
for i in range (n):
    if( k>m[i]):
        if m[i]==0:
            continue
        k=m[i]
for i in range (n):
    s=s+m[i]/k
print(s)