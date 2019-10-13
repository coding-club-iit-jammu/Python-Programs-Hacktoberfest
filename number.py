
a=input("enter string")
#Palindrome
b=''
i=len(a)-1
while(i>=0):
    b=b+a[i]
    i=i-1
if(b==a):
    print("palindrome")
else:
    print("not palindrome")
    
#Prime
n=int(a)
f=0
i=2
while i<=n**0.5:
    if(n%i==0):
        f=1
        break
    i=i+1
if(f==0):
    print("Prime No")
else:
    print("Not prime no")

#Perfect no
n=int(a)
s=0
for i in range(1,n):
    if(n%i==0):
        s=s+i
if(s==n):
    print("Perfect no")
else:
    print("not perfect no")
