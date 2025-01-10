class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        n = len(nums)
        
        current = sum(nums[:k])
        maxSum = current

        for i in range(k,n):
            current+= nums[i] - nums[i-k]
            maxSum = max(maxSum,current)

        return maxSum/k



        #sliding window approach used
