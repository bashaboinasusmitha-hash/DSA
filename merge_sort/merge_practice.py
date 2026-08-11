def merge(nums,lb,mid,up):
    b=[0]*len(nums)
    i=lb
    j=mid+1
    k=lb
    while i<=mid and j<=up:
        if nums[i]<=nums[j]:
            b[k]=nums[i]
            i+=1
            k+=1
        else:
            b[k]=nums[j]
            j+=1
            k+=1
    while i<=mid:
        b[k]=nums[i]
        i+=1
        k+=1
    while j<=up:
        b[k]=nums[j]
        j+=1
        k+=1
    for k in range(lb,up+1):
        nums[k]=b[k]
def merge_sort(nums,lb,up):
    if lb<up:
        mid=(lb+up)//2
        merge_sort(nums,lb,mid)
        merge_sort(nums,mid+1,up)
        merge(nums,lb,mid,up)
nums= [15, 5, 24, 8, 1, 3, 16, 10, 20]
merge_sort(nums,0,len(nums)-1)
print(nums)

