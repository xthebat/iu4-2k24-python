import some_modeule
from cat.meow import meow

print(some_modeule) 

def main():
    print("what's in a bag?")
    print(__name__)
    meow()

if __name__ == '__main__':
    main()