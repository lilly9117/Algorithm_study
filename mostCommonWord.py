# 금지된 단어 제외한 가장 흔하게 등장하는 단어 출력
# 대소문자 구분 하지 x, 구두점 무시


from collections import Counter

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        
        #데이터 전처리
        words = [word for word in re.sub('[^\w]',' ', paragraph).lower().split() 
                if word not in banned] # 정규표현식 사용
        
        counts = Counter(words) # counter 객체 사용
        
        return counts.most_common(1)[0][0] #가장 흔하게 등장하는 단어의 첫번째 index로