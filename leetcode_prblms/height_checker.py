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
#relative sort array:
arr1 = [2,3,1,3,2,4,6,7,9,2,19] 
arr2=[2,1,4,3,9,6]
n=len(arr1)
key=max(arr1)
count=[0]*(key+1)
ans=[]
for i in range(n):
    count[arr1[i]]+=1
for j in range(len(arr2)):
    while count[arr2[j]]>0:
        ans.append(arr2[j])
        count[arr2[j]]-=1
print(ans)
for k in range(len(count)):
    while count[k]>0:
        ans.append(k)
        count[k]-=1
print(ans)