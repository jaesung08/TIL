# 칸 갯수와 칸 내용 입력받기
n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

# 갯수를 셀 변수 선언
one = 0
zero = 0
minus_one = 0

# 재귀를 위해 함수로 선언
def search(x, y, k):
    global one, zero, minus_one
    check = paper[x][y]

    for i in range(x, x + k):
        for j in range(y, y + k):
            
            if paper[i][j] != check:
                
                for a in range(3):
                    for b in range(3):
                        search( x + a*k // 3, y + b*k // 3, k//3)
                return
            
    if check == -1:
        minus_one += 1
    elif check == 0:
        zero += 1
    elif check == 1:
        one += 1

search(0, 0, n)
print(minus_one)
print(zero)
print(one)