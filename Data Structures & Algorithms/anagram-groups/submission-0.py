from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = defaultdict(list)

        for word in strs:
            alpha = [0]*26
            for i in word:
                alpha[ord(i)-ord('a')] += 1
            results[tuple(alpha)].append(word)
        
        return list(results.values())
                