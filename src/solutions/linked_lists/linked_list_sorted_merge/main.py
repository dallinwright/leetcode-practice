from loguru import logger

from src.solutions.linked_lists.linked_list import LinkedList, Node


def merge_lists(first_list: LinkedList, second_list: LinkedList):
    first_node: Node = first_list.head
    second_node: Node = second_list.head

    while first_node is not None and second_node is not None:
        first_value = first_node.value
        second_value = second_node.value

        if second_value < first_value:
            first_list.insert_previous(first_node, second_value)
            second_node = second_node.next
        else:
            if first_node.next is None and second_node is not None:
                while second_node is not None:
                    first_list.insert_end(second_node.value)
                    second_node = second_node.next
                return first_list

            first_node = first_node.next

    return first_list


def test_merge_lists():
    logger.info("\n")
    logger.info("Merging")
    first_list = LinkedList()

    first_list.insert_end(1)
    first_list.insert_end(3)
    first_list.insert_end(9)

    assert first_list.list_snapshot() == "1 -> 3 -> 9"

    second_list = LinkedList()
    second_list.insert_end(2)
    second_list.insert_end(4)
    second_list.insert_end(10)

    assert second_list.list_snapshot() == "2 -> 4 -> 10"

    logger.info(first_list.list_snapshot())
    logger.info(second_list.list_snapshot())

    summed_result = merge_lists(first_list, second_list)

    logger.info(summed_result.list_snapshot())
