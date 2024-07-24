str_num = input()
result = int(str_num[0])

for i in range(1, len(str_num)):
    num = int(str_num[i])
    # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기가 아닌 더하기 수행
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)
