def search(x, nums):
    low = 0;
    high = len(nums)
    while low <= high:
        mid = low + high // 2
        item = nums[mid]
        if x == item:
            return(mid)
        elif x < item:
            high = mid -1 
        elif x > item:
            low = mid + 1
search(3, [1,2,3,4,5])
