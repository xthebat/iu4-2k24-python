class Node:
    """
    Class for nodes
    """

    def __init__(self, id: int, name: str, parent_id: int):
        self.id = id
        self.name = name
        self.parent_id = parent_id


def parse_nodes(filename: str) -> list:
    """
    Function to parse SMD file and to collect all nodes as Classes

    :param filename: Name of the .smd file
    :return: List of Classes
    """
    start_keyword = "nodes"
    end_keyword = "end"
    parsing = False
    nodes = []

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if parsing:
                if line == end_keyword:
                    break
                else:
                    parts = line.split()
                    if len(parts) >= 3:
                        id = int(parts[0])
                        name = parts[1]
                        parent_id = int(parts[2])

                        nodes.append(Node(id, name, parent_id))
            elif line == start_keyword:
                parsing = True

    return nodes


def make_animation_static(filename: str, rewrite: bool = False):
    """
    Changing/Creating SMD file so the animation dont change X and Y coordinates 

    :param  filename: Name of the .smd file
    :param  rewrite: If true - will overwrite original file, otherwise will create new one
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        # print(line)
        if "time" in line:
            new_lines = lines[i + 1].split(" ")
            for b in range(5, 7):
                new_lines[b] = "0.000000"
            lines[i + 1] = " ".join(new_lines)

    with open(filename if rewrite else f"new_{filename}", 'w') as file:
        file.writelines(lines)


if __name__ == "__main__":
    filename = "a_move_c4_walkNE.smd"
    parsed_data = parse_nodes(filename)
    for node in parsed_data:
        print(f"ID: {node.id}, Name: {node.name}, Parent ID: {node.parent_id}")
    make_animation_static(filename)
