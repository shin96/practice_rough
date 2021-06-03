from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.right, self.sibling, self.left = None, None, None

    def connect_siblings(self):

        root = self

        queue = deque()
        queue.append(root)
        while queue:
            level_size = len(queue)
            previous_node = None
            for _ in range(level_size):

                current_element = queue.popleft()

                if previous_node:
                    previous_node.sibling = current_element
                previous_node = current_element

                if current_element.left:
                    queue.append(current_element.left)
                if current_element.right:
                    queue.append(current_element.right)

    def print_nodes(self):
        next_level_root = self
        while next_level_root:
            current = next_level_root
            next_level_root = None
            while current:
                print(current.value, end=' ')

                if not next_level_root:
                    if current.left:
                        next_level_root = current.left
                    elif current.right:
                        next_level_root = current.right
                current = current.sibling
            print()


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(100)

    root.connect_siblings()
    print("level_order_succesor: ", root.print_nodes())


if __name__ == '__main__':
    main()
