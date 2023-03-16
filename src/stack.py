class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node



class Stack:
    """Класс для стека"""
    @property
    def top(self):
        return self.head

    @top.setter
    def top(self, data):
        self.head = data
        return self.head


    @property
    def data(self):
        return self.data

    def __init__(self, head=None):
        """Конструктор класса Stack"""
        self.head = head


    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        result = self.top.data
        self.top = self.top.next_node
        return result

    def __str__(self):
        current = self.head
        result = ''
        while current != None:
            result += current.data
            result += '\n'
            current = current.next_node
        result += 'None'
        return result
