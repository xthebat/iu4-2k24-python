import pytest

from task02.tree import get_tree


@pytest.mark.parametrize(
    "path, depth, level_tree, expected",
    [["C:/MLNI/iu4-2k24-python/kovalev_i/task02", 4, 1, ['exsamples of files',
                                                         ['Fezz_Audio_Gratia_04.jpg.lnk',
                                                          'Архив WinRAR.rar',
                                                          'Документ Word.DOCX', 'Докуьент PDF.pdf',
                                                          'Табличка Excel.xlsx'], 'requirements.txt',
                                                         'scripts', [], 'src', ['main.py', 'task02',
                                                                                ['tree.py',
                                                                                 '__init__.py',
                                                                                 '__pycache__',
                                                                                 [
                                                                                     'tree.cpython-311.pyc',
                                                                                     'tree.cpython-38.pyc',
                                                                                     '__init__.cpython-311.pyc',
                                                                                     '__init__.cpython-38.pyc']]],
                                                         'task02.iml', 'test',
                                                         ['test_get_tree.py', '__pycache__',
                                                          [
                                                              'test_get_tree.cpython-311-pytest-8.1.1.pyc']]]],
     ["C:/MLNI/iu4-2k24-python/kovalev_i/task02", 6, 1, ['exsamples of files',
                                                         ['Fezz_Audio_Gratia_04.jpg.lnk',
                                                          'Архив WinRAR.rar',
                                                          'Документ Word.DOCX', 'Докуьент PDF.pdf',
                                                          'Табличка Excel.xlsx'], 'requirements.txt',
                                                         'scripts', [], 'src', ['main.py', 'task02',
                                                                                ['tree.py',
                                                                                 '__init__.py',
                                                                                 '__pycache__',
                                                                                 [
                                                                                     'tree.cpython-311.pyc',
                                                                                     'tree.cpython-38.pyc',
                                                                                     '__init__.cpython-311.pyc',
                                                                                     '__init__.cpython-38.pyc']]],
                                                         'task02.iml', 'test',
                                                         ['test_get_tree.py', '__pycache__',
                                                          [
                                                              'test_get_tree.cpython-311-pytest-8.1.1.pyc']]]],
     ["C:/MLNI/iu4-2k24-python/kovalev_i/task02", 1, 1, ['exsamples of files', 'requirements.txt', 'scripts', 'src',
                                                         'task02.iml', 'test']]
     ]
)
def test_get_tree(path: str, depth: int, level_tree, expected: list):
    assert get_tree(path, depth, level_tree) == expected
    pass
