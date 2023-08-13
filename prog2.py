s=input("Enter string")
d=dict()
p=dict()
f=0
s2=s.split()
for j in s2:
    
      if j!=' ':
        if j not in d:
            d[j]=1
        else:
            d[j]=d[j]+1
print(d)
k=d.values()
print("Dictionary values=",k)
m=min(k)
print("Minimum frequency count=",m)
for i in d:
    if d[i]>m:
        d[i]=d[i]-1
print(d)
for j in d:
    if(d[j]!=m):
        f=1
        

if(f==1):
   print("The frequency of all characters cannot be made same")
else:
    print("The frequency of all characters can be made same")        
    
        
            
