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
#distribution of candies to people:
candies = 7
num_people = 4
li=[0]*num_people
give=1
while candies>0:
    for i in range(num_people):
        if candies==0:
            break
        total=min(give,candies)
        li[i]+=total
        candies-=total
        give+=1
print(li)