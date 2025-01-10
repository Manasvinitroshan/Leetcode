class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        
        result = []
        leftsum = [0]
        rightsum = [0]

        for i in range(len(nums)):
            leftsum.append(nums[i]+leftsum[-1])
        
        for j in range(len(nums)-1,-1,-1):
            rightsum.append(rightsum[-1] + nums[j]) 


        rightsum = rightsum[::-1][1:]
        leftsum = leftsum[:-1]
        for k in range(len(nums)):
            result.append(abs(rightsum[k] - leftsum[k]))
            
 
        return result
    
    # prefix algorithm