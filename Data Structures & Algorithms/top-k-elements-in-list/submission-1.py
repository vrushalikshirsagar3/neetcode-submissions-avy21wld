class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt_nums = {}
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            cnt_nums[num] = 1 + cnt_nums.get(num, 0)
        for num, cnt in cnt_nums.items():
            freq[cnt].append(num)
        res = [] 
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if int(len(res)) == k:
                    return res