from bfs import TreeNode
from collections import deque


def average_of_level(root):
    if root is None:
        return

    queue = deque()
    queue.append(root)
    level_average = []
    while queue:
        size_of_level = len(queue)
        sum_temp = 0

        for _ in range(size_of_level):
            current_node = queue.popleft()
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
            sum_temp += current_node.val
        level_average.append(sum_temp / size_of_level)
    return level_average


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    print("level order average: ", average_of_level(root))


main()
