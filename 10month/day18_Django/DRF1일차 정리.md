# 20231018

## URI(URN) 와 URL

- http://127.0.0.1:8000/articles/index.html   - URI O, URL O
- http://127.0.0.1:8000/articles/index        - URI O, URL X

- URI: 식별자. 즉, 리소스의 이름을 나타냄
- URL: 식별자 + 위치. 즉, 우리가 원하는 자원이 서버의 어디에 있는 지 알려주는 규약

## API 서버란 ?

- DRF: API 서버를 쉽게 만들 수 있도록 도와줌
- Server 종류
  - 웹 서버
    - 정적인 컨텐츠(html, css, 이미지 등)를 제공하기 위한 서버
    - 대표적: Nginx, Apache
  - API 서버
    - 클라이언트가 데이터를 요청하면, 해당 데이터를 제공하기 위한 서버
    - 일반적으로 API 서버는 WAS 위에서 동작
  - WAS(Web Application Server)
    - 동적인 컨텐츠를 제공하기 위한 서버
      - DB 서버, API 서버, 세션 관리, 보안 등을 모두 포함함
    - 이런 것들을 모두 합쳐서 하나의 애플리케이션 실행 환경을 제공하는 서버

- Django 개발 서버
  - 웹 서버, WAS 이런 거 상관없이 그냥 개발 서버
  - 위의 내용들은 모두 배포 시 구분되는 것!
  - 개발 서버와 별개로 생각해야 한다.

- asgi.py, wsgi.py + gunicorn
  - Django 를 WAS로 배포할 수 있도록 도와줌
    - 동적 파일 처리, db 접근 등을 도와줌
  - 정적 파일
    - 일반적으로는 Nginx 등을 활용
    - `python manage.py collectstatic`

## REST API 디자인 가이드

```python
# 예전 버전
urlpatters = [
    path('articles/'),
    path('articles/create/'),
    path('articles/<int:pk>/update/'),
    path('articles/<int:pk>/delete/'),

    # RESTful 하게 구현
    # 1. 자원을 식별만 하자!
    # 2. 그럼 자원의 행동 ?
    #   요청할 때 http method 로 구분하자!
    path('articles/'),
    path('articles/<int:pk>/'),
]
```

- REST API 설계의 가장 중요한 두 가지는 다음과 같다.

1. URI 는 리소스를 표현해야 한다. (리소스명은 동사보다는 명사를 사용)
   - 행위에 대한 표현이 들어가지 말아야 한다.

2. 행위는 HTTP Method 로 표현한다.

```
GET /articles/1/delete/ -> 잘못된 URI 구성
DELETE /articles/1/     -> 자원에 대한 표현 + 행위
```

- 추가적인 몇가지 예시
```
# 전체 출력 시
GET /articles/show/     -> X
GET /articles/          -> O

# 회원 추가 시
GET /articles/create/   -> X
POST /articles/         -> O
```

- REST API 설계 시 몇가지 규칙

1. 슬래시 구분자(/)는 계층 관계를 나타내는데 사용한다.

유저가 __가진__ devices 들 조회: `GET users/{userid}/devices`

2. 하이픈(-)은 URI 가독성을 높이는 데 사용
3. 언더바(_)는 URI에 사용하지 않는다

```
GET users/userexample/  -> X
GET users/userExample/  -> X
GET users/user_example/ -> X
GET users/user-example/ -> O
```

4. URI 에는 소문자를 사용해라
- RFC3986(URI 문법 형식 표준) 대소문자를 구별하도록 규정
  - 대소문자에 따라 다른 리소스로 인식

5. 파일 확장자는 URI 에 포함시키지 않는다
   - Accept header 를 사용하여 확장자를 표현함

```
GET articles/dog.jpg    -> X
GET articles/dog HTTP/1.1 Host: articles Accept: image/jpg  -> O
```

- 수많은 규칙들이 존재해서 정확히 지키기가 너무 어렵다!
  - 많이 공부해야함


# API 의 데이터 전송 방식

- SOAP(Simple Object Access Protocol)
  - XML 데이터 구조
- REST API 와의 차이점

