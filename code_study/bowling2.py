# A가 특정한 무게의 볼링공을 선택했을때 이어서 B가 볼링공을 선택하는 경우를 차례대로 계산

# n, m = map(int, input().split())
# data = list(map(int, input().split()))

n, m = 5, 3
weight = [1, 3, 2, 3, 2]
# n, m = 8, 5
# weight = [1, 5, 4, 3, 2, 4, 5, 2]

# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11

for x in weight:
    # 각 무게에 당 볼링공의 개수
    array[x] += 1

count = 0

# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m + 1):
    print('step', i, 'A가 무게가', i, '인 공을 선택')
    print('A가 선택할 수 있는 경우의 수 = 무게가', i, '인 볼링공의 개수 = array[i] =', array[i])
    n -= array[i]  # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    print(
        'B가 선택할 수 있는 경우의 수 = 남은 볼링공 중 무게가 i가 아닌 볼링공의 개수 = n - array[i] = ', n)
    count += array[i] * n  # B가 선택하는 경우의 수와 곱하기
    print('step', i, '수행결과 : A가 선택할 수 있는 경우의 수 * B가 선택할 수 있는 경우의수 = ',
          array[i] * n)
    print('현재까지 가능한 총 경우의 수 = ', count, '\n')