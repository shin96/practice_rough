from unittest import TestCase
from reverse_linked_list import Node


class Test(TestCase):
    def test_node_creation(self):
        node_1 = Node(5)
        self.assertEqual(node_1.value, 5)
        self.assertEqual(node_1.next, None)

    def test_node_reverse(self):
        node_1 = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        node_4 = Node(4)



