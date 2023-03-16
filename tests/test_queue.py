"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from src.queue import Queue, Node

class TestNode(unittest.TestCase):

    def test_init(self):
        n1 = Node('abc', None)
        self.assertEqual(n1.data, 'abc')

class TestQueue(unittest.TestCase):

    def test_init(self):
        queue = Queue()
        self.assertEqual(queue.head, None)
        self.assertEqual(queue.tail, None)

    def test_enqueue(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')
        self.assertEqual(queue.tail.data, 'data3')
        self.assertEqual(queue.head.data, 'data1')

    def test_str(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')
        self.assertEqual(str(queue), 'data1\ndata2\ndata3')
