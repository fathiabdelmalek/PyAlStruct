from al_struct.utils.nodes import Node


class SinglyLinkedList:
    def __init__(self):
        self._head = None

    def __str__(self):
        values = []
        tmp = self._head
        while tmp:
            values.append(str(tmp.data))
            tmp = tmp.next
        del tmp
        return " -> ".join(values)

    def __repr__(self):
        return f"SinglyLinkedList({str(self)})"

    def __len__(self):
        size = 0
        tmp = self._head
        while tmp:
            size += 1
            tmp = tmp.next
        return size

    def __iter__(self):
        self._current = self._head
        return self

    def __next__(self):
        if self._current:
            current = self._current
            self._current = self._current.next
            return current.data
        else:
            raise StopIteration

    def __del__(self):
        self._head = None


if __name__ == '__main__':
    linked_list = SinglyLinkedList()
    linked_list._head = Node(1)
    second = Node(2)
    third = Node(3)
    linked_list._head.next = second
    second.next = third

    print("Singly Linked List:", linked_list)
    print("Length:", len(linked_list))

    # Iterating through the linked list
    for node_data in linked_list:
        print("Node data:", node_data)

    del linked_list
