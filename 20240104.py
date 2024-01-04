"""
문제 링크 : https://www.acmicpc.net/problem/1926 ( 문제명 : 그림 )

1. 아이디어
- 2중 For문 → 값이 1 && 방문 X 데이터 → BFS 탐색.
- BFS 탐색하면서, 그림 개수 1++, 그림의 최대 넓이 갱신.

2. 시간복잡도
- BFS : O(V+E); 단, 1<=n<=500, 1<=m<=500
- V : m*n ( 입력 데이터 개수 )
- E : V*4 ( 각 Vertex에 연결된 Edge가 2~4. 넉넉하게 4로 계산. )
- O(1,250,000) < ( 컴퓨터 1초 연산 개수 == 2억개 )  →  가능!

3. 자료 구조
- 그래프 전체 지도 : int[][] ( 1, 0으로 이루어진 데이터 배열. → 2차원 배열 사용. )
- 방문 여부 : bool[][] ( 2차원 배열에 해당하는 bool값 2차원 배열 사용. )
- Queue : BFS 알고리즘에 사용.

"""

# 입출력 속도를 높여주는 코드. 습관화하는게 좋음!!!!
import sys
input = sys.stdin.readline
# //입출력 속도를 높여주는 코드. 습관화하는게 좋음!!!!

from collections import deque

n, m = map(int, input().split()) # map()은 첫째 인자로 받은 함수로 뒤에 들어온 List의 요소들을 작업해줌.
                                # 여기서는 input().split()으로 입력 값들을 인자가 str인 List로 만들었고, 이를 int로 변환함.

                                # 의문점 : 예시 데이터가
                                # 6 5
                                # 1 1 0 1 1
                                # 0 1 1 0 0
                                # 0 0 0 0 0
                                # 1 0 1 1 1
                                # 0 0 1 1 1
                                # 0 0 1 1 1
                                # 인데 어떻게 n, m으로 행렬의 값이 들어갔지??
                                
"""                             
                                아니면 그건가?
                                1. 파일 실행 후 스크립트 언어답게, 한 줄씩 실행이 된다.
                                2. input() 함수를 만나면 입력값이 들어오기 전까지 실행을 일시 정지한다.
                                3. 입력 값을 줄 단위로 끊어서 받는다. 예시 데이터에서는 "6 5"를 받으면 코드를 다시 재개한다.
                                4. n, m = map(int, input().split()) 작업으로 "6 5"를 각각 n과 m에 할당한다.
                                5. 이후 변수 map 작업 시, n만큼 for문을 구동하므로, n행 만큼의 줄을 입력 받아 처리한다.

                                이러면 납득이 되지!                                
"""
map = [list(map(int, input().split())) for _ in range(n)]

"""
파이썬의 for문은 이렇게 활용도 가능한 듯.
for문 앞에 수행할 구문을 작성해서, 리스트( [] )에 반복적으로 값이 들어가도록 하는 구문.
"""

chk = [[False]*m for _ in range(n)]

"""
변수 chk의 출력값이 어떻게 되는 거지?
각각의 변수를 print()로 출력해봐야 정확한 이해가 가능할 듯...
"""

# 외워라..?
# 각각 [우측, 하단, 좌측, 상단]의 방향 조합.
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(y, x):
    result = 1 # 그림 사이즈 초기값
    queue = deque()
    queue.append((y, x))
    while queue:
        ey, ex = queue.popleft()
        for k in range(4): # 동서남북 4방을 탐색.
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny<n and 0<=nx<m:
                if map[ny][nx] == 1 and chk[ny][nx] == False:
                    result += 1
                    chk[ny][nx] == True
                    queue.append((ny, nx))

    return result

cnt = 0 # 그림 개수
max_v = 0 # 그림 최대 크기

for j in range(n):
    for i in range(m):
        if map[j][i] == 1 and chk[j][i] == False:
            # BFS로 그림 개수, 크기 탐색
            # 각 결과값 갱신.
            # 방문 여부 갱신.
            chk[j][i] = True
            cnt += 1
            max_v = max(max_v, bfs(j, i))


print(cnt)
print(max_v)