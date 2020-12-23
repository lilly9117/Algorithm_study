# 로그 재정렬 
# 로그 가장 앞 부분 - 식별자
# 문자로 구성된 로그가 숫자 로그보다 앞에
# 문자 동일한 경우 식별자 순으로
# 숫자 로그는 입력 순서대로

class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        
        # 람다 + 연산자 이용
        letters, digits = [], []
        
        for log in logs:
            if log.split()[1].isdigit(): # 숫자 여부 판별 - isdigit()
                digits.append(log)
            else:
                letters.append(log)
        
        # 정렬 
        letters.sort(key = lambda x: (x.split()[1:], x.split()[0])) 
        return letters + digits # 문자 로그가 더 앞에 