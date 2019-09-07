# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return "%s->%s" % (self.val, self.next)


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        previous = head
        current = previous.next
        previous.next = None

        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp

        return previous
