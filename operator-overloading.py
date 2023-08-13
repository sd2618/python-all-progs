class Time:
    def __init__(self,hours,minutes):
        self.hours=hours
        self.minutes=minutes
    
    def __add__(self,other):
        return self.hours+ other.hours , self.minutes+other.minutes
    
h1=int(input("Enter hours"))
h2=int(input("Enter hours"))
m1=int(input("Enter minutes"))
m2=int(input("Enter minutes"))
c=Time(h1,m1)
s=Time(h2,m2)
print(c+s)



        