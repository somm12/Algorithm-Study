input_num = int(input())
num = input_num
count = 0

while True:
  #units
  right_digit = num % 10
  #tens
  left_digit = num // 10
  sum_result = left_digit + right_digit
  new_num = right_digit* 10 + sum_result % 10
  num = new_num
  count += 1
  if input_num == new_num:
    break
print(count)