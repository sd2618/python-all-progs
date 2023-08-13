a=input("enter binary number 1=\n")
b=input("enter binary number 2=\n")
c=0
t=0
k=''
a=a.split()
b=b.split()
for i in range(len(a)-1,-1,-1):
    if(c==1):
        t=t+1
        if t==2:
            c=0
            t=0
    if (int(a[i])+int(b[i])+c)==0:
        k='0'+k
    elif (int(a[i])+int(b[i])+c)==1:
        k='1'+k
    elif (int(a[i])+int(b[i])+c)==2:
        k='0'+k
        c=1
    elif (int(a[i])+int(b[i])+c)==3:
        k='1'+k
        c=1
if c==1:
    k='1'+k
print(k)

    
        

        


