"""
[[ 단지번호붙이기 ]]

시간 제한	메모리 제한	    제출	정답	    맞힌 사람	정답 비율
1 초	    128 MB	    174768	    77700	    49333	    42.341%

문제
<그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다.
철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 
여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다.
대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 
지도를 입력하여 단지수를 출력하고,각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.


입력
첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

출력
첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

예제 입력 1 
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000

예제 출력 1 
3
7
8
9
"""

"""
1. 아이디어 : 연결된 집의 집합을 단지라고 정의하고, 그 단지의 개수와 크기를 구해 오름차순으로 정렬해서 출력하는 프로그램을 작성.
            방문하지 않은 좌표를 찾아 그 주변에 연결된 부분을 탐색하는 문제이므로, 그래프 탐색 알고리즘을 사용.
            그 중에서 DFS를 재귀함수로 사용. 좌표를 탐색해 방문 여부를 확인하고, 그 값이 1이면 DFS 탐색 시작.

2. 시간복잡도 : DFS의 시간복잡도는
                O(V+E)
                = 5*V
                = 5*N^2 ( 여기서, N이 충분히 크다면 상수는 무시할 수 있다. )
                = N^2
                = 25*25
                = 625     <<    ( 컴퓨터 연산 속도 == 초당 2억개 )
                알고리즘 사용 가능.

3. 자료 구조 : 단지 지도를 입력 받을 2차원 배열. 방문 여부를 확인할 2차원 배열.
                DFS 탐색 후 결과를 담을 list.
"""

import sys

input = sys.stdin.readline

N = int(input())

# 오답1 : 개행문자 등의 불필요한 입력을 걷어내기 위해, strip()을 사용한다.
#household_map = [list(map(int, input().split())) for _ in range(N)]
household_map = [list(map(int, input().strip())) for _ in range(N)]
check = [[False] * N for _ in range(N)]

result_list = []
num_household = 0

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
def dfs(i, j):
    global num_household
    num_household += 1

    for idx in range(4):
        temp_y = i + dy[idx]
        temp_x = j + dx[idx]

        if 0<=temp_y<N and 0<=temp_x<N:
            if check[temp_y][temp_x] == False:
                check[temp_y][temp_x] = True
                if household_map[temp_y][temp_x] == 1:
                    dfs(temp_y, temp_x)                    
# 오답 2 : list에 append 위치 부적절.
#    result_list.append(num_household)


# 오답3 : range(N) 미사용.
#for i in N:
#    for j in N:
for i in range(N):
    for j in range(N):
        if check[i][j] == False:
            check[i][j] = True
            if household_map[i][j] == 1:
                num_household = 0
                dfs(i, j)
# 오답 2 : list에 append 위치 부적절.
                result_list.append(num_household)


result_list.sort()

print(len(result_list))
for element in result_list:
    print(element)


"""
그런데 생각해보니 전제가 잘못되지 않았나?
우선 방문 여부 False를 확인하고,
True로 무조건 바꿔 준 다음에 해당 좌표가 1인지 0인지 판단해야 하는 것 아닌가?
이러면 방문했지만 1이 아니라서 True로 바꾸지 않은 좌표들이 생길 것 같은데...?
"""