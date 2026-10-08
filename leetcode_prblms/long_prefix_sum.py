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
number=30
if number<=1:
    print("NO")
for i in range(2,number):
    if number%i==0:
        print("Not")
        break
else:
    print("Yes")
series=5
a,b=0,1
for i in range(series):
    print(a,end=" ")
    a,b=b,a+b
print()
s1="hey"
s2="hello"
print(sorted(s1)==sorted(s2))
s="susmitha"
v=["a","e","i","o","u"]
n=len(v)
vow=0
cons=0
for i in range(len(s)):

    if s[i] in v:
        vow+=1
    else:
        cons+=1
print(vow)#3
print(cons)#5

num=[1,2,3,4,6]
n=max(num)
for i in range(1,len(nums)+1):
    if i not in num:
        print(i)
        
num = [1, 2, 3, 4, 6]
n = len(num) + 1
total = n * (n + 1) // 2
actual = sum(num)
missing = total - actual
print(missing)