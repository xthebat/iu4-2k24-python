import calc

print(f"task01.py = {__name__}")


def main():
    print("Hi, im boss of GYM, I call methods from other packages\n")

    print("try get 6300 with help package calc")
    calc.diff(7300, 1000)
    calc.sum(5300, 1000)


if __name__ == '__main__':
    main()