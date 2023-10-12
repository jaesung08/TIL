-- Table 구조 확인
PRAGMA table_info('examples');

-- `cid`
-- cid는 "Column ID"를 의미하는 컬럼
-- 각 컬럼의 고유한 식별자를 나타내는 정수 값
-- 일반적으로 cid 컬럼은 사용자가 직접 사용하지 않으며, 
-- PRAGMA table_info() 명령과 같은 메타데이터 조회 작업에서 컬럼의 정보를 식별하는 데 사용

-- 1. Create a table
CREATE TABLE examples (
  ExamId INTEGER PRIMARY KEY AUTOINCREMENT,
  LastName VARCHAR(50) NOT NULL,
  FirstName VARCHAR(50) NOT NULL
);

-- 2. Modifying table fields
-- 2.1 ADD COLUMN
ALTER TABLE 
  examples
ADD COLUMN
  Country VARCHAR(100) NOT NULL;
 
-- sqlite는 단일 문을 사용하여 한번에 여러 열을 추가하는 것을 지원하지 않음
ALTER TABLE examples
ADD COLUMN Age INTEGER NOT NULL;

ALTER TABLE examples
ADD COLUMN Address VARCHAR(100) NOT NULL;

-- 2.2 RENAME COLUMN
ALTER TABLE examples
RENAME COLUMN Address TO PostCode;

-- 2.3 DROP COLUMN
ALTER TABLE examples
DROP COLUMN PostCode;

-- 2.4 RENAME TO
ALTER TABLE examples
RENAME TO new_examples;

-- 3. Delete a table
DROP TABLE new_examples;
DROP TABLE examples;

-- sqlite는 컬럼 수정 불가
-- 대신 테이블의 이름을 바꾸고, 새 테이블을 만들고 데이터를 새 테이블에 복사하는 방식을 사용
