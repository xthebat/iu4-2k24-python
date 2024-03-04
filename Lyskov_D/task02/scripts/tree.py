import os


def tree(startPath: str, maxLevel: int):
    for address, dirs, files in os.walk(startPath):
        level = address.replace(startPath, '').count(os.sep)
        if (level < maxLevel):
            indent = '-' * 4 * (level)
            print(f"|{indent}{os.path.basename(address)}/")
            subIndent = '-' * 4 * (level + 1)
            for f in files:
                print(f"|{subIndent}{f}")
