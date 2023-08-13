a={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
n=int(input("Enter number combination"))
z=list()
c=0
m=n
while m!=0:
    r=m%10
    c+=1
    m=m//10

if c==2:
    l=str(n)
    k=list(a[l[0]])
    p=list(a[l[1]])
    for i in k:
        for j in p:
            z.append((i+j))
    print(z)
    
elif c==1:
    print(a[n])



