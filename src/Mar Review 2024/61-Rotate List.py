# Given the head of a linked list, rotate the list to the right by k places.

 

# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
# Example 2:


# Input: head = [0,1,2], k = 4
# Output: [2,0,1]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        # count the length 
        current = head
        length = 0
        while current:
            length += 1
            current = current.next
        
        # construct a dummy node
        dummy = ListNode(0)
        dummy.next = head
    
        # move ahead pointer for k%length steps first
        ahead = dummy
        k = k % length
        for i in range(k) :
            ahead = ahead.next
        
        # move ahead and behind at the same time
        behind = dummy
        while ahead.next:
            ahead = ahead.next
            behind = behind.next

        # re-organize 
        ahead.next = dummy.next
        dummy.next = behind.next
        behind.next = None

        return dummy.next