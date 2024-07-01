from src.solutions.linked_lists.linked_list import LinkedList, Node


def merge_lists(first: LinkedList, second: LinkedList):
    first_node: Node = first.head
    second_node: Node = second.head
    new_list = LinkedList()

    while first_node is not None or second_node is not None:
        # Gets tricky real fast. If we have no more nodes in a list, since they are sorted we insert the remaining
        # values in the other list.
        if first_node is None:
            new_list.insert_end(second_node.value)
            second_list_node = second_node.next
        elif second_node is None:
            new_list.insert_end(first_node.value)
            first_list_node = first_node.next
        else:
            # We have two values to insert, but no guarantee both values are greater than the current tail value.
            # We need to then go backwards  and then insert.
            current_tail: Node = new_list.tail

    return new_list


def test_merge_lists():
    first_list = LinkedList()

    first_list.insert_end(1)
    first_list.insert_end(3)
    first_list.insert_end(5)
    first_list.insert_end(9)

    assert first_list.print_list() == "1 -> 3 -> 5 -> 9"

    second_list = LinkedList()
    second_list.insert_end(1)
    second_list.insert_end(4)
    second_list.insert_end(10)

    first_list.print_list()
    second_list.print_list()

    summed_result = merge_lists(first_list, second_list)
    summed_result.print_list()
