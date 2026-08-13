#quick sort implementation when pivot = first element:
def partition(nums,low,high):
    pivot=nums[low]
    start=low+1
    end=high
    while start<end:
        while start<high and nums[start]<=pivot:
            start+=1
        while end>low and nums[end]>pivot:
            end-=1
        if start<end:
            nums[start],nums[end]=nums[end],nums[start]
    nums[low],nums[end]=nums[end],nums[low]
    return end
def quick_sort(nums,low,high):
    if low<high:
        p=partition(nums,low,high)
        quick_sort(nums,low,p-1)
        quick_sort(nums,p+1,high)
nums=[8, 3, 1, 7, 0, 10, 2]
quick_sort(nums,0,len(nums)-1)
print(nums)