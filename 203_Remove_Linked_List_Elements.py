# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Input: head = [1,2,6,3,4,5,6], val = 6
#Output: [1,2,3,4,5]
#Example 2:

#Input: head = [], val = 1
#Output: []
#Example 3:

#Input: head = [7,7,7,7], val = 7
#Output: []

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy

        while head:
            if head.val != val:
                prev.next = head
                prev = prev.next
            head = head.next

        prev.next = None
        return dummy.next
