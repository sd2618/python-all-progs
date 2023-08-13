s=input("Enter string")
d=dict()
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print("The duplicate letters in string are=")
for i in d:
    if (d[i]>1):
        print(i)
    
