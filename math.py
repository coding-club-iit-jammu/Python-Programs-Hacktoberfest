
a=[1,2,3,4]
i=0
a.sort()
l=len(a)
s=0
i=0
while(i<l):
    s=s+a[i]
    i=i+1
mean=s/l
median=0
if(l%2!=0):
    median=a[((l+1)//2)-1]
else:
    median=(a[((l//2)+1)-1]+a[(l//2)-1])/2
maxi=0
i=0
n=0
r=0
l=len(a)
while(i<l):
    n=a[i]
    count=0
    j=0
    while(j<l):
        if(a[i]==a[j]):
            count=count+1
        j=j+1
    if(count>=maxi):
        maxi=count
        r=a[i]
    i=i+1
print("median=",median)
print("mode",r)
print("mean:",mean)
