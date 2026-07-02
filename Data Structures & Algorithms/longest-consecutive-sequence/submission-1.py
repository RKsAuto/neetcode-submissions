class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        seq = []
        ml = 0
        for i in nums:
            if len(seq)== 0 or seq[-1]+1 == i:
                seq.append(i)
            elif seq[-1] == i:
                continue
            else:
                ml = max(len(seq),ml)
                seq = []
                seq.append(i)
        ml = max(len(seq),ml)
        return ml