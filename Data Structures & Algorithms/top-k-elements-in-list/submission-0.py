from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        top_item = count.most_common(k)
        res = [item[0] for item in top_item] 
        return res