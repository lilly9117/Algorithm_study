# 빗물 트래핑
# 높이를 입력받아 비 온 후 얼마나 많은 물이 싸일 수 있는지 계산

class Solution(object):
    def trap1(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        if not height:
            return 0
        # 투 포인터 
        rain = 0
        left = 0
        right = len(height)-1
        left_max = height[left]
        right_max = height[right]
        
        while left<right:
            left_max = max(height[left],left_max)
            right_max = max(height[right], right_max)
            
            if left_max <= right_max:
                rain += left_max - height[left]
                left+=1
            else:
                rain += right_max - height[right]
                right -=1
                
        return rain

    # Sol2 : 스택 쌓아가면서 어렵다ㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜ
    def trap2(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        stack =[]
        rain = 0
        
        for i in range(len(height)):
            #변곡점을 만나는 경우?
            #현재 높이가 이전 높이보다 높을 때 : 변곡점 만날 때마다 하나씩 꺼내면서
            while stack and height[i] > height[stack[-1]]:
                #스택에서 꺼냄
                top = stack.pop()
                
                if not len(stack):
                    break
                
                # 이전과의 차이만큼 물 높이 채워나감!
                distance = i - stack[-1] -1
                water = min(height[i], height[stack[-1]]) - height[top]
                
                rain += distance * water
            
            stack.append(i)
        
        return rain