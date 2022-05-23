hour, minute = map(int,input().split())

time = int(input())

updateMinute = minute + time
if updateMinute >= 60:
    hour = hour + (updateMinute // 60)
    updateMinute = updateMinute % 60
    if hour > 23:
        hour = hour - 24

print(hour,end=' ')
print(updateMinute,end='')