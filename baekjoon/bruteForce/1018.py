def chessMake(x,y,bOrW):
    global arr
    count = 0
        
    for i in range(x, x + 8):
        for k in range(y, y + 8):
            if (i + k) % 2 == 0:
                if arr[i][k] != bOrW:
                    count += 1
            else:
                if arr[i][k] == bOrW:
                    count += 1
    return count


if __name__ == "__main__":
    n, m = map(int,input().split())
    arr = []
    min = 2147000000
    first = 0
    # 보드판 입력 
    for i in range(n):
        arr.append(list(input()))
    # 어디를 시작점으로 8 x 8 체스판을 만들 수 있는지 모든 경우를 가져옴   
    for i in range(n - 7):
        for k in range(m - 7):
            # 체스판 가장 왼쪽 위쪽이 흰색이냐 검은색이냐 두 가지 경우
            case1 = chessMake(i,k,'W')
            case2 = chessMake(i,k,'B')
            # 색을 바꿀 수 있는 더 작은 경우의 수를 할당.
            if case1 <= case2:
                res = case1
            else:
                res = case2
            if min > res:
                min = res
    print(min)