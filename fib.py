#fibonacci series
n=int(input())
a=0
b=1
c=0
for i in range(1,n+1):
  print(' '*(n-i),end='')
  for j in range(1,i+1):
   if(i==2 and j==1):
     print(b,end=' ')
   else:
     print(c,end=' ')
     c=a+b
     a=b
     b=c
  print(end='\n')
