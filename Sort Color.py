def sortColors(self, nums: List[int]) -> None:
        count = [0]*( max(nums) + 1)
        b = [0]  * len(nums)
        for num in nums:
            count[num] += 1
        for i in range(1, max(nums) + 1):
            count[i ] = count[i] + count[i - 1]
           
        

        for i in range(len(nums)-1, -1 , -1):
            b[count[nums[i]]-1] = nums[i]
            count[nums[i]] -= 1
            
        for i in range(len(nums)):  
            nums[i] = b[i]
       
            
