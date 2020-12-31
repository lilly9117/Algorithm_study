        
import collections

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome1(self, head): # 리스트로 변환
        """
        :type head: ListNode
        :rtype: bool
        """
        q = [] # 리스트 0> pop함수에 인덱스 지정해서 얼마든지 원하는 위치 자유롭게 추출가능함
        
        if not head:
            return True
        
        node = head
        while node is not None:
            q.append(node.val) # list로 변환
            node = node.next 
            
        while len(q) > 1:
            if q.pop(0) != q.pop(): # 판별
                return False
            
        return True

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        q = collections.deque() # 데크 이용해서 최적화
        
        if not head:
            return True
        
        node = head
        while node is not None:
            q.append(node.val)
            node = node.next
            
        while len(q) >1:
            if q.popleft() != q.pop():
                return False
            
        return True
            