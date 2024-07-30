n = int(input())
dic = {}

for _ in range(n):
    name, score = input().split()
    dic[name] = int(score)

dic = dict(sorted(dic.items(), key=lambda x: x[1]))

for name in dic.keys():
    print(name, end=' ')
