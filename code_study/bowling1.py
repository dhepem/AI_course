# 이중 for문
# 차례대로 탐색하면서 중복 제외하여 카운트
# 복잡도가 높다

# n, m = map(int, input().split())  # n : 볼링공의 개수 m : 볼링공의 최대 무게
# weight = list(map(int, input().split()))  # n개의 공의 무게

n, m = 5, 3
weight = [1, 3, 2, 3, 2]
# n, m = 8, 5
# weight = [1, 5, 4, 3, 2, 4, 5, 2]

count = 0

for i in range(n):
    for j in range(i, n):
        if weight[i] != weight[j]:
            count += 1

print(count)
