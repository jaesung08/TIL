-- SQL문 작성시 주의사항
-- 세미콜론(;) 기준으로 하나의 SQL문 판별

-- 새로운 테이블을 작성
-- id, 이름, 직업, 능력, 국적 소속회사, 나이
-- 필드명, 타입, 제약조건 순으로 작성
-- NOTNULL : 이 필드는 NULL값일 수 없다는 제약조건

CREATE TABLE superheroes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    이름 TEXT NOT NULL,
    직업 TEXT NOT NULL,
    능력 TEXT,
    국적 TEXT,
    소속회사 TEXT,
    나이 INTEGER
);

-- 테이블명 변경하기
-- ALTER TABLE ~~ RENAME TO ~~
ALTER TABLE superheroes
RENAME TO superhero;
-- 한글 이름으로도 가능

-- 새로운 컬럼 추가
-- ALTER TABLE ~~ ADD COLUMN
ALTER TABLE superhero
ADD COLUMN 가입날짜 DATE ;

--

-- 임시컬럼 추가
ALTER TABLE superhero
ADD COLUMN 임시 TEXT;

-- 임시 컬럼 -> 곧 삭제 컬럼
-- ALTER TABLE ~~ RENAME COLUMN ~~ TO ~~
ALTER TABLE superhero
RENAME COLUMN 임시 TO 곧삭제;

-- 곧 삭제 컬럼 삭제
-- ALTER TABLE ~~ DROP COLUMN ~~
ALTER TABLE superhero
DROP COLUMN 곧삭제;
-- DROP이 VS코드 내에서 버전이 맞지않아 제대로 실행되지않음
-- => sqlite3 superhero.sqlite3로 터미널에서 실행하여 명령어 실행 시 잘 작동함

-- 테이블 삭제
ALTER TABLE superhero
DROP TABLE superhero;

-- sqlite3 superhero.sqlite3 (sqlite3 터미널 실행)
-- .mode csv
-- .import superheroes.csv superhero
-- .import (csv파일명) (sqlite명)


