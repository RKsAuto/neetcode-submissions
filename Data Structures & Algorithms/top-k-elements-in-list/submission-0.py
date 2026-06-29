from collections import defaultdict, Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        maxheap = []
        res = []
        for i in count.keys():
            c,v = count[i],i
            heapq.heappush(maxheap,(-c,v))
        for j in range(k):
            c,v = heapq.heappop(maxheap)
            res.append(v)
        return res
