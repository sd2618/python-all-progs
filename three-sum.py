l=[9,2,1,6,-1,-4]
s=0
n=int(input("Enter a number=\n"))

for i in range(len(l)-2):
    for j in range(i+1,len(l)-1):
        for k in range(j+1,len(l)):
            s=0
            
            s=l[i]+l[j]+l[k]
            if s==n:
                print(l[i],l[j],l[k])

    
        


