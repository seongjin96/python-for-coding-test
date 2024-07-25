def solution(s):
    min_len = len(s)
    slice_unit = 1

    # 문자열의 절반 길이가 넘어갈 경우 자를 수 없으므로 절반까지만 진행
    while slice_unit <= (len(s) // 2):
        new_s = ''  # 압축된 문자열
        idx = 0

        # 문자열 길이만큼 탐색
        while idx < len(s):
            count = 0   # 압축된 문자열 개수
            word = s[idx:idx+slice_unit]    # slice_unit 단위로 잘린 문자열

            # 압축시킬 문자열이 있을때까지 탐색
            while word == s[idx:idx+slice_unit]:
                count += 1
                idx += slice_unit

            # 압축된 문자열이 있을 경우 압축된 개수만큼 문자열에 추가
            if count > 1:
                new_s += str(count)
            new_s += word

        # 압축된 문자열의 최소 길이
        min_len = min(min_len, len(new_s))
        slice_unit += 1     # 자를 문자열 단위 증가

    return min_len


print(solution('xababcdcdababcdcd'))
