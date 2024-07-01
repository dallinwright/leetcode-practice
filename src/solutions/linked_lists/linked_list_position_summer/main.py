from src.solutions.linked_lists.linked_list import LinkedList


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


def test_sum_linked_lists():
    first_list = LinkedList()

    first_list.insert_end(1)
    first_list.insert_end(9)

    second_list = LinkedList()
    second_list.insert_end(7)

    summed_result = sum_linked_lists(first_list, second_list)

    assert summed_result.head.value == 8
    assert summed_result.head.next.value == 9
