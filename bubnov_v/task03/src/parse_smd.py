import os
import sys
from smd_classes import Node, Frame, PositionNode


def parse_file(filename: str, directory=os.path.dirname(__file__)) -> tuple[str, str, list[Node], list[Frame]]:
    """Parses an SMD (Source Model Data) file and extracts information about nodes and frames.

    Args:
        filename (str): The name of the SMD file to parse.
        directory (str, optional): The directory containing the SMD file. Defaults to the directory of the script.

    Returns:
        tuple: A tuple containing the filename, directory, nodes, and frames extracted from the SMD file.
            - filename (str): The name of the parsed SMD file.
            - directory (str): The directory containing the parsed SMD file.
            - nodes (list): A list of Node instances representing nodes in the SMD file.
            - frames (list): A list of Frame instances representing frames of animation in the SMD file.

    Raises:
        FileNotFoundError: If the specified file cannot be found.
    """
    nodes = []
    frames = []
    full_filename = os.path.join(directory, filename)
    try:
        with open(full_filename, 'rt') as file_smd:
            current_section = None
            for line in file_smd:
                line = line.strip()
                if line.startswith('nodes'):
                    current_section = 'nodes'
                elif line.startswith('skeleton'):
                    current_section = 'skeleton'
                elif line.startswith('end'):
                    current_section = None

                elif current_section == 'nodes':
                    parts = line.split()
                    nodes.append(Node(int(parts[0]), parts[1], int(parts[2])))

                elif current_section == 'skeleton':
                    if line.startswith('time'):
                        frame_id = int(line.split()[1])
                        positions = []
                    else:
                        parts = line.split()
                        node_id = int(parts[0])
                        positions.append(PositionNode(node_id, float(parts[1]), float(parts[2]), float(parts[3]),
                                                      float(parts[4]), float(parts[5]), float(parts[6])))

                        if node_id == len(nodes) - 1:
                            frames.append(Frame(frame_id, positions))
        return filename, directory, nodes, frames

    except FileNotFoundError:
        return filename, directory, nodes, frames


def create_new_smd(old_smd: tuple[str, str, list[Node], list[Frame]]) -> None:
    """Creates a new SMD (Source Model Data) file with modified positions.

    Args:
        old_smd (tuple): A tuple containing the filename, directory, nodes, and frames of the old SMD.
            filename (str): The name of the old SMD file.
            directory (str): The directory where the new SMD file will be saved.
            nodes (list): A list of Node instances representing nodes in the animation.
            frames (list): A list of Frame instances representing frames of animation.

    Returns:
        None

    Prints:
        Creates a new SMD file with modified positions and prints its content.
    """
    filename, directory, nodes, frames = old_smd
    for frame in frames:
        pos = frame.positions[0]
        pos.x = 0.0
        pos.y = 0.0

    new_filename = f'new_{filename}'
    new_directory = os.path.join(directory, 'modified')
    full_filename = os.path.join(new_directory, new_filename)
    try:
        os.mkdir(new_directory)
    except FileExistsError:
        pass

    stdout = sys.stdout
    with open(full_filename, 'wt', encoding='utf-8') as new_smd:
        sys.stdout = new_smd
        print('nodes')
        for node in nodes:
            print(f'  {node.node_id} {node.name} {node.parent_id}')
        print('end')
        print('skeleton')
        for frame in frames:
            print(f'  time {frame.frame_id}')
            for pos in frame.positions:
                print(f'    {pos.node_id}', end=' '),
                print(f'{pos.x:.6f} {pos.y:.6f} {pos.z:.6f}', end=' ')
                print(f'{pos.rx:.6f} {pos.ry:.6f} {pos.rz:.6f}')
        print('end')
    sys.stdout = stdout
