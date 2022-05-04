test_case = int(input())
result = []
apartment = [[]]
def f(k,n,apartment):
    total = 0
    if k > 0:
        for i in range(k):
            for room in range(1,n+1):
                total += apartment[i][room]
                apartment[i+1][room] = total
            total = 0
        return apartment[k][n]

for i in range(test_case):
    floor_k = int(input())
    room_n = int(input())
    apartment = [[i for i in range(room_n+1)] for i in range(floor_k+2)]
    result.append(f(floor_k,room_n,apartment))


for i in result:
    print(i)