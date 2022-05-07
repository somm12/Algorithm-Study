dates = [0,30,28,31,30,31,30,31,31,30,31,30]
day_of_week = ['MON','TUE','WED','THU','FRI','SAT','SUN']
total = 0

month, date = map(int, input().split())
for i in range(1,month):
    total += dates[i]
total += date
index = total % 7
if month == 1:
    index = date % 7
    index = index -1
print(day_of_week[index])
