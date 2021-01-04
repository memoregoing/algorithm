import collections
from typing import *

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        for word in strs:
            anagrams["".join(sorted(word))].append(word)
        return anagrams.values()


if __name__ == '__main__':
    s = Solution()
