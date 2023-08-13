s=input("Enter a string")
t=s.split()
l=[]
r=[]
for i in t:
    l.append((len(i),i))
l.sort(reverse=True)
for i,j in l:
    r.append(j)
print("Word in decending order=",r)
