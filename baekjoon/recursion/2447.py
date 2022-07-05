n = int(input())

def star(l):
    if l == 3:
        return ['***','* *','***']

    arr = star(l//3)
    stars = []

    for i in arr:
        stars.append(i*3)

    for i in arr:
        stars.append(i+' '*(l//3)+i)

    for i in arr:
        stars.append(i*3)

    return stars

print('\n'.join(star(n)))

# n == 9 일 때는 n == 3일 때의 패턴을 기준으로 만들어짐.
# n == 27 일 때는 n == 9일 때의 패턴을 기준으로 만들어짐.
# 각 줄 기준이 되는 패턴을 가지고 크게 3줄로 나누어서 줄바꿈을 가지고 출력.

# for문에서 첫 줄, 마지막 줄은 출력 패턴이 같고, 가운데 부분은 공백이 있기 때문에,
# 2번째 for문은 n // 3 by n //3 로 공백을 만들기 위해서 각 원소 출력시 n // 3 만큼의 공백을 사이로 둔다.