class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0 
        p_cnt = 0 
        for num in nums:
            if num == 1:
                cnt += 1
            else:
                p_cnt = max(p_cnt, cnt)
                cnt = 0
        return max(cnt, p_cnt)