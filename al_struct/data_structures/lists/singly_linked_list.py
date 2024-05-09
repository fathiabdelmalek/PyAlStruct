from typing import Any

from al_struct.utils.exceptions import EmptyListException
from al_struct.utils.nodes import Node
from al_struct.data_structures.lists.base_linked_list import BaseLinkedList


class SinglyLinkedList(BaseLinkedList):
    """Singly linked list data structure."""

    def __init__(self):
        """Initialize an empty singly linked list."""
        super().__init__()

    def __str__(self):
        values = []
        temp: Node = self._head
        while temp:
            values.append(str(temp.data))
            temp = temp.next
        del temp
        return " -> ".join(values)

    def __repr__(self):
        return f"PyAlStruct.SinglyLinkedList({str(self)})"

    def prepend(self, data: Any) -> None:
        """
        Add a new node with data to the beginning of the list.
        :param data: The data to be added to the list.
        """
        node: Node = Node(data)
        if self._head is not None:
            node.next = self._head
        self._head = node
        self._size += 1

    def append(self, data: Any) -> None:
        """
        Add a new node with data to the end of the list.
        :param data: The data to be added to the list.
        """
        node: Node = Node(data)
        if not self._head:
            self._head = node
            return
        temp = self._head
        while temp.next:
            temp = temp.next
        temp.next = node
        self._size += 1

    def get_tail(self) -> Any:
        """
        Get data of the last node in the list.
        :return: The data of the last node in the list.
        """
        if not self._head:
            raise EmptyListException()
        temp: Node = self._head
        while temp.next:
            temp = temp.next
        return temp.data
