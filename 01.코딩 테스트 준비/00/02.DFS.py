"""
※ Reference from 유튜브 "개발자 장고"(https://www.youtube.com/@developer_jango)

1. 아이디어
    2중 for문을 수행하며, 값이 1 && 방문하지 않은 좌표에서 DFS( 재귀 함수 ) 수행.
    총 단지수를 갱신하고, 각 단지 내의 집의 개수를 List에 저장.
    List를 오름차순( Ascending ) 정렬 후 출력.

2. 시간 복잡도
    DFS : O(V+E)
    → O(5*n^2)
    → Big-O Notation에서는 n 등에 곱해진 상수는 무시할 수 있음.
    → O(n^2)
    → O(625)
    는 컴퓨터 연산 처리 속도인 초당 2억개 보다 적은 개수이므로, 처리 가능.

3. 자료 구조
    그래프 저장을 위한 int형 2차원 배열.
    방문 여부 확인을 위한 bool형 2차원 배열.
    단지 내의 집의 개수를 저장할 int형 List.
"""

import sys

input = sys.stdin.readline

N = int(input())

# sys.stdin.readline을 통해 입력을 받으면, 개행문자( \n )도 문자로 입력받기 때문에, 쓸데없는 부분을 쳐내는 ".strip()" 함수를 사용함.
household_map = [list(map(int, input().strip())) for _ in range(N)]
check = [[False] * N for _ in range(N)]

# 단지 내의 집의 개수들을 담을 list 변수.
result = []
# 단지 내의 집의 개수를 담을 int형 변수.
each = 0

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
def dfs(y, x):
    # 함수 안에서 전역 변수를 사용하기 위해 global 키워드 사용.
    global each
    each += 1

    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        
        if 0<=ny<N and 0<=nx<N:
            if household_map[ny][nx] == 1 and check[ny][nx] == False:
                check[ny][nx] = True
                dfs(ny, nx)


for j in range(N):
    for i in range(N):
        if household_map[j][i] == 1 and check[j][i] == False:
            # 방문 체크 표시.
            # DFS로 크기 구하기.
            # 크기를 결과 리스트에 입력.
            check[j][i] = True
            each = 0
            dfs(j, i)
            result.append(each)


result.sort()
print(len(result))
for i in result:
    print(i)
            