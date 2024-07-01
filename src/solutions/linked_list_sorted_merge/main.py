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

    def print_list(self):
        current_node = self.head
        if current_node is None:
            print("List is empty")
            return

        message = f"{current_node.value}"
        current_node = current_node.next

        while current_node is not None:
            message = f"{message} -> {current_node.value}"
            current_node = current_node.next

        print(message)


def merge_lists(first: LinkedList, second: LinkedList):
    first_list_node = first.head
    second_list_node = second.head
    new_list = LinkedList()

    while first_list_node is not None or second_list_node is not None:
        if first_list_node is None:
            new_list.insert_end(second_list_node.value)
            second_list_node = second_list_node.next
        elif second_list_node is None:
            new_list.insert_start(first_list_node.value)
            first_list_node = first_list_node.next
        else:
            current_tail = new_list.tail








    return new_list


if __name__ == '__main__':
    first_list = LinkedList()

    first_list.insert_end(1)
    first_list.insert_end(3)
    first_list.insert_end(5)
    first_list.insert_end(9)

    second_list = LinkedList()
    second_list.insert_end(1)
    second_list.insert_end(4)
    second_list.insert_end(10)

    first_list.print_list()
    second_list.print_list()

    summed_result = merge_lists(first_list, second_list)
    summed_result.print_list()
