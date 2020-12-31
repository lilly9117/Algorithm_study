class Solution(object):
    def arrayPairSum1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        pair = []
        nums.sort() #오름차순 정렬
        
        for n in nums:
            pair.append(n)
            if len(pair) == 2:
                sum += min(pair)
                pair = []
                
        return sum
    
    # sol2: 짝수번째 값만 계산
    def arrayPairSum2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        nums.sort() # 정렬
        
        for i, n in enumerate(nums): #enumerate사용해서 짝수번째만!
            if i % 2 == 0:
                sum += n
                
        return sum

    # sol3 : 완전 간단?
    def arrayPairSum3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2]) # 짝수번째만 가져오는거 slicing으로!!!