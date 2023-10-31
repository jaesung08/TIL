# 1101 Introduction of Vue
## Front-end Development
### client-side frameworks
- Front-end Development
  - 웹사이트와 웹 애플리케이션의 사용자 인터페이스(UI)와 사용자 경험(UX)을 만들고 디자인하는 것
  - =>HTML, CSS, JavaScript 등을 활용하여 사용자가 직접 상호작용하는 부분을 개발

- Client-side Frameworks
  - 클라이언트 측에서 UI와 상호작용을 개발하기 위해 사용되는 JavaScript 기반 프레임워크
  - ![1](pict/pict1.png)

- Client-side frameworks가 필요한 이유
  1. 웹에서 하는 일이 많아졌다.
    - 단순히 무언가를 읽는 곳 => 무언가를 하는 곳 
    - 사용자는 이제 웹에서 문서만을 읽는 것이 아닌 음악을 스트리밍하고, 영화를 보고, 원거리에 있는 사람들과 텍스트 및 영상 채팅을 통해 즉시 통신하고 있음
    - 이처럼 현대적이고 복잡한 대화형 웹사이트를 "웹 애플리케이션(web applications)"이라 부름
    - JavaScript 기반의 Client-side frameworks의 출현으로 매우 동적인 대화형 애플리케이션을 훨씬 더 쉽게 구축할 수 있게 됨

  2. 웹에서 하는 일이 많아졌다.
    - 다루는 데이터가 많아졌다
    - 만약 친구가 이름을 변경했다면?
    - 친구 목록, 타임라인, 스토리등 친구 이름이 출력되는 모든 곳이 함께 변경되어야 함
    - 애플리케이션의 기본 데이터를 안정적으로 추적하고 업데이트(텐더링, 추가, 삭제 등)하는 도구가 필요
    - => 애플리케이션의 상태를 변경할 때마다 일치하도록 UI를 업데이트해야 한다는 것!