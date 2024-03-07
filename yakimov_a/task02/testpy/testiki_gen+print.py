
import sys
import pytest
from io import StringIO

sys.path.append('/Users/yaao20u291/Library/Mobile Documents/com~apple~CloudDocs/code/Python/iu4-2k24-python/iu4-2k24-python/yakimov_a/task02')

from scripts.tree import gen_tree, print_tree


@pytest.fixture
def captured_output():
    # Захватываем стандартный вывод
    capture = StringIO()
    sys.stdout = capture
    yield capture
    # Восстанавливаем стандартный вывод после завершения теста
    sys.stdout = sys.__stdout__

@pytest.mark.parametrize("path_depth", open("testpy/data_for_test/file_1copy.txt"))
def test_gen_tree(path_depth, captured_output):
    path, depth = path_depth.strip().split(" - ")
    result = gen_tree(path, int(depth))
    assert result

    # Тестируем функцию print_tree
    print_tree(result)
    
    # Получаем захваченный вывод
    output = captured_output.getvalue()
    
    # Проверяем, что вывод соответствует ожидаемому
    expected_output = ("|-- Микита\n  |-- Лаб\n  |-- Семы\n")

    expected_output = expected_output.strip()

    assert output == expected_output





