from dataclasses import dataclass


@dataclass
class PositionNode:
    """Represents the position of a node at a specific frame.

    Attributes:
        node_id (int): The unique identifier of the node.
        x (float): The x-coordinate of the node's position.
        y (float): The y-coordinate of the node's position.
        z (float): The z-coordinate of the node's position.
        rx (float): The rotation around the x-axis at the node's position.
        ry (float): The rotation around the y-axis at the node's position.
        rz (float): The rotation around the z-axis at the node's position.
    """
    node_id: int
    x: float
    y: float
    z: float
    rx: float
    ry: float
    rz: float


@dataclass
class Frame:
    """Represents a frame of animation.

    Attributes:
        frame_id (int): The unique identifier of the frame.
        positions (List[PositionNode]): A list of PositionNode instances representing node positions in this frame.
    """
    frame_id: int
    positions: list[PositionNode]


@dataclass
class Node:
    """Represents a node in the animation hierarchy.

    Attributes:
        node_id (int): The unique identifier of the node.
        name (str): The name of the node.
        parent_id (int): The node_id of the parent node (-1 if no parent).
    """
    node_id: int
    name: str
    parent_id: int
