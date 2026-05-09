class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #iterate through all the numbers to see if they are any duplicates

        #for big 0(n) we would want to just iterate through the array once. 
        #So lets track the numbers that are seen in on a HashSet since
        #HashSets do not allow duplicates

        seen = set()

        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return True

        return False
         
         #memory complexity would be O(n) since using Hashset