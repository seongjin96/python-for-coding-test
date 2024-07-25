s = input()

result = []
num = 0

for alpha in s:
    # 숫자일 경우 더하기
    if alpha.isdigit():
        num += int(alpha)
    # 알파벳인 경우 결과 리스트에 삽입
    else:
        result.append(alpha)

# 알파벳 오름차순 정렬
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if num != 0:
    result.append(str(num))

# 리스트를 문자열로 변환하여 출력
print(''.join(result))
