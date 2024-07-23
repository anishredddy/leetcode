from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_anagrams = defaultdict(list)

        for string in strs:
            # Count the occurrences of each character in the string
            char_count = [0] * 26
            for char in string:
                char_count[ord(char) - ord('a')] += 1

            key = tuple(char_count)
            grouped_anagrams[key].append(string)
        return list(grouped_anagrams.values())