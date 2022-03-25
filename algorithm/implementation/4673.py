arr = [i for i in range(10001)]

for i in range(1,len(arr)):
    if i < 10:
        arr[2*i] = 0
    elif 10<= i and i< 100:
        arr[i+int(i/10)+int(i%10)] = 0
    elif 100<= i and i < 1000:
        arr[i+int(i/100) + int((i%100)/10) + int((i%100)%10)] = 0
    elif 1000<= i and i < 10001:
        if int(i+i/1000)+int((i%1000)/100)+ int((i%1000)%100/10) + int((i%1000)%100%10) < 10000:
            arr[int(i+i/1000)+int((i%1000)/100)+ int((i%1000)%100/10) + int((i%1000)%100%10)] = 0

arr = list(set(arr))

arr.remove(0)
arr.sort()

for i in range(0,len(arr)-1):
    if arr[i] != 0:
        print(arr[i])