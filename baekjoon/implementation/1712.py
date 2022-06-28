if __name__ == "__main__":
    A, B, C = map(int,input().split())
    if C - B <= 0:
        res = -1
    else:
        res = (A // (C - B)) + 1
    print(res)