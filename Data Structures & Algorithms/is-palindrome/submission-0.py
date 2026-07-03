import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        sub = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        print(sub)
        return sub==sub[::-1]

        