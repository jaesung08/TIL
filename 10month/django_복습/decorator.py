# 데코레이터 함수
# 메인 로직(func함수)를 감싸주는 새로운 함수를 만든다.
def my_decoratior(func):
    def wrapper():
        print("전처리")
        func()
        print("후처리")
    return wrapper

@my_decoratior
def myFunc3():
    print("myFunc3")


myFunc3()

###

is_logined = False

def my_decoratior(func):
    def wrapper():
        if not is_logined:
            print("로그인 하시오.")
        func()
        print("후처리")
    return wrapper

@my_decoratior
def myFunc3():
    print("myFunc3")


myFunc3()

# 로그인하지 않으면, default 경로로 보내버림
# default : accounts/login/
# @login_required