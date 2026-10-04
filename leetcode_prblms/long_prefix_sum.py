nums = [1,2,3,2,5]
n=len(nums)
ans=nums[0]
for i in range(1,n):
    if nums[i]==nums[i-1]+1:
        ans+=nums[i]
    else:
        break
print(ans)
while ans in nums:
    ans+=1
print(ans)
num=212
x=num
rev=0
while num>0:
    digits=num%10
    rev=10*rev+digits
    num=num//10
if rev==x:
    print("palindrome")
else:
    print("not")
num=4
res=1
for i in range(1,num+1):
    res*=i
print(res)