#! python3
import sys
import re

BLUEPRINT_RE = r'Blueprint (\d+)'
ROBOT_RE = r'Each (?P<robot_type>.+?) robot costs (?P<num_1>\d+) (?P<resource_1>[^\s]+)(?: and (?P<num_2>\d+) (?P<resource_2>[^\s]+))?'

class Blueprint:
    def __init__(self, id):
        self.id = id
        self.robots = {}

    def add_bot(self, robot, dependencies):
        self.robots[robot] = dependencies
    
    def calculate_dependency_tree(self):
        tree = {}

        for bot_type, resources in self.robots.items():
            for resource_type, num in resources.items():
                print(bot_type, resource_type, num)


def run_part_1(filename):
    with open(filename, 'r') as file:
        for raw_line in file.readlines():
            line = raw_line.strip()
            (blueprint, robots) = line.split(":")
            match_blueprint = re.match(BLUEPRINT_RE, blueprint)
            blueprint = Blueprint(id=match_blueprint[1])

            for robot in robots.split("."):
                robot = robot.strip()
                if not robot:
                    continue
                match = re.match(ROBOT_RE, robot)
                dependencies = {match.group('resource_1'): int(match.group('num_1'))}
                if match.group('resource_2'):
                    dependencies[match.group('resource_2')] = int(match.group('num_2'))
                blueprint.add_bot(match.group('robot_type'), dependencies)

                # build a dependency tree
                blueprint.calculate_dependency_tree()


            # do something


def run_part_2(filename):
    with open(filename, 'r') as file:
        for raw_line in file.readlines():
            line = raw_line.strip()
            print(".." + line)
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