# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 재귀구조로 뒤집기
        
        def reverse(node, prev = None):
            if not node:
                return prev
            
            next, node.next = node.next, prev
            
            return reverse(next, node)
        
        return reverse(head)
        
        def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        # 반복구조로 뒤집기
        
        node, prev = head, None
        
        while node: # node None될때까지
            next, node.next = node.next, prev # node.next를 이전 prev 리스트로 계속 연결
            prev, node = node, next # node가 none이 될 때 prev는 뒤집힌 연결 리스트의 첫번째 노드가 된다
            
        return prev