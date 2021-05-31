class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, val):
        node_ = Node(val)
        last_node = self.get_last_node()
        if last_node is None:
            self.head = node_
        else:
            last_node.next = node_

    def get_last_node(self):
        temp = self.head
        if temp is None:
            return None
        while temp.next is not None:
            temp = temp.next
        return temp

    def print_nodes(self):

        temp = self.head

        if not temp:
            print("No node available")

        while temp is not None:
            print("node -> ", temp.value)
            temp = temp.next

    def reverse_linked_list(self):
        current = self.head
        previous = None
        i = 0
        while current is not None:
            i += 1
            # print("iteration ", i)
            next_nodes = current.next
            # print("next nodes:", next_nodes)
            current.next = previous
            previous = current
            # print("previous", previous)
            current = next_nodes

        # print(current, "this should come")
        self.head = previous
        return current


class Node:
    def __init__(self, value=None, next_ptr=None):
        self.value = value
        self.next = next_ptr

    def __repr__(self) -> str:
        return super().__repr__()

    def __str__(self) -> str:
        return f'node: {self.value}, next: {self.next}'


def main():
    linked_list = LinkedList()
    linked_list.push(1)
    linked_list.push(2)
    linked_list.push(3)
    linked_list.print_nodes()
    print("reversing the nodes")
    linked_list.reverse_linked_list()
    linked_list.print_nodes()


main()
