#eucid alogarithm
#hcf and lcm
a=int(input("enter 1st no"))
b=int(input("enter 2nd no"))
hcf=1
r=1
if(a>b):
    while(r>0):
        r=a%b
        a=b
        b=r
    hcf=a
else:
    while(r>0):
        r=b%a
        b=a
        a=r
    hcf=b
print(hcf)
lcm=(a*b)//hcf
print(lcm)
        
