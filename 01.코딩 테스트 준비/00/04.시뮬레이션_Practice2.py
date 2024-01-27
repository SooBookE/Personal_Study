"""
[로봇 청소기 동작 방식]
로봇 청소기는 다음과 같이 작동한다.

    1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
    2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
        1. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
        2. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
    3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
        1. 반시계 방향으로 90도 회전한다.
        2. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
        3. 1번으로 돌아간다.

        
[입력 방식]
첫째 줄에 방의 크기 N과 M이 입력된다. (3 <= N, M <= 50)

둘째 줄에 처음에 로봇 청소기가 있는 칸의 좌표 (r, c)와 처음에 로봇 청소기가 바라보는 방향 d가 입력된다. 
d가 0인 경우 북쪽, 1인 경우 동쪽, 2인 경우 남쪽, 3인 경우 서쪽을 바라보고 있는 것이다.
로봇 청소기가 있는 칸은 항상 빈 칸이다.
"""
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
y, x, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

# 북동남서
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
rotate_range = len(dy)

cnt = 0

while 1:
    if room[y][x] == 0:
        room[y][x] = 2
        cnt += 1
    isClean = False
    
    for i in range(1, 5):
        loop = ((d - i) + rotate_range) % rotate_range
        ny = y + dy[loop]
        nx = x + dx[loop]
        if 0<=ny<N and 0<=nx<M:
            if room[ny][nx] == 0:
                d = loop
                y = ny
                x = nx
                isClean = True
                break
    if isClean == False:
        ny = y - dy[d]
        nx = x - dx[d]
        if 0<=ny<N and 0<=nx<M:
            if room[ny][nx] == 1:
                break
            else:
                y = ny
                x = nx
        else:
            break

print(cnt)

"""
총평 : 순서대로 구현하되, 순서를 바꿔서 적용할 때 가독성이 더 좋다면 순서를 교체 후 진행.
        예외 처리를 항상 생각해야하고, 플래그 등을 사용해서 if 문을 구현하는 방식 고려 필요.
        문제 내에서 방향 탐색 요구를 자주하므로, 사용 방식에 익숙해질 필요성 존재.
        배열 내에서 정방향/역방향 탐색하는 방식 기억해둘 것!
"""