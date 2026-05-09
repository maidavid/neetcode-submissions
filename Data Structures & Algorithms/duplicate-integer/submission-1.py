class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #need to have a counter and track if an item is seen
        #iterate through array

        #we can initialize a set to track the numbers that are seen
        seen = set()

        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return True

        return False
        


        
                  