#count no of pairs of elements in a given list whose sum is equal to given sum 
x=input().split(' ')
n=int(x[0])    #no of elements of list
s=int(x[1])    #required sum
count=0
b=[]
a=input().split(' ')
for i in range(n):
    f=0
    for j in range(n):
        if(int(a[i])+int(a[j])==s):
            f=1
            p=a[i]
            q=a[j]
            break
    if(f==1):
        if(p not in b and q not in b):
            b.append(p)
            b.append(q)
            count=count+1
print(count)      #no of pairs


