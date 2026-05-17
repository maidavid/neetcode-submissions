class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #array of strings. order is not an issue

        #count characters from a-z for each word
        #keep track with a Hashtable. key will be each count of the letters for the word
        #value would be the strings in the array
        #O(m*n*26) , m = length of string, *26 letters, total num of input strings

        result = defaultdict(list) #mapping charCount to list of Anagrams

        for s in strs:
            count = [0] *26  # a - z 

            for c in s:
                count[ord(c) - ord("a")] += 1

            result[tuple(count)].append(s) #use tuple mutable

        return list(result.values())
