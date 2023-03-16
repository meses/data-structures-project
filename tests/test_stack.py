"""Здесь надо написать тесты с использованием unittest для модуля stack."""

import unittest
from src.stack import Stack, Node

class TestNode(unittest.TestCase):

    def test_init(self):
        n1 = Node('abc', None)
        self.assertEqual(n1.data, 'abc')

class TestStack(unittest.TestCase):

    def test_push(self):
        stack = Stack()
        stack.push('data1')
        self.assertEqual(stack.top.data, 'data1')

        stack.push('data2')
        self.assertEqual(stack.top.next_node.data, 'data1')
        self.assertEqual(stack.top.data, 'data2')

    def test_pop(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        data = stack.pop()
        self.assertEqual(stack.top.data, 'data1')
        self.assertEqual(data, 'data2')

    def test_str(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        self.assertEqual(str(stack), 'data2\ndata1\nNone')




if __name__ == '__main__':
    unittest.main()
