class Solution(object):
    # Sol1: 브루트 포스로 계산
    def twoSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        
    # Sol2: in 이용
    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, n in enumerate(nums):
            remain = target - n
            
            if remain in nums[i+1:]: # 뒤에서 해당 값 있으면 return
                return nums.index(n), nums[i+1:].index(remain)+(i+1)
