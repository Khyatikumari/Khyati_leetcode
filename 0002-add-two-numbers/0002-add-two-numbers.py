# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        initn = ListNode(-1)
        k = initn

        # iterate both lists with 2 pointers
        # add values, create new node and attach to previous
        # continue adding till any one of the list is done
        # then iterate the remaining parts of the list and add 

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            res = v1 + v2 + carry
            carry = res // 10
            
            curr = ListNode(res % 10, None)
            k.next = curr
            k = curr

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return initn.next