class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
       n=len(nums)

       for i in range(n-1):
         min_val=i
         for j in range(i+1,n):
            if nums[j]<nums[min_val]:
                min_val=j
         nums[i],nums[min_val]=nums[min_val],nums[i] 
       return nums           