class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self, head=None, tail=None):
        """Конструктор класса Queue"""
        self.head = head
        self.tail = tail

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node


    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if self.head:
            removed = self.head
            self.head = self.head.next_node
            return removed.data
        return None

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        if not self.head:
            return ''
        current = self.head
        result = ''
        while current != self.tail:
            result += current.data
            result += '\n'
            current = current.next_node
        result += current.data
        return result
