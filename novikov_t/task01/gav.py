def gav(n):
    if (n < 1) or (n > 30):
        print("GAV!")
    else:
        for i in range(n, 1, -1):
            print("gav " * i)
        print(__name__, end='!')