import argparse
import os

import pytest

from sem02.syntax_samples import function_sample


@pytest.mark.parametrize(
    "x,y,expected",
    [
        [2, -2, 0],
        [2, 0, 2],
        [100, 500, 600]
    ]
)
def test_function_sample(x: int, y: int, expected: int):
    assert function_sample(x, y) == expected


def test_divide_float():
    value: int = 10
    actual = value / 2
    assert isinstance(actual, float)
    assert actual == 5


def test_divide_int():
    value: int = 10
    actual = value // 2
    assert isinstance(actual, int)
    assert actual == 5


def test_string():
    string = "MEOW.MEOW\r\nGAV.GAV\r\nTEST"
    lines = string.splitlines()
    assert isinstance(lines, list)
    assert lines[0] == "MEOW.MEOW"
    assert lines[1] == "GAV.GAV"
    assert lines[2] == "TEST"

    assert lines[0].split(".")[0] == "MEOW"

    assert "----".join(lines) == "MEOW.MEOW----GAV.GAV----TEST"

    tmp = string.removeprefix("MEOW.MEOW")
    assert tmp == "\r\nGAV.GAV\r\nTEST"

    assert tmp is not string


def test_list():
    lst: list[int] = [100, 200, 300, 400, 500]

    tmp = lst

    lst.remove(300)
    assert lst == [100, 200, 400, 500]

    for it in lst:
        assert isinstance(it, int)

    assert tmp is lst

    assert lst[-1] == 500
    assert lst[2:] == [400, 500]
    assert lst[1:2] == [200]


def test_tuple():
    value_with_two_items: tuple[str, str] = ("a", "b")
    value_with_many_items: tuple[str, ...] = ("a", "b", "c", "b")
    assert value_with_many_items.count("b") == 2


def test_set():
    value: tuple[str, ...] = ("a", "b", "c", "b", "c", "b")
    assert set(value) == {"a", "c", "b"}

    value_set = set(value)

    with pytest.raises(TypeError):
        # noinspection PyUnresolvedReferences
        x = value_set[1]


def test_dict():
    value: dict[str, int] = {
        "Номер": 1,
        "ФИО": 2,
        "Git": 3
    }

    assert value["Git"] == 3

    # keys = list()
    keys = []
    for key in value:
        keys.append(key)

    # value.keys()
    # value.values()
    # value.items()

    assert keys == ["Номер", "ФИО", "Git"]

    for key, number in value.items():
        assert key == "Номер"
        assert number == 1
        break


def test_for():
    values = []
    for number in range(3):
        values.append(number)

    assert values == [0, 1, 2]
    assert list(range(3)) == [0, 1, 2]


def test_while():
    value = [1, 2, 3]
    while len(value) != 0:
        it = value.pop(0)
        print(it)
    assert len(value) == 0


def test_print():
    value = [1, 2, 3]
    print(f"{value=}")
    print(f"value={value}")
    value = 1.32432
    print(f"value={value:.3f}")
    value = 0xDEADBEEF
    print(f"value=0x{value:X} MEOW")
    print(f"value=0x{value:x} MEOW")

    # BAN!
    print(f"value=" + hex(value) + " MEOW")


def explore_directory(is_dir: bool, directories_count: int, files_count: int) -> tuple[list[str], list[str]]:
    if is_dir:
        style = Fore.BLUE
        directories_count += 1
    else:
        style = Fore.GREEN
        files_count += 1

    string = f"{CROWBAR if is_last else T_LEFT} {style}{name}{Style.RESET_ALL}"
    return string, directories_count, files_count


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tree - recursive ls.")
    parser.add_argument(
        "path", type=str, default=os.getcwd(),
        nargs=1, help="Path to directory that will be recursively scanned.")
    parser.add_argument(
        "-d", "--depth", type=int, default=-1,
        nargs=1, help="Maximum depth of tree.")
    args = parser.parse_args()
    path = args.path[0]

    if not os.path.isdir(path):
        parser.error("provided string is not a valid path")

    explore_directory()

    tree.run(path, int(args.depth[0] if isinstance(args.depth, list) else args.depth), sys.stdout)
