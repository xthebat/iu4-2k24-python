import os
import pytest
from parse_smd import parse_file


@pytest.mark.parametrize(
    argnames='number_node, number_frames, file',
    argvalues=[
        [85, 1, 'shield_aim_walk_aim_dvert_right.smd'],
        [85, 91, 'a_move_walkNE.smd'],
        [85, 67, 'a_move_runSE.smd'],
        [85, 64, 'a_move_c4_crouchWalkW.smd'],
        [85, 63, 'a_move_c4_crouchWalkSE.smd'],
        [85, 90, 'a_move_knife_align.smd']
    ]
)
def test_parse_file(number_node: int, number_frames: int, file: str) -> None:
    directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources')
    fl, dir_parse, nodes, frames = parse_file(file, directory)
    assert len(nodes) == number_node and len(frames) == number_frames
