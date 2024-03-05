import os


def function_sample(x: int, y: int) -> int:
    return x + y

# putin - path of start (put in)
# depth - depth of tree
# skip - count of space
# return - count of folder for check
# skip_stick - need for delite past stick


def dir_control(putin: str = None, depth: int = 1, skip: int = 0, skip_stick: int = 0) -> int:
    count_folder = 0
    if putin is None:
        putin = os.getcwd()
    dir_cur = os.listdir(putin)

    for dir_str in dir_cur:

        # {'└' * ( 1 if skip > 0 else 0)}

        # write stick
        if dir_str == dir_cur[-1]:
            print(f"{'      ' * skip_stick}{'│     ' * (skip-skip_stick)}└—————{dir_str}")
            skip_stick += 1
        else:
            print(f"{'      ' * skip_stick}{'│     ' * (skip-skip_stick)}├—————{dir_str}")

        dir_str = os.path.join(putin, dir_str)
        if os.path.isdir(dir_str):
            count_folder += 1
            i = depth-1
            if i > 0:
                count_folder += dir_control(dir_str, i, skip+1, skip_stick)

    return count_folder


dir_control("test flobers", 3)
