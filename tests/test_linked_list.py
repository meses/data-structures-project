"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest
from src.linked_list import LinkedList, Node

class TestNode(unittest.TestCase):

    def test_init(self):
        n1 = Node('abc')
        self.assertEqual(n1.data, 'abc')

class TestQueue(unittest.TestCase):

    def test_init(self):
        ll = LinkedList()
        self.assertEqual(ll.head, None)
        self.assertEqual(ll.tail, None)

    def test_add_beginning(self):
        ll = LinkedList()
        ll.insert_beginning('data1')
        self.assertEqual(ll.head.data, 'data1')
        ll.insert_beginning('data2')
        self.assertEqual(ll.head.data, 'data2')
        self.assertEqual(ll.tail.data, 'data1')
        ll.insert_beginning('data3')
        self.assertEqual(ll.head.data, 'data3')

    def test_add_at_end(self):
        ll = LinkedList()
        ll.insert_at_end('data1')
        self.assertEqual(ll.head.data, 'data1')
        ll.insert_at_end('data2')
        self.assertEqual(ll.head.data, 'data1')
        self.assertEqual(ll.tail.data, 'data2')
        ll.insert_at_end('data3')
        self.assertEqual(ll.head.data, 'data1')
        self.assertEqual(ll.tail.data, 'data3')

    def test_str(self):
        ll = LinkedList()
        ll.insert_at_end('data1')
        ll.insert_at_end('data2')
        ll.insert_at_end('data3')
        ll.insert_beginning('data0')
        self.assertEqual(str(ll), " data0 -> data1 -> data2 -> data3 -> None")

    def test_get_data_by_id(self):
        ll = LinkedList()
        ll.insert_at_end({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
        ll.insert_beginning({'id': 0, 'username': 'serebro'})
        self.assertEqual(ll.get_data_by_id(2), {'id': 2, 'username': 'mik.roz'})
        self.assertEqual(ll.get_data_by_id(0), {'id': 0, 'username': 'serebro'})
        self.assertEqual(ll.get_data_by_id(4), None)


    def test_to_list(self):
        ll = LinkedList()
        ll.insert_at_end({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
        ll.insert_beginning({'id': 0, 'username': 'serebro'})
        self.assertEqual(ll.to_list(), [{'id': 0, 'username': 'serebro'},
                                        {'id': 1, 'username': 'lazzy508509'},
                                        {'id': 2, 'username': 'mik.roz'},
                                        {'id': 3, 'username': 'mosh_s'}])
