def search(x, nums):
    low = 0
    high = len(nums)
    while(low <= high):
        middle = (low + high) // 2
        item = nums[middle]

        if(item == x):
            return(middle)
        elif(item < x):
            low = middle + 1
        elif(item > x):
            high = middle - 1
