import pdb
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def print_(self):
        l = self
        while(l):
            print l.val,
            l = l.next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result_list = ListNode((l1.val+l2.val)%10)
        c = (l1.val+l2.val)/10
        l1, l2 = l1.next, l2.next
        result_node = result_list
        while(l1 or l2 or c==1):
            val1, l1 = (0, None) if l1 is None else (l1.val, l1.next)
            val2, l2 = (0, None) if l2 is None else (l2.val, l2.next)
            tmp_node = ListNode((val1 + val2 + c)%10)
            c = (val1 + val2 + c)/10
            result_node.next = tmp_node
            result_node = tmp_node
        return result_list

l1 = ListNode(1)

l2 = ListNode(9)
l2.next = ListNode(9)

rl = Solution().addTwoNumbers(l1, l2)
rl.print_()