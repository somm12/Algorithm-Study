test_case = int(input())
queue = []
count  = 0
result =[]
for i in range(test_case):
    numOfqueue, index = map(int, input().split())
    element_index = [i for i in range(numOfqueue)]
    queue = list(map(int,input().split()))
    while True:
        a = queue.pop(0)
        if queue == []:
            count +=1
            result.append(count)
            break
        b = max(queue)
        if a < b:
            queue.append(a)
            element_index.append(element_index.pop(0))
        else:
            count += 1
            if element_index[0] == index:
                result.append(count)
                break
            else:
                element_index.pop(0)
    count = 0

for value in result:
    print(value)
