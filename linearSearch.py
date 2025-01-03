class Solution:
    def search(self, nums: List[int], target: int) -> int:

        position = 0

        while True:
            if(nums[position] == target):
                return position 
            
            
            position+=1
            
            if(position == len(nums)):
                return -1