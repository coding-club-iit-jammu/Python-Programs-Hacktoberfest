s=input()
b=[]
for i in range(len(s)):
    c=s[i]
    count=0
    for j in range(len(s)):
        if (c==s[j]):
            count=count+1
    if(count not in b):
        b.append(count)
if(len(b)==1):
    print("all unique characters have same frequency")
else:
    print("all unique characters don't have same frequency")
