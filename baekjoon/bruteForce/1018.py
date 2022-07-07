import copy

def chessMake(x,y,bOrW):
    board = copy.deepcopy(arr)
    count = 0
    board[x][y] = bOrW
    if arr[x][y] != board[x][y]:
        count = 1
    for i in range(x, x + 8):
        for k in range(y, y + 8):
            if k == y:
                continue
            if board[i][k] == board[i][k - 1]:
                if board[i][k - 1] == 'B':
                    board[i][k] = 'W'
                else:
                    board[i][k] = 'B'
                count += 1
        if i != x + 7:# 다음 row로 넘어가기 전. row의 첫번째 원소가 그 전 row의 첫번째 원소와 다른지확인
            if board[i + 1][y] == board[i][y]:
                if board[i][y] == 'B':
                    board[i + 1][y] = 'W'
                else:
                    board[i + 1][y] = 'B'
                count += 1
    return count


if __name__ == "__main__":
    n, m = map(int,input().split())
    arr = [[0] * (m +1)]
    min = 2147000000
    # 보드판 입력 
    for i in range(1, n + 1):
        temp = list(input())
        temp.insert(0,0)
        arr.append(temp)
    
    for i in range(1, (n - 8) + 1 + 1):
        for k in range(1, (m - 8) + 1 + 1):
            case1 = chessMake(i,k,'W')
            case2 = chessMake(i,k,'B')
            if case1 <= case2:
                res = case1
            else:
                res = case2
            if min > res:
                min = res
    print(min)