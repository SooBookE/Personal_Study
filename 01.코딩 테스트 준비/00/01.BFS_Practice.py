"""
[[ 문제 ]]

그림
시간 제한   메모리 제한     제출	    정답	    맞힌 사람	정답 비율
2 초        128 MB	        37993	    16507	    11451	    42.085%
문제
어떤 큰 도화지에 그림이 그려져 있을 때, 그 그림의 개수와, 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력하여라. 단, 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의하자. 가로나 세로로 연결된 것은 연결이 된 것이고 대각선으로 연결이 된 것은 떨어진 그림이다. 그림의 넓이란 그림에 포함된 1의 개수이다.

입력
첫째 줄에 도화지의 세로 크기 n(1 ≤ n ≤ 500)과 가로 크기 m(1 ≤ m ≤ 500)이 차례로 주어진다. 두 번째 줄부터 n+1 줄 까지 그림의 정보가 주어진다. (단 그림의 정보는 0과 1이 공백을 두고 주어지며, 0은 색칠이 안된 부분, 1은 색칠이 된 부분을 의미한다)

출력
첫째 줄에는 그림의 개수, 둘째 줄에는 그 중 가장 넓은 그림의 넓이를 출력하여라. 단, 그림이 하나도 없는 경우에는 가장 넓은 그림의 넓이는 0이다.

예제 입력 1 
6 5
1 1 0 1 1
0 1 1 0 0
0 0 0 0 0
1 0 1 1 1
0 0 1 1 1
0 0 1 1 1

예제 출력 1 
4
9
"""

"""
[[ 문제 풀이 방식 ]]

1. 아이디어 : 1로 연결되어 있는 덩어리들을 탐색해서, 덩어리들의 개수와 덩어리 크기가 가장 큰 것의 크기를 출력해야 한다.
            도화지를 담을 int형 2차원 배열을 생성해야 한다.
            연결된 덩어리 탐색에는 BFS를 사용해야하고, 이를 위한 Queue가 필요하다.
            한 번 탐색한 곳을 중복 탐색하지 않도록 도화지 크기에 해당하는 bool형 2차원 배열이 필요하다.
            탐색하지 않은 곳이며, 값이 1인 좌표를 찾으면 해당 좌표를 True로 만들고, 해당 덩어리의 사이즈를 1 키운 후 다시
            주변을 탐색해야 한다.

2. 시간 복잡도 : BFS의 시간 복잡도는 O(V+E)이다.
                문제에서
                V = m * n
                E = 4 * V
                따라서,
                V+E = 5(m * n)
                    = 5( 500 * 500 )
                    = 1,250,000
                이며, 컴퓨터의 연산 처리 속도는
                초당 2억개이므로,
                허용 범위 안에 속한다.

3. 자료 구조 : 도화지를 담을 int형 2차원 배열.
                방문 여부를 확인할 도화지 크기만큼의 bool형 2차원 배열.
                BFS 수행을 위한 Queue.
"""

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

picture = [list(map(int, input().split())) for _ in range(n)]

check = [[False] * m for _ in range(n)]


direction_y = [0, 1, 0, -1]
direction_x = [1, 0, -1, 0]

def bfs(i, j):
    queue = deque()
    queue.append((i, j))

    temp_size = 1

    while queue:

        # 오답1 : pop으로 Queue의 Data 꺼내서 사용하지 않음!
        que_y, que_x = queue.popleft()
        for idx in range(4):
            temp_y = que_y + direction_y[idx]
            temp_x = que_x + direction_x[idx]

            # 오답2 : temp_y, temp_x 좌표가 picture의 범위 내인지 확인 안 함!!!
            #         → "예외 처리"를 안 해줬다는 말!
            if 0 <= temp_y < n and 0 <= temp_x < m:
                if check[temp_y][temp_x] == False and picture[temp_y][temp_x] == 1:
                    check[temp_y][temp_x] = True
                    temp_size += 1
                    queue.append((temp_x, temp_y))

    return temp_size


"""
진짜 궁금한게, 이 예제에서는 queue가 쌓일 틈도 없이 들어오면 바로 꺼내서 검사하는데,
그럼 굳이 queue를 쓸 필요가 있는 걸까...?
다른 예제도 이렇게 쓰는 걸까..?
"""


max_size = ea = 0

for i in range(n):
    for j in range(m):
        if picture[i][j] == 1 and check[i][j] == False:
            check[i][j] = True
            ea += 1
            max_size = max(max_size, bfs(i, j))

print(ea)
print(max_size)