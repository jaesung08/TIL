# 7.17
# 각 형태별 데이터 타입
a1 = 1
a2 = 2.5
a3 = 2 + 3j
a4 = "Hello"
a5 = [1, 2, 3] #리스트
a6 = (1, 2, 'hi') #튜플
a7 = {1, 2, 3, 'hi'} #세트
a8 = {'a':1, 'hi':3, 'hello':5 } #딕셔너리
a9 = True
a10 = range(10)
a11 = None
a12 = lambda x,y : x+y

for i in range(1,13):
    var = f'a{i}'
    var = eval(var)
    print(type(var))

#메모리 주소불러오기
height = 181
print(id(height))
weight = 76
print(id(weight))
weight = 77
print(id(weight))

number = 10
double = 2 * number
print(double)
number = 5
print(double)

def calculate_sum(x, y) :
    return x+y

def calculate_sub(x, y):
    return x - y

char = input()
char = input("문자 한개를 입력하세요")
num = int(input())

char1, char2 = input().split()
#각 정수를 분리해서 받는 함수
num1, num2 = map(int, input().split())
#각 정수를 .을 기준으로 분리해서 받는 함수
year, month, day = map(int, input().split('.')) 
#정수를 받아서 리스트로 저장시킴
num_list = list(map(int, input().split()))
print(num_list)


name = input()
age = int(input())
height = float(input())
# 1. 포맷코드
print("저의 이름은 %s, 나이는 %d, 키는 %.2f"%(name, age, height))
# %s는 문자열, %d는 정수, %.2f는 소수점 둘째자리까지의 실수(.2를 뺴면 여섯째자리까지 나옴)

# 2. f-string
print(f"저의 이름은 {name}, 나이는 {age}, 키는 {height :.2f}")

# 3. .format()
print("저의 이름은 {}, 나이는 {}, 키는 {:.2f}".format(name, age, height))

# 총 3가지의 방법이 있으나 f-string을 가장 유용하게 사용한다.

