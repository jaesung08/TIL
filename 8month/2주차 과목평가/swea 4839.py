'''
코딩반 학생들에게 이진 탐색을 설명하던 선생님은 이진탐색을 연습할 수 있는 게임을 시켜 보기로 했다.

짝을 이룬 A, B 두 사람에게 교과서에서 각자 찾을 쪽 번호를 알려주면, 이진 탐색만으로 지정된 페이지를 먼저 펼치는 사람이 이기는 게임이다.

예를 들어 책이 총 400쪽이면, 검색 구간의 왼쪽 l=1, 오른쪽 r=400이 되고, 중간 페이지 c= int((l+r)/2)로 계산한다.

찾는 쪽 번호가 c와 같아지면 탐색을 끝낸다.

A는 300, B는 50 쪽을 찾아야 하는 경우, 다음처럼 중간 페이지를 기준으로 왼쪽 또는 오른 쪽 영역의 중간 페이지를 다시 찾아가면 된다.
 
A

B

첫 번째 탐색

l=1, r=400, c=200

l=1, r=400, c=200

두 번째 탐색

l=200, r=400, c=300

l=1, r=200, c=100

세 번째 탐색

l=1, r=100, c=50


책의 전체 쪽수와 두 사람이 찾을 쪽 번호가 주어졌을 때, 이진 탐색 게임에서 이긴 사람이 누구인지 알아내 출력하시오. 비긴 경우는 0을 출력한다.

[입력]
 

첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
테스트 케이스 별로 책의 전체 쪽 수 P, A, B가 찾을 쪽 번호 Pa, Pb가 차례로 주어진다. 1<= P, Pa, Pb <=1000
 

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, A, B, 0 중 하나를 출력한다.
'''


# def binary_search(pages, p):
#     start = 1
#     end = pages

#     while start <= end:
#         mid = (start+end)//2
#         if mid == p :
#             return 1
#         elif mid > p:
#             mid = end -1
#         else :
#             mid = start + 1
#     return 0

def bianry_search(pages, p):
    start = 1
    end = pages
    mid = 0
    cnt = 1
    # 만약 middle이 p와 같다면, 찾는 값 p를 찾은 것이므로 탐색을 종료
    while p != mid:
        mid = (start + end)//2
        if mid > p:
            end = mid
        else:
            start = mid
        cnt += 1
    return cnt


T = int(input())
for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    A = bianry_search(P, Pa)
    B = bianry_search(P, Pb)
    result = ''
    if A == B:
        result = 0
    elif A < B:
        result = 'A'
    else:
        result = 'B'
    print(f'#{tc} {result}')
