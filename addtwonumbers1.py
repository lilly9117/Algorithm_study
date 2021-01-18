# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# sol1 : 자료형 변환 -> 여러 함수 이용
class Solution(object):
    
    # 먼저 역순으로 된 연결리스트 뒤집기 -> 저번 문제에 풀이했었음...
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
    
    # 그 다음 연결 리스트를 파이썬의 리스트로 변경
    def toList(self, node):
        list = []
        while node:
            list.append(node.val)
            node = node.next
        return list
    
    # 파이썬 리스트를 연결 리스트로 변경하는 함수
    def toReverseLinkedList(self, result = ListNode):
        prev = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node
        return node
    
    # 드디어 두 연결리스트 덧셈,,,
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))
        
        # 덧셈연산위해 int형태로 결합
        resultStr = int(''.join(str(e) for e in a)) + int(''.join(str(e) for e in b))
        
        return self.toReverseLinkedList(str(resultStr))