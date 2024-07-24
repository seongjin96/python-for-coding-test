# 전부 0으로 바꾸는 경우와 전부 1로 바꾸는 경우 중에서 더 적은 횟수를 가지는 경우를 계산

s = input()

idx = 0
zero_count = 0  # 전부 0으로 바꾸는 경우
one_count = 0   # 전부 1로 바꾸는 경우

while idx < len(s):
    # '0'일경우 1이 나올 때까지 인덱스 증가
    if s[idx] == '0':
        while idx < len(s) and s[idx] == '0':
            idx += 1
        # 연속이 끊겼을 경우 횟수 증가
        zero_count += 1
    # '1'일경우 0이 나올 때까지 인덱스 증가
    else:
        while idx < len(s) and s[idx] == '1':
            idx += 1
        one_count += 1

# '0'과 '1'중에서 연속된 숫자가 최소로 나타 났을 경우
print(min(zero_count, one_count))
