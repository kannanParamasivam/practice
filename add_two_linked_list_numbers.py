from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        carry_over = 0
        head = ListNode(None)
        cur = head

        while l1 != None or l2 != None or carry_over > 0:
            digit_1 = l1.val if l1 != None else 0
            digit_2 = l2.val if l2 != None else 0
            digit_sum = digit_1 + digit_2 + carry_over
            cur.next = ListNode(digit_sum) if digit_sum < 10 else ListNode(digit_sum%10)
            cur = cur.next
            carry_over = digit_sum // 10 if digit_sum >= 10 else 0
            l1 = l1.next if l1 != None else None
            l2 = l2.next if l2 != None else None
        
        return head.next

    
    def get_linked_list(self, num_in_reverse: List[int]):
        head = ListNode(None)
        cur = head

        for digit in num_in_reverse:
            cur.next = ListNode(int(digit))
            cur = cur.next

        return head.next

    
    def get_num_in_reverse_from_linked_list(self, list_node):
        res = ''

        while list_node != None:
            res += str(list_node.val)
            list_node = list_node.next
        
        return res



