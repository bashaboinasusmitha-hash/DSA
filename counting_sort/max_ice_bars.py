costs = [1,6,3,1,2,5]
coins=20
n=len(costs)
key=max(costs)
count=[0]*(key+1)
ans=[0]*n
res=0
for i in range(n):
    count[costs[i]]+=1
print(count)#[0, 2, 1, 1, 0, 1, 1]
for j in range(1,len(count)):
    count[j]+=count[j-1]
print(count)#[0, 2, 3, 4, 4, 5, 6]
for k in range(n-1,-1,-1):
    ans[count[costs[k]]-1]+=costs[k]
    count[costs[k]]-=1
print(ans)#[1, 1, 2, 3, 5, 6]
a=0
for m in range(len(ans)):
    res+=ans[m]
    if res<=coins:
        a+=1
print(a)