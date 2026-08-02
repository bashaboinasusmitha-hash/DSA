nums=[0,0]
li=[]
n=len(nums)
s=""
print(nums)     
for i in range(n-1):
    min_idx=i
    for j in range(i+1,n):
        if str(nums[j])+str(nums[min_idx])>str(nums[min_idx])+str(nums[j]):
            min_idx=j
    nums[i],nums[min_idx]=nums[min_idx],nums[i]
print(nums)
for i in nums:
    s+=str(i)
if s[0]=="0":
    print("0")
else:
    print(s)