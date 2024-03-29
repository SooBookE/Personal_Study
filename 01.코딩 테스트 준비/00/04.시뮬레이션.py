"""
기본 문제 링크 : https://www.acmicpc.net/problem/14503

특정 조건을 만나기 전까지 while 문으로 반복 작업 실시.
for문으로 4방 탐색 및 이동/청소 작업 실시.


아이디어 :
- 특정 조건( 후진 불가. )을 만족하는 한 계속 반복 작업 → while문 사용. 조건을 만나면 break.
- 4방 탐색 실시 후 작업하지 않은 빈 칸이면 이동. → for문 사용.
- 4방 탐색 후 모두 작업한 칸이면 바라보는 방향 유지한 채로 한 칸 후진 후 작업 반복.
- 후진 불가 시에 while문 종료.

시간복잡도 :
- while문의 최대 수행 시간 = N * M( 방의 크기. )
    컴퓨터의 연산 속도는 초당 2억개. 이 때, 연산을 방의 크기( N * M )만큼 반복 수행하므로
    위와 같이 계산하는 듯.
- 각 칸에서 4방향으로 연산 수행.
→ 최대 시간복잡도 == ( 연산을 수행하는 방의 크기 ) * ( 각 칸에서 연산을 수행하는 방향 )
                == N * M * 4( 변수 N, M을 제외한 상수는 생략 가능. )
                == N * M
                == 50 * 50
                == 2,500       <<      2억개에 해당하므로, 연산 수행 가능.

자료 구조 :
- 방의 전체 지도 : int[][] ( int형 2차원 배열. )
    - 전체 지도에서 벽, 청소 전, 청소 후 공간을 약속된 숫자로 표현하면 새로운 자료 구조를
    사용하지 않아도 된다.
    e.g. 벽, 청소 전, 청소 후를 각각
        1, 0, 2
        로 표시.
- 현재 위치, 방향 : int( y ), int( x ), int( direction )
- 청소한 칸의 개수 : int( cnt )


"""

import sys

input = sys.stdin.readline

N, M = map(int, input().split())                            # 방 크기.
y, x, d = map(int, input().split())                         # 좌표 및 바라보는 방향.
map = [list(map(int, input().split())) for _ in range(N)]   # 방의 정보.
cnt = 0                                                     # 청소한 방의 칸 수.

dy = [-1, 0, 1, 0]  # 북, 동, 남, 서 ( 행의 값. )
dx = [0, 1, 0, -1]  # 북, 동, 남, 서 ( 열의 값. )

