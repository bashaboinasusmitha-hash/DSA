candyType = [1,1,2,3]
li=[]
n=len(candyType)
m=n//2
for i in candyType:
    if i not in li:
        li.append(i)
if len(li)>=m:
    print(m)
else:
    print(len(li))
#or
candyType=[6,6,6,6]
s=set(candyType)
m=len(candyType)
n=len(s)
print(min(m,n))
