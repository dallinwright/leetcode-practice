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

    def insert_at_position(self, value, position):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            current_node = self.head
            current_position = 0

            while current_node is not None:
                if current_position == position:
                    new_node.next = current_node
                    new_node.prev = current_node.prev
                    current_node.prev.next = new_node
                    current_node.prev = new_node
                    break

                current_position += 1
                current_node = current_node.next

    def list_snapshot(self):
        current_node = self.head

        if current_node is None:
            print("List is empty")
            return

        message = f"{current_node.value}"
        current_node = current_node.next

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

    linked_list.insert_at_position(0, 1)
    linked_list.insert_at_position(12, 5)
    linked_list.insert_at_position(13, 3)

    assert linked_list.list_snapshot() == "5 -> 0 -> 4 -> 13 -> 3 -> 2 -> 12 -> 1 -> 6 -> 0 -> 0 -> 3 -> 1"
