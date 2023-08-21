# 8.2
## 2차원배열
* 1차원 list를 묶어놓은 LIST
* 2차원 이상의 다차원 LIST는 차원에 따라 index를 선언 ( arr[0][0] 식 )
* 2차원 List의 선언 : 세로길이(행의 개수), 가로길이(열의 개수)를 필요로 함
* Python에서는 데이터 초기화를 통해 변수선언과 초기화가 가능함
```
arr=[[0,1,2,3], [4,5,6,7]] (2행 4열의 2차원 List)
 
    1열 2열 3열 4열
1행  0    1    2    3
2행  4    5    6    7
```

#### 참고 
```
3  (3x3행열) 행열이 나뉘어짐 
1    2    3
4    5    6
7    8    9 

N = int(input)
arr = [list(map(int, input().split())) for _ in range (N) ]

3 (3x3행열) 행열이 나누어지지않음 split 차이 
123
456
789

N = int(input)
arr = [list(map(int, input())) for _ in range (N) ]
```

### 2차원 배열의 접근
* 배열순회
    * n X m 배열의 n*m개의 모든 원소를 빠짐없이 조사하는 방법

* 행 우선순회
```py

행→ㅁㅁㅁㅁ
행→ㅁㅁㅁㅁ
행→ㅁㅁㅁㅁ

# i 행의 좌표
# j 열의 좌표
for i in range(n):
    for j in range(m):
        f(Array[i][j])  # 필요한 연산수행
```

* 열 우선순회
```py
열열열열
↓↓↓↓
ㅁㅁㅁㅁ
ㅁㅁㅁㅁ
ㅁㅁㅁㅁ

# i 행의 좌표
# j 열의 좌표
for j in range(m):
    for i in range(n):
        f(Array[i][j])  # 필요한 연산수행
```

* 지그재그 순회
```py
→ㅁㅁㅁㅁ→
←ㅁㅁㅁㅁ←
→ㅁㅁㅁㅁ→

# i 행의 좌표
# j 열의 좌표
for i in range(n):
    for j in range(m):
        f(Array[i][j + (m-1-2*j) * ( i%2 ) ])  # 필요한 연산수행
```


# 델타를 이용한 2차배열 탐색
* 2차 배열의 한 좌표에서 4방향의 인접 배열 요소를 탐색하는 방법
```py
arr[0 ... N-1][0 ... N-1] # nXn 배열
di[ ] <- [0, 1, 0 ,-1]
dj[ ] <- [1, 0, -1, 0]
for i : 0 -> N-1
    for j : 0 -> N-1
         ni <- i + di[k]
         nj <- j + dj[k]
         if 0 <= ni < N and 0 <= nj < N # 유효 인덱스면
                          f(arr[ni][nj])

# di[ ] dj[ ] => [0,1] [1,0] [0, -1] [-1, 0] 로 상하좌우로 이동한다.
```


##### 더미코드
* 디버깅시 실행코드가 없는 경우 dummy code를 중단점으로 활용 

### 전치 행렬
* ![Alt text](<pict1 전치행렬.png>)
