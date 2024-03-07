# import os
# import sys
# import pytest

# sys.path.append('/Users/yaao20u291/Library/Mobile Documents/com~apple~CloudDocs/code/Python/iu4-2k24-python/iu4-2k24-python/yakimov_a/task02')

# from scripts.tree import gen_tree, print_tree

# @pytest.mark.parametrize(
#     argnames="path_depth",
#     argvalues=[
#         open("testpy/file_1.txt")
#     ]
# )

# def test_gen_tree(path_depth):

#     # Создаем список для хранения ожидаемых результатов
#     expected_results = [('/Users/yaao20u291/Documents', 0), ('/Users/yaao20u291/Documents/Микита', 1), ('/Users/yaao20u291/Documents/Микита/Лаб', 2), ('/Users/yaao20u291/Documents/Микита/Семы', 2), ('/Users/yaao20u291/Documents/НИРС', 1), ('/Users/yaao20u291/Documents/Сел_курсач', 1), ('/Users/yaao20u291/Documents/Сел_курсач/5.Паялная станция', 2), ('/Users/yaao20u291/Documents/$RECYCLE.BIN', 1), ('/Users/yaao20u291/Documents/LabVIEW Data', 1), ('/Users/yaao20u291/Documents/LabVIEW Data/LVInternalReports', 2), ('/Users/yaao20u291/Documents/ar_multioreo', 1), ('/Users/yaao20u291/Documents/ar_multioreo/ci', 2), ('/Users/yaao20u291/Documents/ar_multioreo/patches', 2), ('/Users/yaao20u291/Documents/ar_multioreo/etc', 2), ('/Users/yaao20u291/Documents/ar_multioreo/boards', 2), ('/Users/yaao20u291/Documents/ar_multioreo/files', 2), ('/Users/yaao20u291/Documents/ar_multioreo/build', 2), ('/Users/yaao20u291/Documents/ar_multioreo/.git', 2), ('/Users/yaao20u291/Documents/ar_multioreo/.vscode', 2), ('/Users/yaao20u291/Documents/ar_multioreo/OCD', 2), ('/Users/yaao20u291/Documents/ar_multioreo/src', 2), ('/Users/yaao20u291/Documents/National Instruments', 1), ('/Users/yaao20u291/Documents/National Instruments/Circuit Design Suite 14.2', 2), ('/Users/yaao20u291/Documents/resume', 1), ('/Users/yaao20u291/Documents/Other', 1), ('/Users/yaao20u291/Documents/Экономика', 1), ('/Users/yaao20u291/Documents/Леонидов', 1), ('/Users/yaao20u291/Documents/Леонидов/Lab1', 2), ('/Users/yaao20u291/Documents/Леонидов/ДЗ', 2), ('/Users/yaao20u291/Documents/Леонидов/ЛР3', 2), ('/Users/yaao20u291/Documents/Леонидов/ЛР2', 2), ('/Users/yaao20u291/Documents/Леонидов/LEONIDOV', 2), ('/Users/yaao20u291/Documents/Леонидов/STM32LAb', 2), ('/Users/yaao20u291/Documents/Курнос', 1), ('/Users/yaao20u291/Documents/Курнос/ДЗ', 2), ('/Users/yaao20u291/Documents/Курнос/MF500-1558', 2), ('/Users/yaao20u291/Documents/Власов', 1), ('/Users/yaao20u291/Documents/Pyth', 1), ('/Users/yaao20u291/Documents/Pyth/scr', 2), ('/Users/yaao20u291/Documents/Pyth/scripts', 2), ('/Users/yaao20u291/Documents/ИП', 1), ('/Users/yaao20u291/Documents/ИП/DZ_36', 2), ('/Users/yaao20u291/Documents/Arduino', 1), ('/Users/yaao20u291/Documents/Diplom', 1), ('/Users/yaao20u291/Documents/BOOK', 1), ('/Users/yaao20u291/Documents/Dom', 1), ('/Users/yaao20u291/Documents/Сергеева', 1), ('/Users/yaao20u291/Documents/Резчикова', 1), ('/Users/yaao20u291/Documents/Резчикова/TRIZ', 2), ('/Users/yaao20u291/Documents/Резчикова/Курсач_РЕзчикова', 2), ('/Users/yaao20u291/Documents/Blackmagic Design', 1), ('/Users/yaao20u291/Documents/Blackmagic Design/DaVinci Resolve', 2)]

#     # Читаем пути из файла
#     with open(path_depth, "r") as file:
#         for line in file:
#             # Разделяем строку по символу "-"
#             parts = line.strip().split(" - ")

#             # Получаем путь и глубину
#             path = parts[0].strip()
#             depth = int(parts[1].strip())
#             # print(path, depth)

#             # передаем его в функцию gen_tree
#             result = gen_tree(path, depth)

#             #assert result == expected_results
#             assert result


import sys
import pytest

sys.path.append('/Users/yaao20u291/Library/Mobile Documents/com~apple~CloudDocs/code/Python/iu4-2k24-python/iu4-2k24-python/yakimov_a/task02')

from scripts.tree import gen_tree

@pytest.mark.parametrize("path_depth", open("testpy/data_for_test/file_1.txt"))
def test_gen_tree(path_depth):
    path, depth = path_depth.strip().split(" - ")
    result = gen_tree(path, int(depth))
    assert result