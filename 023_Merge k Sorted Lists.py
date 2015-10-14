import pdb

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def print_list(self):
        cursor = self
        while cursor.next:
            print cursor.val, '->',
            cursor = cursor.next
        print cursor.val

class MyHeap(object):
    """docstring for MyHeap"""
    def __init__(self, node_list):
        super(MyHeap, self).__init__()
        self.n = 0
        self.heap = []
        for node in node_list:
            if isinstance(node, ListNode):
                self.insert(node)

    def pop(self):
        if self.n == 0:
            return None
        i, result = 0, self.heap[0]
        self.heap[0] = self.heap[self.n-1]
        self.n -= 1
        while 2*(i+1) < self.n and self.heap[i].val > min(self.heap[2*i+1].val, self.heap[2*i+2].val):
            if self.heap[2*i+1].val < self.heap[2*i+2].val:
                self.heap[i], self.heap[2*i+1] = self.heap[2*i+1], self.heap[i]
                i = 2*i + 1
            else:
                self.heap[i], self.heap[2*i+2] = self.heap[2*i+2], self.heap[i]
                i = 2*i + 2

        if 2*i + 1 == self.n-1 and self.heap[i].val > self.heap[2*i+1].val:
            self.heap[i], self.heap[2*i+1] = self.heap[2*i+1], self.heap[i]
        return result

    def insert(self, element):
        if self.n == len(self.heap):
            self.heap.append(element)
        else:
            self.heap[self.n] = element
        self.n += 1
        i = self.n-1
        if i%2:
            if self.heap[i].val > self.heap[(i-1)/2].val:
                return True
            else:
                self.heap[i], self.heap[(i-1)/2] = self.heap[(i-1)/2], self.heap[i]
                i = (i-1)/2
        while (i-1)/2 >= 0:
            if not i%2:
                i -= 1
            if min(self.heap[i].val, self.heap[i+1].val) >= self.heap[(i-1)/2].val:
                break
            else:
                if self.heap[i].val < self.heap[i+1].val:
                    self.heap[(i-1)/2], self.heap[i] = self.heap[i], self.heap[(i-1)/2]
                else:    
                    self.heap[(i-1)/2], self.heap[i+1] = self.heap[i+1], self.heap[(i-1)/2]
            i = (i-1)/2

        return True

    def get_n(self):
        return self.n
    
    def print_heap(self):
        for i in range(self.n):
            print self.heap[i].val, 
        print 

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head_list = lists[:]
        heap = MyHeap(head_list)
        
        if heap.get_n == 0:
            return None
        head = heap.pop()
        tail = head

        while heap.get_n() > 0:
            if tail.next:
                heap.insert(tail.next)
            tail.next = heap.pop()
            tail = tail.next

        return head

node_lists=[
    [
        ListNode(-1),
        ListNode(1),
    ],
    [
        ListNode(-3),
        ListNode(1),
        ListNode(4),
    ],
    [
        ListNode(-2),
        ListNode(-1),
        ListNode(0),
        ListNode(2),
    ],
]
for node_list in node_lists:    
    for i in range(len(node_list)-1):
        node_list[i].next = node_list[i+1]

head_list = [node_list[0] for node_list in node_lists]

head = Solution().mergeKLists(head_list)
head.print_list()