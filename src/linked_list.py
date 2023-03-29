class Node:
    """Класс для узла односвязного списка"""
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:
    """Класс для односвязного списка"""
    def __init__(self, head=None, tail=None):
        """Конструктор класса Queue"""
        self.head = head
        self.tail = tail

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        data = Node(data)
        if self.head is None:
            self.head = self.tail = data
        else:
            data.next_node = self.head
            self.head = data

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        data = Node(data)
        if self.head is None:
            self.head = self.tail = data
        else:
            self.tail.next_node = data
            self.tail = data

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        return ll_string
