#! python3
import sys

# double linked list
class Node:
    def __init__(self, value, previous):
        self.next = None
        self.value = value

        self.prev = previous
        self.next = None
        if previous is not None:
            previous.next = self


    def __repr__(self):
        return f'{self.value}'

    def print_list(self):
        print_node = self
        print_vals = []
        while print_node != self.prev:
            print_vals.append(str(print_node.value))
            print_node = print_node.next
        print_vals.append(str(print_node.value))
        print(', '.join(print_vals))


def run_part_1(filename):
    original_node_list = []
    root = None
    zero = None

    with open(filename, 'r') as file:
        previous = None
        for raw_line in file.readlines():
            line = raw_line.strip()
            node = Node(value=int(line), previous=previous)
            original_node_list.append(node)

            if node.value == 0:
                zero = node

            previous = node
            if not root:
                root = node

        # wrap around
        root.prev = previous
        previous.next = root

    # print("Initial arrangement")
    # root.print_list()
    for node in original_node_list:
        if node.value == 0:
            continue

        insert_at = node
        forward = True if node.value > 0 else False
        for _ in range(0, abs(node.value)):
            if forward:
                insert_at = insert_at.next
            else:
                insert_at = insert_at.prev

        if insert_at != node:
            if node == root:
                root = node.next

        # if forward:
        #     p1 = insert_at.value
        #     p2 = insert_at.next.value
        # else:
        #     p1 = insert_at.prev.value
        #     p2 = insert_at.value

        # remove from links
        old_next = node.next
        old_prev = node.prev
        old_next.prev = old_prev
        old_prev.next = old_next

        # insert new links
        if forward:
            insert_at.next.prev = node
            node.next = insert_at.next
            node.prev = insert_at
            insert_at.next = node
        else:
            insert_at.prev.next = node
            node.prev = insert_at.prev
            node.next = insert_at
            insert_at.prev = node

        # print("")
        # print(f'{node.value} moves between {p1} and {p2}')
        # root.print_list()

    root.print_list()
    # guessed 9663, it's too high
    counter = 0
    node = zero
    coordinates = []
    while counter < 3001:
        if counter % 1000 == 0:
            coordinates.append(node.value)
        node = node.next
        counter += 1
    print(sum(coordinates))





def run_part_2(filename):
    with open(filename, 'r') as file:
        for raw_line in file.readlines():
            line = raw_line.strip()
            warues 
            # do something


if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else None
    if not mode:
        mode == "ax"

    if mode == "ax":
        run_part_1('./example.txt')
    elif mode == "a":
        run_part_1("./input.txt")
    elif mode == "bx":
        run_part_2('./example.txt')
    elif mode == "b":
        run_part_2('./input.txt')