s='abcabcfgdyhgt'
l=len(s)
k=''
for i in range(l):
    k=k+s[i]
    for j in range(i+1):
        if(s[j]==k[i]):
            break


print(k)
