class Node:
    """Класс для узла стека"""
    '''
    def __init__(self, data):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next_node

    def setData(self, new_data):
        self.data = new_data

    def setNext(self, new_next_node):
        self.next_node = new_next_node

    '''
    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node



class Stack:
    """Класс для стека"""

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
        pass

    @property
    def top(self):
        return self.head

    @property
    def data(self):
        return self.data
