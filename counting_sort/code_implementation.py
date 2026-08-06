nums= [2,1,1,0,2,5,4,0,2,8,7,7,9,2,0,1,9]
n=len(nums)
key=max(nums)
count=[0]*(key+1)
ans=[0]*n
#count frequenciees:
for i in range(n):
    count[nums[i]]+=1
print(count)#[3, 3, 4, 0, 1, 1, 0, 2, 1, 2]
#updating count array:
for j in range(1,len(count)):
    count[j]+=count[j-1]
print(count)#[3, 6, 10, 10, 11, 12, 12, 14, 15, 17]
#sort the array:
for k in range(n-1,-1,-1):
    ans[count[nums[k]]-1]=nums[k]
    count[nums[k]]-=1
print(ans)#[0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 4, 5, 7, 7, 8, 9, 9]
for num in range(n):
    nums[num]=ans[num]
print(nums)