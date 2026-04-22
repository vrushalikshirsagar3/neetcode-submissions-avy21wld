class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums) * 2
        ans = [0] * n
        j = 0
        for i in range(n):
            if j == len(nums):
                j = 0
            ans[i] = nums[j]

            j += 1
        return ans