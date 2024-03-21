from dataclasses import dataclass


@dataclass
class Node:
    """
    Class for nodes(bones)
    """
    id: int
    name: str
    parent_id: int


@dataclass
class Bone:
    id: int
    x: float
    y: float
    z: float
    x_rot: float
    y_rot: float
    z_rot: float


@dataclass
class Frame:
    time: int
    bones: list[Bone]


def parse_nodes(filename: str) -> list:
    """
    Function to parse SMD file and to collect all nodes(bones)

    :param filename: Name of the .smd file
    :return: List of nodes(bones)
    """

    nodes = []
    start_keyword = "nodes"
    end_keyword = "end"
    parsing = False

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


def parse_animation(filename: str) -> list[Frame]:
    """
    Function to parse animation(frames) from given SMD file

    :param filename: Name of the .smd file
    :return: List of frames
    """

    frames = []
    current_frame_bones = []
    current_frame_time = None
    start_keyword = "skeleton"
    end_keyword = "end"
    parsing = False

    with open(filename, 'r') as file:
        for line in file:

            if parsing:
                if end_keyword in line:
                    frames.append(Frame(time=current_frame_time,
                                  bones=current_frame_bones))
                    break
                else:
                    if "time" in line:
                        if current_frame_time is None:
                            current_frame_time = int(line.split()[1])
                            continue
                        frames.append(
                            Frame(time=current_frame_time, bones=current_frame_bones))
                        current_frame_bones = []
                        current_frame_time = int(line.split()[1])
                    else:
                        data = line.split()
                        x, y, z, x_rot, y_rot, z_rot = map(float, data[1:])
                        bone = Bone(
                            id=int(data[0]), x=x, y=y, z=z, x_rot=x_rot, y_rot=y_rot, z_rot=z_rot)
                        current_frame_bones.append(bone)
            elif start_keyword in line:
                parsing = True
    return frames


def make_animation_static(filename: str, rewrite: bool = False):
    """
    Changing/Creating SMD file so the animation dont change X and Y coordinates 

    :param  filename: Name of the .smd file
    :param  rewrite: If true - will overwrite original file, otherwise will create new one
    """

    with open(filename, 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if "time" in line:
            new_lines = lines[i + 1].split(" ")
            for coordinate in range(5, 7):
                new_lines[coordinate] = "0.000000"
            lines[i + 1] = " ".join(new_lines)

    with open(filename if rewrite else f"new_{filename}", 'w') as file:
        file.writelines(lines)


if __name__ == "__main__":
    filename = "a_move_c4_walkNE.smd"

    parsed_nodes = parse_nodes(filename)
    for node in parsed_nodes:
        print(f"ID: {node.id}, Name: {node.name}, Parent ID: {node.parent_id}")

    parsed_animation = parse_animation(filename)
    for frame in parsed_animation:
        print(f"Frame time: {frame.time}")

    make_animation_static(filename)
