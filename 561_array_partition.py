class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse = True)
        ans = 0
        for i in range(0,len(nums)-1,2):
            ans += min(nums[i],nums[i+1])
        return ans

