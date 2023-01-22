from collections import Counter 
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr)
        s = []
        for key,val in count.items():
            if val == 1:
                s.append(key)
        if k > len(s):
            return ""
        else:
            return s[k-1]
