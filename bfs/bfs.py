# Given a binary tree, populate an array to represent its level-by-level traversal. You should populate the values of
# all nodes of each level from left to right in separate sub-arrays.

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right, self.left = None, None


def in_order_traversal(root):
    result = []

    if root is None:
        return result

    queue = deque()
    queue.append(root)

    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            current_node = queue.popleft()
            current_level.append(current_node.val)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        result.append(current_level)

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    print("level order traversal: ", in_order_traversal(root))


if __name__ == "__main__":
    main()
