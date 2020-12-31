  
from typing import List


class Solution(object):
    # 1. 브루트 포스로 계산 -> 최적화 필요함 ㅠ
    # def threeSum(self, nums):
    #     results = []
    #     nums.sort() # 먼저 정렬

    #     # 브루트 포스 n^3 반복
    #     #three 포인트 풀이
    #     for i in range(len(nums) - 2):
    #         # 중복된 값 건너뛰기
    #         if i > 0 and nums[i] == nums[i - 1]:
    #             continue
    #         for j in range(i + 1, len(nums) - 1):
    #             if j > i + 1 and nums[j] == nums[j - 1]:
    #                 continue
    #             for k in range(j + 1, len(nums)):
    #                 if k > j + 1 and nums[k] == nums[k - 1]:
    #                     continue
    #                 if nums[i] + nums[j] + nums[k] == 0:
    #                     results.append([nums[i], nums[j], nums[k]])

    #     return results
    
    # 투 포인터 
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        results = []
        nums.sort()
        
        for i in range(len(nums) - 2):
            # 중복된 값 건너뛰기
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i+1, len(nums)-1 # 간격좁혀가면서 sum 계산
            
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                
                if sum < 0:
                    left += 1
                elif sum > 0 :
                    right -=1
                else: # 정답
                    results.append((nums[i], nums[left], nums[right]))
                    
                    # 양옆으로 ㄷㅇ일한 값 있을 수 있으므로 skip
                    while left < right and nums[left] == nums[left+1]:
                        left +=1
                    while left < right and nums[right] == nums[right -1]:
                        right -=1
                    
                    left +=1
                    right -=1
                    
        return results
                    
                    