class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_anagrams = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            grouped_anagrams[tuple(count)].append(s)
        return list(grouped_anagrams.values())

        