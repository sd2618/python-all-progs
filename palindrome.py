n=321
m=n
s=0
while(m!=0):
    r=m%10
    s=s*10+r
    m=m//10

print(s)

if(n==s):
  print("palindrome")
else:
   print("not palindrome")

