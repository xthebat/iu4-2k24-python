import date
from additions.add import osIs


def main():
    print(f"Hi bro, it's {date.now}")
    print(f"Date of create this is {date.create_date}")
    osIs()

if __name__ == '__main__':
    main()