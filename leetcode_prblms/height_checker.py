heights = [1,1,4,2,1,3]
n=len(heights)
key=max(heights)
count=[0]*(key+1)
b=[0]*n
ans=0
for i in range(n):
    count[heights[i]]+=1
for j in range(1,len(count)):
    count[j]+=count[j-1]
for k in range(n-1,-1,-1):
    b[count[heights[k]]-1]=heights[k]
    count[heights[k]]-=1
for m in range(n):
    if heights[m]!=b[m]:
        ans+=1
print(ans)