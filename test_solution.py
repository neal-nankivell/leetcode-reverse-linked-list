import solution
import unittest
from solution import ListNode
from typing import List


class Test_TestSolution(unittest.TestCase):
    def setUp(self):
        self.sut = solution.Solution()

    def test_reverseList(self):
        result = self.create_list(
            self.sut.reverseList(self.create_linked_list([1, 2])))

        self.assertEqual(result, [2, 1])

    def create_linked_list(self, list: List[int]) -> ListNode:
        head = ListNode(list[0])

        last = head
        for num in list[1:]:
            last.next = ListNode(num)
            last = last.next

        return head

    def create_list(self, head: ListNode) -> List[int]:
        list = []
        current = head
        while current:
            list.append(current.val)
            current = current.next

        return list


if __name__ == '__main__':
    unittest.main()
