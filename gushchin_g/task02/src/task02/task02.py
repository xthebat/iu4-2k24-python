import sys
from typing import List
from os import walk

PATH_ARGUMNET_ID = 2
REQURSION_ARGUMENT_ID = 1

STYLE_RESSET = "\033[0m"
STYLE_COLOR_BLUE = "\033[34m"

INTEDATION_EMPTY = "    "
INTEDATION_VERTICAL = "|   "
INTEDATION_END = "|-- "

PATH_ID = 0
TYPE_ID = 1


def generate_intedation(lines: List[bool]) -> str:
    answer: str = ""
    append: str = ""

    for element in lines:
        if element is False:
            append = INTEDATION_EMPTY
        else:
            append = INTEDATION_VERTICAL

        answer = f"{answer}{append}"

    append = INTEDATION_END
    answer = f"{answer}{append}"

    return answer


def generate_union_list(
    dirnames: List[str], filenames: List[str]
) -> List[List]:  # List[[str, bool]]
    result_list: List[List] = []  # List[[str, bool]]

    for dirname in dirnames:
        result_list.append([dirname, True])
    for filename in filenames:
        result_list.append([filename, False])

    result_list.sort(key=lambda arr: arr[PATH_ID], reverse=False)  # by name

    return result_list


def get_path(arguments: List[str]) -> str:
    try:
        return arguments[PATH_ARGUMNET_ID]
    except Exception:
        return ""


def get_reqursion_number(arguments: List[str]) -> int:
    try:
        answer = int(arguments[REQURSION_ARGUMENT_ID])
        if answer < 0:
            return 0
        return answer
    except Exception:
        return 0


def scan_dirrectory(scan_dir_path: str, curr_req: int, lines: List[bool]):
    indentation = generate_intedation(lines)

    union_list: List[List] = []  # List[[str, bool]]

    for dirpaths, dirnames, filenames in walk(scan_dir_path):
        union_list = generate_union_list(dirnames=dirnames, filenames=filenames)
        dirs_count = len(dirnames)
        break

    dir_iter: int = 0
    for element in union_list:
        name: str = element[PATH_ID]
        if element[TYPE_ID] is True:
            name = set_style(element[PATH_ID], STYLE_COLOR_BLUE)
            dir_iter += 1
        print(f"{indentation}{name}")

        if curr_req > 1:
            if dir_iter >= dirs_count:
                lines.append(False)
            else:
                lines.append(True)

            scan_dirrectory(f"{scan_dir_path}/{element[PATH_ID]}", curr_req - 1, lines)
            lines.pop()


def set_style(input: str, style: str) -> str:
    return f"{style}{input}{STYLE_RESSET}"


def main():
    check_path: str = get_path(sys.argv)
    reqursion: int = get_reqursion_number(sys.argv)

    if reqursion <= 0:
        exit()

    lines: List[bool] = []

    print(check_path)
    scan_dirrectory(check_path, reqursion, lines)


if __name__ == "__main__":
    main()
