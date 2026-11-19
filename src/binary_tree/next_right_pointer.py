from collections import deque


class Node[T]:
    """Binary tree node with an extra `next` pointer to its right neighbor at the same level."""

    def __init__(self, value: T):
        self.value: T = value
        self.left: Node[T] | None = None
        self.right: Node[T] | None = None
        self.next: Node[T] | None = None


def next_right_pointer[T](root: Node[T] | None) -> Node[T] | None:
    """Next Right Pointer.

    You are given a perfect binary tree where all leaves are on the same level, and every parent has
    two children. Populate each next pointer to point to its next right node. If there is no next
    right node, the next pointer should be set to `None`.

    Breadth-first traverses level by level, linking each node's `next` pointer to its right sibling.
    """
    if not root:
        return root

    level: deque[Node] = deque([root])

    while level:
        right = None

        for _ in range(len(level)):
            left = level.pop()
            if left:
                left.next = right
            right = left
            if left.right:
                level.appendleft(left.right)
            if left.left:
                level.appendleft(left.left)

    return root
