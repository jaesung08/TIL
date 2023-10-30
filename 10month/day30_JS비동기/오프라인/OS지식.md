# OS지식
- 오늘 배울 내용은 "비동기적 처리"
- 동기적 vs 비동기적 / 동시에 일을 처리하는 것은 다른 개념!
- 용어로 적으면 아래와 같다!
- 동기적 : Synchronous, 비동기적 : Asynchrounous, Blocking, Non-Blocking
    - 비슷한 개념이라 혼동할 수 있으니 주의

## 동기적(Synchronous) vs 비동기적(Asynchrounous)
- 순서대로 일이 마치는가 ? 에 대한 여부
- A -> B -> C 함수가 순서대로 호출 되었을 때, 순서대로 끝나는가?
- 즉, 실행순서와 끝나는 순서가 동일한가에 대한 구분

## Blocking vs Non-Blocking
- 동시에 작업을 할 수 있는가 ?
- A -> B 함수를 호출
  - A가 실행되는 도중에 B함수가 아무것도 못하면 Blocking
  - A가 실행되는 도중에 B 함수도 자기 일을 동시에 진행한다면 Non-Blocking

- 예시
```
강사 금기륜이 근영님에게 일을 시키고 밥을 먹으러 가고 싶음
- 강사 입장에서 일이 진행, 밥을 먹는다 ( 두 가지 작업이 존재함 )
- 근영님은 일이 끝나면 강사에게 전화함

1. 일을 시키고 바로 밥을 먹으러 감
    - 일의 진행과 동시에 밥을 먹는 것 ( Non-Blocking )
    1.1 밥을 먹는 중에, 근영님이 일이 끝났다고 전화를 함
        - 끝나는 순서가 동일함 ( Synchronous )
        -> NonBlocking-Synchronous
    1.2 밥을 먹고 와서 일에 대한 결과를 들음
        - 끝나는 순서가 바뀜 ( Asynchrounous )
        -> NonBlocking-Asynchrounous

2. 일이 끝날 때 까지 기다렸다가, 결과를 듣고 밥을 먹으러 감
    - 밥을 동시에 먹지 못함 ( Blocking )
    - 동시에 처리를 못함 -> 끝나는 순서가 무조건 보장
        -> Blocking-Synchronous

- Blocking-Asynchrounous 한 상황은 ?
    - 실제 사례를 생각해 봐도 잘 안떠오름
        -> 개발자의 실수
    - NonBlocking-Asynchrounous 방식을 쓰는데,
        그 과정 중에서 하나라도 Blocking 요소가 존재한다면,
        의도치 않게 Blocking-Asynchrounous 가 발생가능
```