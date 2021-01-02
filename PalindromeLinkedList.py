        
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

    def isPalindrome2(self, head):
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

    #런너 이용한 풀이 !!
    def isPalindrome3(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        rev = None
        slow = fast = head #빠른 런너, 느린런너 초기값 - head
        
        while fast and fast.next: # 런너 이동 -> next 존재하지 않을 때까지 이동
            fast  = fast.next.next # 빠른 런너는 2칸씩 이동
            rev, rev.next, slow = slow, rev, slow.next #느린 런너는 한칸씩 이동 -> 역순으로 연결 리스트 rev를 생성하는 로직 slow앞에 덧붙임
            #(앞에 계속 새로운 노드 추가되는 형태)  rev : slow의 역순 연결 리스트
            
        if fast: #fast가 아직 None이 아닌경우 slow한칸 더 이동
            slow = slow.next
            
        # 팰린드롬 여부 확인
        while rev and rev.val == slow.val : # rev하나씩 풀어가면서 비교
            slow, rev = slow.next, rev.next
        
        return not rev  
        # return not slow 가능
            