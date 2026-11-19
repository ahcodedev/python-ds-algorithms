from src.data_structures.singly_linked_list_node import SinglyLinkedListNode
from src.singly_linked_lists.remove_nth_node_from_list import remove_nth_from_end


def test_remove_nth_from_end():
    head = SinglyLinkedListNode(1)
    assert remove_nth_from_end(head, 1) is None

    head = SinglyLinkedListNode(1)
    head.next = SinglyLinkedListNode(2)
    nth_node = remove_nth_from_end(head, 2)
    assert nth_node is not None
    assert nth_node.data == 2

    nth_node = remove_nth_from_end(head, 1)
    assert nth_node is not None
    assert nth_node.data == 1

    head = SinglyLinkedListNode(1)
    head.next = SinglyLinkedListNode(2)
    head.next.next = SinglyLinkedListNode(3)
    head.next.next.next = SinglyLinkedListNode(4)
    nth_node = remove_nth_from_end(head, 2)
    assert nth_node is not None
    assert nth_node.next is not None
    assert nth_node.next.next is not None
    assert nth_node.next.next.data == 4
