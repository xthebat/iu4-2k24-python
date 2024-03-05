import date
from additions.add import os_is


def main():
    print(f"Hi bro, it's {date.now}")
    print(f"Date of create this is {date.create_date}")
    os_is()


if __name__ == '__main__':
    main()
