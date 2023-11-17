# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        values = []
        current_node = head
        while current_node is not None:
            values.append(current_node.val)
            current_node = current_node.next
        return values == values[::-1]
