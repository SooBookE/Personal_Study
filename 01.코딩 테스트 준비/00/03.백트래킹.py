"""
기본문제 : https://www.acmicpc.net/problem/15649

1. 아이디어 :
            백트래킹 재귀함수 안에서, for문을 수행하며 숫자 확인.( 이 때, 방문 여부도 확인하며 수행한다. )
            재귀함수에서 M개를 선택할 경우 출력.

2. 시간복잡도 :
                중복 불가이므로,
                O(N!)
                이고, N은 10까지만 가능.

3. 자료구조 :
            int[] = 결과값 저장.
            bool[] = 방문 여부 확인.

"""

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

rs = []
# rs의 방문 여부를 chk로 찾을 때, chk의 인자 수를 N+1로 채우고 0번 Index를 사용하지 않음으로써
# chk의 Index 참조를 0~(N-1)이 아니라 1~N으로 좀 더 직관적으로 사용하고자 하기와 같이 조치.
#   결론 : 귀찮음 + 직관성을 위한 코드.
chk = [False] * (N+1)


#====================================================하기 백트래킹 알고리즘 2 of 3로 이해해보기!!!!!!!
# 하기부터는 백트래킹의 기본 문제 패턴.
def recur(num):
    if num == M:
        print('\t'.join(map(str, rs)))
        return
    for i in range(1, N+1):
        if chk[i] == False:
            chk[i] = True
            rs.append(i)
            recur(num+1)

            # 하나의 순열을 만들고 계속 다음 순열을 만들어야 하기 때문에
            # 방문 여부의 마지막 요소를 미방문으로 전환.
            # 결과 리스트의 마지막 요소 제거.
            chk[i] = False
            rs.pop()


recur(0)