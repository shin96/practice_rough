from bfs import TreeNode
from collections import deque


# Given a binary tree and a node, find the level order successor of the given node in the tree.
# The level order
# successor is the node that appears right after the given node in the level order traversal.

def level_order_succesor(root, val):
    if root is None:
        return None

    queue = deque()
    queue.append(root)

    while queue:
        current_node = queue.popleft()

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

        if current_node.val == val:
            break
    return queue[0].val if queue else None


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(100)

    print("level_order_succesor: ", level_order_succesor(root, 1))


if __name__ == '__main__':
    main()
