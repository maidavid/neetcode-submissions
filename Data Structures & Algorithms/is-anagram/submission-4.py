class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}
        countT = {}

        #check if both len are the same. anagrams have to have the same letters.
        if len(s) != len(t):
            return False

        #iterate through both words by indexes and add to dictionary then compare
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT
        