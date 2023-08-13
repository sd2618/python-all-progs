def chk(l,u,n):
    for i in range(l,u+1):
        if i==n:
            return(True)
    return(False)

l=int(input("Enter lower limit"))
u=int(input("Enter upper limit"))
n=int(input("Enter number"))
t=chk(l,u,n)
if(t==True):
    print("Number in range")
else:
    print("Number not in range")

