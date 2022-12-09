#! python3
import sys

from collections import namedtuple

Node = namedtuple('Node', ['name', 'type', 'children', 'parent', 'size'])
class Node(Node):
    def __repr__(self):
        return f'\n   - {self.name} [{self.children} {self.size}]'


def calculate_totals(filename):
    with open(filename, 'r') as file:
        all_lines = [line.strip() for line in file.readlines()]

        commands = []
        current_group = None
        for line in all_lines:
            if line.startswith('$'):
                current_group = []
                if (line.startswith('$ cd')):
                    commands.append({'type': 'cd', 'directory': line[len('$ cd '):]})
                elif (line.startswith('$ ls')):
                    commands.append({'type': 'ls', 'entries': current_group})
            else:
                current_group.append(line)
        
        root = Node(name='root', type='dir', children={}, parent=None, size={'calculated': 0})
        current_node = root
        for command in commands:
            if command['type'] == 'cd':
                directory_name = command['directory']
                if directory_name == '..':
                    current_node = current_node.parent
                    continue

                if directory_name in current_node.children:
                    current_node = current_node.children[directory_name]
                else:
                    new_node = Node(name=directory_name, type='dir', children={}, parent=current_node, size={'calculated': 0})
                    current_node.children[directory_name] = new_node
                    current_node = new_node
            elif command['type'] == 'ls':
                for entry in command['entries']:
                    if entry.startswith('dir'):
                        directory_name = entry[len('dir '):]
                        if directory_name not in current_node.children:
                            current_node.children[directory_name] = Node(name=directory_name, type='dir', children={}, parent=current_node, size={'calculated': 0})
                    else:
                        (size, name) = entry.split()
                        current_node.children[name] = Node(name=name, type='file', children=None, parent=current_node, size=int(size))
        
        totals_per_directory = {}
        def calculate_size(node, breadcrumb):
            if node.type == 'file':
                return node.size

            total = 0
            for child in node.children.values():
                size = calculate_size(child, breadcrumb + ':' + child.name)
                total += size
                if child.type == 'dir':
                    totals_per_directory[breadcrumb + ':' + child.name] = size
            return total        

        calculate_size(root, '')
    return totals_per_directory

def run_part_1(filename):
    totals_per_directory = calculate_totals(filename)
    print(sum([size for size in totals_per_directory.values() if size <= 100000]))


def run_part_2(filename):
    totals_per_directory = calculate_totals(filename)

    MAX_SPACE = 70_000_000

    need_free = 30_000_000
    current_free = MAX_SPACE - totals_per_directory[':/']

    directory_sizes = [size for size in totals_per_directory.values()]
    sorted(directory_sizes)

    for size in directory_sizes:
        if current_free + size > need_free:
            print(size)
            break
        

if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else None
    if not mode:
        mode == "ax"

    if mode == "ax":
        run_part_1('./sample-input.txt')
    elif mode == "a":
        run_part_1("./input.txt")
    elif mode == "bx":
        run_part_2('./sample-input.txt')
    elif mode == "b":
        run_part_2('./input.txt')