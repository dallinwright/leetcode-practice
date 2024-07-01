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


def sum_linked_lists(first, second):
    first_list_node = first.head
    second_list_node = second.head

    summed_list = LinkedList()

    while first_list_node is not None or second_list_node is not None:
        first_value = first_list_node.value if first_list_node else 0
        second_value = second_list_node.value if second_list_node else 0

        total = first_value + second_value
        summed_list.insert_end(total)

        if first_list_node:
            first_list_node = first_list_node.next

        if second_list_node:
            second_list_node = second_list_node.next

    return summed_list


if __name__ == '__main__':
    first_list = LinkedList()

    first_list.insert_end(1)
    # first_list.insert_end(0)
    # first_list.insert_end(9)
    first_list.insert_end(9)

    second_list = LinkedList()
    second_list.insert_end(7)
    # second_list.insert_end(3)
    # second_list.insert_end(2)

    first_list.print_list()
    second_list.print_list()

    summed_result = sum_linked_lists(first_list, second_list)
    summed_result.print_list()
