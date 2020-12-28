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
    
    # Sol3: 첫번째 수를 뺀 결과 키 조회 -> 시간복잡도 개선 O(n)
    def twoSum3(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, num in enumerate(nums): #키, 값 바꿔서 저장
            dic[num] =i
    
        for i, num in enumerate(nums):
            if (target-num in dic) and (i != dic[target-num]):# 타겟에서 첫번째 수 뺀 결과 조회
                return nums.index(num), dic[target-num]
    
    # Sol4: 쪼끔 간결하게
    def twoSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        
        for i, num in enumerate(nums):
            if target - num in dict:
                return [dic[target-num], i] # 정답 찾으면 바로 빠져나오도록
            dic[num]= i

    # Sol5 : 투  -> 풒이 불가,, 정렬이 안된 상태이기 때문에 sort는 사용하면 원래 index 찾기 힘드므로 X!!
    # def twoSum5(self, nums, target): 
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: List[int]
    #     """
    #     left = 0
    #     right = len(nums) -1
        
    #     while not left == right:
    #         if nums[left] + nums[right] <target:
    #             left +=1
    #         elif nums[left] + nums[right] > target:
    #             right-=1
    #         else:
    #             return left, right

