from bfs import TreeNode
from collections import deque


def find_min_depth(root):
    if root is None:
        return -1

    queue = deque()
    queue.append(root)
    min_depth = 0

    while queue:
        min_depth += 1
        size_of_level = len(queue)

        for _ in range(size_of_level):
            current_node = queue.popleft()
            if current_node.left is None and current_node.left is None:
                return min_depth

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(100)

    # print("what is root", root)
    print("min depth is: ", find_min_depth(root))


if __name__ == "__main__":
    main()
