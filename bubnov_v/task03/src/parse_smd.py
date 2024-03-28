import os
from smd_classes import Node, Frame, PositionNode


def parse_file(filename: str, directory: str = os.getcwd()) -> tuple[str, str, list[Node], list[Frame]]:
    """
    Parse an SMD file and return its components.

    Args:
        filename (str): The name of the SMD file.
        directory (str, optional): The directory where the file is located. Defaults to the current working directory.

    Returns:
        tuple[str, str, list[Node], list[Frame]]: A tuple containing filename, directory, nodes, and frames.
    """
    nodes = []
    frames = []
    full_filename = os.path.join(directory, filename)
    try:
        nodes, frames = read_smd(full_filename, nodes, frames)
        return filename, directory, nodes, frames
    except FileNotFoundError:
        return filename, directory, nodes, frames


def read_smd(filename: str, nodes: list[Node], frames: list[Frame]) -> tuple[list[Node], list[Frame]]:
    """
    Read an SMD file and extract nodes and frames.

    Args:
        filename (str): The name of the SMD file.
        nodes (list[Node]): List to store Node objects.
        frames (list[Frame]): List to store Frame objects.

    Returns:
        tuple[list[Node], list[Frame]]: A tuple containing read out nodes and frames.
    """
    with open(filename, 'rt') as file_smd:
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
    return nodes, frames


def create_new_smd(old_smd: tuple[str, str, list[Node], list[Frame]]) -> None:
    """
    Create a new SMD file with modified positions and save it.

    Args:
        old_smd (tuple[str, str, list[Node], list[Frame]]): Tuple containing filename, directory, nodes, and frames.
    """
    filename, directory, nodes, frames = old_smd
    for frame in frames:
        pos = frame.positions[0]
        pos.x = 0.0
        pos.y = 0.0

    new_filename = f'new_{filename}'
    new_directory = os.path.join(directory, 'modified')
    full_filename = os.path.join(new_directory, new_filename)

    check_or_create_directory(new_directory)
    output_smd(full_filename, nodes, frames)


def output_smd(filename: str, nodes: list[Node], frames: list[Frame]) -> None:
    """
    Display nodes and frames to an SMD file.

    Args:
        filename (str): The name of the SMD file to be created.
        nodes (list[Node]): List of Node objects.
        frames (list[Frame]): List of Frame objects.
    """
    with open(filename, 'wt', encoding='utf-8') as new_smd:
        new_smd.write('nodes\n')
        for node in nodes:
            new_smd.write(f'  {node.node_id} {node.name} {node.parent_id}\n')
        new_smd.writelines(['end\n', 'skeleton\n'])
        for frame in frames:
            new_smd.write(f'  time {frame.frame_id}\n')
            for pos in frame.positions:
                new_smd.write(f'    {pos.node_id}')
                new_smd.write(f' {pos.x:.6f} {pos.y:.6f} {pos.z:.6f}')
                new_smd.write(f' {pos.rx:.6f} {pos.ry:.6f} {pos.rz:.6f}\n')
        new_smd.write('end\n')


def check_or_create_directory(dir_name: str) -> None:
    """
    Check if directory exists, create it if not.

    Args:
        dir_name (str): The name of the directory.
    """
    try:
        os.mkdir(dir_name)
    except FileExistsError:
        pass
