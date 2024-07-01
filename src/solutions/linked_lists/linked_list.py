from loguru import logger


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_start(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            current_head = self.head
            current_head.prev = new_node
            new_node.next = current_head
            self.head = new_node

    def insert_end(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            current_tail = self.tail
            current_tail.next = new_node
            new_node.prev = current_tail
            self.tail = new_node

    def insert_next(self, existing_node: Node, value: int):
        new_node = Node(value)

        if existing_node is None:
            raise ValueError("Unable to proceed with none node")

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            return

        if existing_node.next is None:
            existing_node.next = new_node
            new_node.prev = existing_node
            self.tail = new_node
        else:
            existing_node.next = new_node
            new_node.prev = existing_node

    def insert_previous(self, existing_node: Node, value: int):
        new_node = Node(value)

        if existing_node is None:
            raise ValueError("Unable to proceed with none node")

        if self.head is None:
            self.head = new_node
        if self.tail is None:
            self.tail = new_node

        if existing_node.prev is None:
            existing_node.prev = new_node
            new_node.next = existing_node
            self.head = new_node
        else:
            current_previous = existing_node.prev

            current_previous.next = new_node
            existing_node.prev = new_node

            new_node.prev = current_previous
            new_node.next = existing_node

    def list_snapshot(self):
        current_node: Node = self.head

        if current_node is None:
            print("List is empty")
            return

        current_value: int = current_node.value
        message: str = f"{current_value}"
        current_node: Node = current_node.next

        while current_node is not None:
            message = f"{message} -> {current_node.value}"
            current_node = current_node.next

        return message


def test_linked_list():
    linked_list = LinkedList()

    logger.info("\nInserting values into the linked list")
    linked_list.insert_start(1)
    linked_list.insert_start(2)
    linked_list.insert_start(3)
    linked_list.insert_start(4)
    linked_list.insert_start(5)

    assert linked_list.list_snapshot() == "5 -> 4 -> 3 -> 2 -> 1"

    linked_list.insert_end(6)
    linked_list.insert_end(0)
    linked_list.insert_end(0)
    linked_list.insert_end(3)
    linked_list.insert_end(1)

    assert linked_list.list_snapshot() == "5 -> 4 -> 3 -> 2 -> 1 -> 6 -> 0 -> 0 -> 3 -> 1"

    short_list = LinkedList()
    short_list.insert_start(1)

    assert short_list.list_snapshot() == "1"

    short_list.insert_next(short_list.head, 3)

    assert short_list.list_snapshot() == "1 -> 3"

    short_list.insert_previous(short_list.tail, 2)

    assert short_list.list_snapshot() == "1 -> 2 -> 3"
