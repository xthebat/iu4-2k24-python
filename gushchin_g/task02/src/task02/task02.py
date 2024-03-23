import os
import sys

from enum import Enum
from typing import List
from typing import Tuple


class ArgumentsIDs(Enum):
    PATH = 2
    RECURSION = 1


class FSElementsListIDs(Enum):
    PATH = 0
    TYPE = 1


class Indentations(Enum):
    EMPTY = "    "
    END = "└── "
    INTERVAL = "├── "
    VERTICAL = "│   "


class PathsTypes(Enum):
    FILE = 0
    DIRRECTORY = 1


class ScanResultIDs(Enum):
    DIRRECTORIES_COUNT = 1
    FILES_COUNT = 2
    RESULT = 0


class TerminalStyles(Enum):
    BLUE = "\033[34m"
    GREEN = "\033[32m"
    RESSET = "\033[0m"


def generate_indentation(lines: List[bool]) -> str:
    result: str = ""

    for element in lines:
        result = f"{result}{Indentations.VERTICAL.value if element else Indentations.EMPTY.value}"

    return result


def generate_union_list(
    dirnames: List[str], filenames: List[str]
) -> List[List]:  # List[[str, bool]]
    result_list: List[List] = []  # List[[str, bool]]

    for dirname in dirnames:
        result_list.append([dirname, PathsTypes.DIRRECTORY.value])
    for filename in filenames:
        result_list.append([filename, PathsTypes.FILE.value])

    result_list.sort(
        key=lambda arr: arr[FSElementsListIDs.PATH.value], reverse=False
    )  # by name

    return result_list


def get_path(arguments: List[str]) -> str:
    try:
        return arguments[ArgumentsIDs.PATH.value]
    except Exception:
        return ""


def get_reqursion_number(arguments: List[str]) -> int:
    try:
        result = int(arguments[ArgumentsIDs.RECURSION.value])
        if result < 0:
            return 0
        return result
    except Exception:
        return 0


def scan_dirrectory(
    scan_dir_path: str, curr_req: int, lines: List[bool]
) -> Tuple[str, int, int]:  # Tuple[paths, dirs_count, files_count]
    result: str = ""

    indentation = generate_indentation(lines)

    union_list: List[List] = []  # List[[str, bool]]

    directories_count: int = 0
    files_count: int = 0

    for dirpaths, dirnames, filenames in os.walk(scan_dir_path):
        union_list = generate_union_list(dirnames=dirnames, filenames=filenames)
        dirs_count = len(dirnames)

        directories_count = len(dirnames)
        files_count = len(filenames)
        break

    dirrectory_iterator: int = 0
    element_iterator: int = 0
    for element in union_list:
        element_iterator += 1

        name: str = element[FSElementsListIDs.PATH.value]
        name = set_style(
            element[FSElementsListIDs.PATH.value],
            TerminalStyles.BLUE.value
            if element[FSElementsListIDs.TYPE.value] == PathsTypes.DIRRECTORY.value
            else TerminalStyles.GREEN.value,
        )

        if element[FSElementsListIDs.TYPE.value] == PathsTypes.DIRRECTORY.value:
            dirrectory_iterator += 1

        complete_indentation: str = (
            f"{indentation}{Indentations.END.value}"
            if element_iterator == len(union_list)
            else f"{indentation}{Indentations.INTERVAL.value}"
        )

        result = f"{result}{complete_indentation}{name}\n\r"

        if curr_req > 1:
            lines.append(dirrectory_iterator < dirs_count)

            subdirrectory_scan_result: str = scan_dirrectory(
                f"{scan_dir_path}/{element[FSElementsListIDs.PATH.value]}",
                curr_req - 1,
                lines,
            )
            directories_count += subdirrectory_scan_result[
                ScanResultIDs.DIRRECTORIES_COUNT.value
            ]
            files_count += subdirrectory_scan_result[ScanResultIDs.FILES_COUNT.value]
            result = f"{result}{subdirrectory_scan_result[ScanResultIDs.RESULT.value]}"

            lines.pop()

    return result, directories_count, files_count


def set_style(input: str, style: str) -> str:
    return f"{style}{input}{TerminalStyles.RESSET.value}"


def main():
    check_path: str = get_path(sys.argv)
    reqursion: int = get_reqursion_number(sys.argv)

    if reqursion == 0:
        print("ERROR::List of arguments is wrong.")
        exit()

    lines: List[bool] = []

    print(check_path)

    scan_dirrectory_result: Tuple[str, int, int] = scan_dirrectory(
        check_path, reqursion, lines
    )
    print(scan_dirrectory_result[ScanResultIDs.RESULT.value])
    print(
        f"{scan_dirrectory_result[ScanResultIDs.DIRRECTORIES_COUNT.value]} directories",
        end=", ",
    )
    print(f"{scan_dirrectory_result[ScanResultIDs.FILES_COUNT.value]} files")


if __name__ == "__main__":
    main()
