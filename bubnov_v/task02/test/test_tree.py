import os
import sys
import pytest
from structure import create_structure, remove_structure
from task02.src.tree import create_tree, output_tree, total_number_element


@pytest.mark.parametrize(
    argnames='dir_name, level, file_answer, structure',
    argvalues=[
        ['dir_1', 1, '1.txt', ['dir_1', ['dir_x', 'main.py', 'add.py'], ['request', 'ask.py'], 'hello', 'world']],
        ['dir_1', 2, '2.txt', ['dir_1', ['dir_x', 'main.py', 'add.py'], ['request', 'ask.py'], 'hello', 'world']],
        ['dir_2', 1, '3.txt', ['dir_2', 'structure.py', 'test_main.py', ['test_tree'], 'KO', 'OK', 'NOBODY']],
        ['dir_2', 2, '4.txt', ['dir_2', 'structure.py', 'test_main.py', ['test_tree'], 'KO', 'OK', 'NOBODY']],
        ['dir_3', 3, '5.txt',
         ['dir_3', ['dir_new_1', ['dir_new_2', ['dir_new_3', 'newWORLD', 'openWORLD', 'createWORLD'],
                                  ['dir_new_4', 'HELLO', 'case.py', 'start.py', 'newest.txt']]]]],
        ['dir_3', 4, '6.txt',
         ['dir_3', ['dir_new_1', ['dir_new_2', ['dir_new_3', 'newWORLD', 'openWORLD', 'createWORLD'],
                                  ['dir_new_4', 'HELLO', 'case.py', 'start.py', 'newest.txt']]]]]
    ]
)
def test_total_number_element(dir_name: str, level: int, file_answer: str, structure: list):
    dir_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'test_tree')
    create_structure(dir_path, structure)

    stdout = sys.stdout
    with open('file_output.txt', 'w', encoding='utf-8') as file:
        sys.stdout = file
        path = os.path.join(dir_path, dir_name)
        total_number_element(output_tree(create_tree(path, level), path, False))
    sys.stdout = stdout

    with open('file_output.txt', 'rb') as file_output, open(os.path.join('answer', file_answer), 'rb') as answer:
        assert file_output.read() == answer.read()

    os.remove(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'file_output.txt'))
    remove_structure(dir_path, structure[0])
