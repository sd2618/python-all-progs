s="leet**cod*e"
k=''
l=list(s)
print(l)
k=list(l)

for i in s:
    
   
    if (i=='*'):
        n=l.index(i)
        l.pop(n)
        l.pop(n-1)
   

print(l)

 