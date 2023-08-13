s=0
l=[]
for i in range(1,37):
    s=i**3-1
    l.append(s)
print(l)

print("\n\n")
k=0
t=[]
for i in range(36):
    k=i**4+2
    t.append(k)
print(t)

if (l==t):
    print("true")
else:
    print("false")
