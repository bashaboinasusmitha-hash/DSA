'''Adding two strings without using the built in functions. Here we can use ord() and chr().'''
s1="121"
s2="349"
i=len(s1)-1
j=len(s2)-1
carry=0
result=""
while i>=0 or j>=0 or carry:
    a=ord(s1[i])-ord('0')
    b=ord(s2[j])-ord('0')
    total=a+b+carry
    digits=total%10
    carry=total//10
    result=chr(digits+ord('0'))+result
    i-=1
    j-=1
print(result)    #470
#explanation:

nums=[2,7,8,10,8,10,1,10,5,9]
n=len(nums)
element_sum=0
digits_sum=0
for i in range(n):
    element_sum+=nums[i]
    while nums[i]>0:
        digits=nums[i]%10
        digits_sum+=digits
        nums[i]=nums[i]//10
print(abs(element_sum-digits_sum))