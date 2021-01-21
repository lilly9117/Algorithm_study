# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head): #값만 교환
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        now = head
        
        while now and now.next:
            now.val, now.next.val = now.next.val, now.val
            now = now.next.next
            
        return head

    def swapPairs2(self, head): # ****반복구조로 swap
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        root = prev = ListNode(None)
        
        prev.next = head # ListNode{val: None, next: ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val:3, ...}}}}
        
        while head and head.next:
            # b가 a(head)를 가리키도록 
            b = head.next
            head.next = b.next
            b.next = head
            
            prev.next = b # prev가 b를 가리키도록 
            
            # 다음번 비교위해 이동
            head = head.next
            prev = prev.next.next
            
        return root.next

    def swapPairs3(self, head): # ****재귀구조로 swap
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head and head.next:
            p = head.next            
            # swap된 값 
            head.next = self.swapPairs(p.next) #재귀구조,,,
            p.next = head
            return p # 재귀
        
        return head
        