# 시뮬레이션 구현.
while 1:   # 특정 조건 만족 시까지 무한 반복.
    if map[y][x] == 0:
        map[y][x] = 2
        cnt += 1
    sw = False  # 청소 후 break문을 수행했는지 확인을 위한 Flag.
    
    for i in range(1, 5):
        ny = y + dy[d-i]
        nx = x + dx[d-i]
        
        # 좌표 탐색 시에는 항상 갱신할 좌표가 지도의 범위에 속하는지 확인.
        if 0<=ny<N and 0<=nx<M:
            if map[ny][nx] == 0:
                # 그 방향으로 회전한 후, 한 칸 전진 후 1번부터 진행한다.
                # 우측의 (d-i)가 -5로 입력되어도 에러가 나지 않도록 아래와 같은 수식 사용.
                d = (d - i + 4) % 4 # (d-i)==-5 일 때, (-1%4) == 3 이므로, Index를 -5로 역행한 값과 동일한 결과 출력.
                                    # 파이썬에서는 배열의 역순으로 인덱스를 찾는 기능이 존재.
                                    # e.g. 크기가 3인 array = []
                                    # array[0] == array[-3]
                                    # array[1] == array[-2]
                                    # array[2] == array[-1]
                                    # 그러나 범위를 초과한 음수 Index는 지원하지 않는다.
                                    # array[-4] != ( array[-1] == array[2] )
                                    # 따라서, 위와 같이 파이썬의 나누기 연산을 통해
                                    # Index를 수정할 필요가 있다.
                """
                근데 굳이 "% 4"를 할 필요가 없는 것 같은데?

                지금 예시에서 i의 범위는 1~4

                d가 0이라 가정했을 때,
                "d-i"가 될 수 있는 값은 -4 ~ -1
                    이 때, "if 0<=ny<N and 0<=nx<M"에서의
                    "d - i + 4"의 값은 0 ~ 3
                d가 3이라 가정했을 때,
                "d-i"가 될 수 있는 값은 -1 ~ 2
                    이 때, "if 0<=ny<N and 0<=nx<M"에서의
                    "d - i + 4"의 값은 3 ~ 6

                아.. % 연산을 해줘야하구나!!!
                """

                # 다음 공부 시에
                # C++과 Python 각각에서 배열의 정방향 순회와 역방향 순회 구현하기 위한 계산 방식 고려해보기!!!
                # → 20240121
                """
                20240125

                arr = [0, 1, 2, 3];
                arr_len = 4;
                이고, 1씩 증감 할 때

                [정방향 순회]
                C++ :
                    int arr[] = {0, 1, 2, 3};
                    int arr_len = sizeof(arr)/sizeof(int);
                    
                    for(int i=0, idx=0; i<8 ; i++){
                        idx = i % arr_len;                                                                          # idx 조작 방식.
                        printf("%d\n", arr[idx]);
                    }

                Python : 
                    arr = [0, 1, 2, 3]
                    arr_len = len(arr)
                    idx = 0
                    loop_len = 8

                    for i in range(loop_len):
                        idx = i % arr_len                                                                           # idx 조작 방식.
                        print(arr[idx])

                [역방향 순회]
                C++ : 
                    int arr[] = {0, 1, 2, 3};
                    int arr_len = sizeof(arr)/sizeof(int);
                    
                    int reverse_idx = 0;
                    
                    // -1이 3이 되도록 조작해야 함. == +4의 배수 하고 %4
                    // 웬만하면 Stable하도록 순회하는 만큼의 수만 곱하던지 고정된 값과 곱하는게 좋을 듯.
                    // → 예를 들어, 여기서는 8
                    for(int i=0, idx=0; i<8; i++, reverse_idx--){
                        // 이렇게 하면 (arr_len * i)가 기하급수적으로 늘어나니까.
                        //idx = (reverse_idx + (arr_len * i)) % arr_len;
                        idx = (reverse_idx + (arr_len * 8/* for문 순회값 */)) % arr_len;                             # idx 조작 방식.
                        printf("%d\n", arr[idx]);
                    }

                Python : 
                    arr = [0, 1, 2, 3]
                    arr_len = len(arr)
                    loop_len = 8
                    reverse_idx = 0
                    idx = 0

                    for i in range(loop_len):
                        reverse_idx -= 1
                        idx = (reverse_idx + (arr_len * loop_len)) % arr_len                                        # idx 조작 방식.
                        print(arr[idx])



                ※ 정방향 순회든, 역방향 순회든, C++이든, Python이든

                    Index = (순회하는 값 + 배열 크기의 배수) % 배열 크기                 단, (순회하는 값 + 배열 크기의 배수)의 합은 양수

                    를 사용하면 의도대로 배열을 순회할 수 있다는 결론 도출.
                """


                """
                ※ 참고 : C와 파이썬에서 음수가 포함된 나누기/나머지 연산 방식은 상이하다.
                        e.g.
                                |c, c++   |python     
                        몫      |-9/3=-3  |-9//3=-3
                                |-8/3=-2  |-8//3=-3
                                |-7/3=-2  |-7//3=-3
                                |9/-3=-3  |9//-3=-3
                                |8/-3=-2  |8//-3=-3
                                |7/-3=-2  |7//-3=-3
                        나머지  |-9%3=0   |-9%3=0
                                |-8%3=-2  |-8%3=1
                                |-7%3=-1  |-7%3=2
                                |9%-3=0   |9%-3=0
                                |8%-3=2   |8%-3=-1
                                |7%-3=1   |7%-3=-2

                ※ 참고2 : 파이썬에서
                            /는 결과값이 float형인 나눗셈 연산자.
                            //는 결과값이 int형인 나눗셈 연산자.
                            를 일컬으며, //는 소수점 아래 값을 모두 버린 정수값을 출력한다.
                """
                y = ny
                x = nx
                sw = True   # 정상적으로 청소를 수행했으면, Flag 전환.
                break

    # 4방향 모두 있지 않은 경우.
    if sw == False:         # 정상적으로 청소를 수행하지 못 했을 경우.
        # 뒤쪽 방향이 막혀있는지 확인.
        ny = y - dy[d]
        nx = x - dx[d]
        if 0<=ny<N and 0<=nx<M:
            if map[ny][nx] == 1:
                break
            else:
                y = ny
                x = nx
        else:
            break

print(cnt)