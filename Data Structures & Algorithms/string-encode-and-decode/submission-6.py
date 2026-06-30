class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res+=str(len(i))
            res+='#'
            res+=i
        return res

    def decode(self, s: str) -> List[str]:
        ans = []
        size = len(s)
        i=0
        print(s)
        while(i<size):
                j=i
                while s[j]!= '#':
                    j+=1
                length = int(s[i:j])
                ans.append(s[j+1:j+1+length])
                i = j+length+1
            
        return ans