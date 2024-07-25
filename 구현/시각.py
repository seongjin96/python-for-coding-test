n = int(input())
result = 0

for hour in range(n + 1):
    for minute in range(60):
        for second in range(60):
            # 매 시각 안에 '3'이 포함 되어 있다면 카운트 증가
            if '3' in str(hour) + str(minute) + str(second):
                result += 1

print(result)
