# NPM

- pip 랑 동일한 역할 (자바스크립트 패키지 관리자)
  - ex) lodash, axios -> cdn 으로 가져왔었음
  - 전역적으로 설치된 패키지를 관리
  - 현재 프로젝트만 패키지 관리 (nvm: 가상환경)

## npm 명령어

- chat gpt 를 참고하세요
- `npm init`: Node.js 패키지 관리하겠다고 초기화하는 도구
  - package.json 파일이 생성됨
- `npm install`: 패키지를 설치하는 도구
  - package.json, package-lock.json 파일을 확인하여 필요한 패키지를 설치
- `npm install <패키지명>`: 현재 프로젝트에 특정 패키지 추가
- `npm install -g <패키지명>`: 전역 영역에 패키지 추가
- `npm root`: 현재 프로젝트가 참조하고 있는 패키지 목록(node_modules) 확인
- `npm audit`
  - 보안 및 의존성 취약점을 해결하기 위해 도와주는 도구
  - 보안 취약점?
    - 개발자가 악성 코드를 넣어놓으면, 그대로 노출됨
    - 최소한의 보안 취약점을 검사해주기 위해 npm 에서 제공하는 명령어
    - 전래동화
      - 무슨 기준으로 보안 취약점을 검색할까 ?
      - Github 경보(Advistory) DB 를 기준으로 프로젝트 취약점을 분석
      - 해당 DB는 아래와 같은 곳에서 데이터를 가져옴
        - 미국 국립 취약점 DB(The National Vulnerability Database)
        - Github 공개 커밋 취약점 분석 커뮤니티
        - Github 에 보고된 보안 경보
        - npm 에 보안 경보 DB
  - 의존성 문제
    - 현재 프로젝트에 구성된 종속성에 대한 설명과 취약성에 대한 보고
    - 취약한 종속성에 대해 호환 가능한 업데이트를 자동으로 설치
    - [주의사항] audit 명령어는 최소한의 해결법
      - 반드시 개발자가 추가로 확인해주어야 한다.

