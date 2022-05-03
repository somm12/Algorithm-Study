from unittest import result


case_num = int(input())
result = []
for i in range(case_num):
    H,W,N = map(int,input().split())
    room_num = (N//H)+1
    floor_num = N%H
    # 맨 꼭대기 층일 경우
    if floor_num == 0:
        floor_num = H
        room_num = (N//H)
    result.append(floor_num*100 + room_num)

for i in result:
    print(i)