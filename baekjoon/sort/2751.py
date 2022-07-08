def solution(arr):
    # 분할된 배열 길이가 1이면 정렬할 필요X 때문에 return
    if len(arr) <= 1:
        return
    # 중간 인덱스 값을 기준으로 배열을 재귀적으로 두 그룹으로 분할
    mid = len(arr) // 2
    g1 = arr[:mid]
    g2 = arr[mid:]

    solution(g1)
    solution(g2)
    # 두 그룹의 인덱스 값(i1,i2)을 통해 더 작은 값을 배열에 배치(index 변수가 병합될 배열의 인덱스)
    i1 = 0
    i2 = 0
    index = 0
    while i1 < len(g1) and i2 < len(g2):
        if g1[i1] < g2[i2]:
            arr[index] = g1[i1]
            i1 += 1
        else:
            arr[index] = g2[i2]
            i2 += 1
        index += 1
    
    # g1, g2 각 두 그룹에 남아있는 원소를 arr배열에 넣어서 마무리
    while i1 < len(g1):
        arr[index] = g1[i1]
        i1 += 1
        index += 1
    while i2 < len(g2):
        arr[index] = g2[i2]
        i2 += 1
        index += 1

if __name__ == "__main__":
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    
    solution(arr)
    for val in arr:
        print(val)
        