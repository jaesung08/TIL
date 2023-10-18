-- 1정규화
-- 중복값 제거
-- 이름, 직업, 능력, 국적, 소속회사, 나이, 가입날짜

-- 이 중 다중값이 발생할 수 있는 필드(능력)를 다른 테이블로 분해함

-- DROP TABLE superhero;

-- CREATE TABLE superhero (
--   id INTEGER PRIMARY KEY,
--   이름 TEXT NOT NULL,
--   직업 TEXT,
--   능력 TEXT,
--   국적 TEXT,
--   소속회사 TEXT,
--   나이 INTEGER,
--   가입날짜 DATE
-- );

-- 1. 1NF - 다중값제거
-- 1.1 능력 테이블 따로 만들기
-- HERO -> 여러 능력을 가짐, 한 능력 -> 여러 HREO 에게 갈 수 있음
-- M:N 이다! 외래키를 어디에 두지 ?
-- 정석 -> 중계 테이블을 만들어야 한다.

-- 중계 테이블 예시
CREATE TABLE superhero (
    id INTEGER PRIMARY KEY,
    name TEXT
);

CREATE TABLE power (
    id INTEGER PRIMARY KEY,
    ability TEXT
);

CREATE TABLE superhero_power (
    superhero_id INTEGER,
    power_id INTEGER,
    FOREIGN KEY (superhero_id) REFERENCES superhero(id),
    FOREIGN KEY (power_id) REFERENCES power(id),
    PRIMARY KEY (superhero_id, power_id)
);

-- 그렇지만... 너무 정석적인 건 힘든걸 ?
-- power 에 중복이 있어도 괜찮지 않을까 ?
DROP TABLE power; 
CREATE TABLE power (
    id INTEGER PRIMARY KEY,
    hero_id INTEGER,
    능력 TEXT,
    FOREIGN KEY (hero_id) REFERENCES hero(id)
);

----------------------------------

-- 2. 2NF - 종속관계 없애기

-- 2.1 2NF - 국적 테이블 만들기
-- DROP TABLE country; # 나중에 편하게 삭제하라고 작성된 코드
CREATE TABLE country (
    id INTEGER PRIMARY KEY, 
    국적 TEXT
);

-- 2.2 2NF - 소속회사 테이블 만들기
-- DROP TABLE company;
CREATE TABLE company (
    id INTEGER PRIMARY KEY, 
    소속회사 TEXT
);

-- 2.3 2NF - 직업 테이블 만들기
-- DROP TABLE job;
CREATE TABLE job (
    id INTEGER PRIMARY KEY,
    직업 TEXT
);

----------------------------------

-- 3. 3NF - '나이' 속성은 직업, 소속 회사, 국적 속성과는 독립적으로 존재하는 속성
-- 그러므로 나이 테이블을 분리하는 것이 좋음
-- 독립적인 속성을 쉽게 생각하는 방법
--  -> 슈퍼 히어로의 나이가 중요한가 ? 우리 나라 소속으로, 나를 도와 줄 수 있도록 그냥 쎄기만 하면 되는거 아닌가 ?
--  -> 즉, 함께 조회할 경우가 많이 없겠구나 -> 독립 속성인가를 고려하면 된다.

-- 나이 테이블 만들기
-- 나이 테이블에 외래키가 있는 이유
-- age 를 테이블로 분리하려면 hero 의 모든 레코드를 age 테이블과 1:1 로 매핑해야함
-- hero 테이블에 외래키를 넣으면 기존 것과 크게 다를바가 없음
-- DROP TABLE age;
CREATE TABLE age (
    id INTEGER PRIMARY KEY,
    hero_id INTEGER,
    나이 INTEGER,
    FOREIGN KEY (hero_id) REFERENCES hero(id)
);

----------------------------------

-- 4. 저장하기

-- 히어로만 따로 있는 테이블 만들기
-- DROP TABLE hero; # 나중에 편하게 삭제하라고 작성된 코드
CREATE TABLE hero (
    id INTEGER PRIMARY KEY,
    이름 TEXT NOT NULL,
    가입날짜 DATE,
    job_id INTEGER,
    company_id INTEGER,
    country_id INTEGER,
    FOREIGN KEY (job_id) REFERENCES job(id),
    FOREIGN KEY (company_id) REFERENCES company(id),
    FOREIGN KEY (country_id) REFERENCES country(id)
);

-- 기존 테이블에서 데이터 가져오기
INSERT INTO country(국적)
SELECT DISTINCT 국적
FROM superhero;

INSERT INTO company(소속회사)
SELECT DISTINCT 소속회사
FROM superhero;

INSERT INTO job(직업)
SELECT DISTINCT 직업
FROM superhero;

INSERT INTO age(hero_id, 나이)
SELECT id, 나이
FROM superhero;

-- hero 테이블에 저장하기 위해서는 외래키로 참조한 테이블의 데이터를 모두 넣어두어야 한다.
INSERT INTO hero (id, 이름, 가입날짜, job_id, company_id, country_id)
SELECT hero.id, hero.이름, hero.가입날짜,
    CASE WHEN hero.직업 = '영웅' THEN 1 ELSE 2 END AS job_id,
    CASE
        WHEN hero.소속회사 = '마블' THEN 1
        WHEN hero.소속회사 = 'DC' THEN 2
        WHEN hero.소속회사 = '저스티스 리그' THEN 3
    END AS company_id,
    CASE
        WHEN hero.국적 = '미국' THEN 1
        WHEN hero.국적 = '아스가르드' THEN 2
        WHEN hero.국적 = '러시아' THEN 3
        WHEN hero.국적 = '왜곡의 나라 와칸다' THEN 4
        WHEN hero.국적 = '아틀란티스' THEN 5
        WHEN hero.국적 = '아마조니아' THEN 6
        WHEN hero.국적 = '크립톤' THEN 7
        WHEN hero.국적 = '영국' THEN 8
        WHEN hero.국적 = '애포콜립스' THEN 9
        WHEN hero.국적 = '아즈라엘' THEN 10
        WHEN hero.국적 = '카하지아' THEN 11
        WHEN hero.국적 = '잉글랜드' THEN 12
        WHEN hero.국적 = '스페인' THEN 13
        WHEN hero.국적 = '독일' THEN 14
        WHEN hero.국적 = '캐나다' THEN 15
        WHEN hero.국적 = '완다' THEN 16
        WHEN hero.국적 = '그리스' THEN 17
        WHEN hero.국적 = '케냐' THEN 18
    END AS country_id
FROM superhero as hero;

----------------------------------

-- JOIN 해보기

-- 눈으로 확인하기 힘드니까 테스트를 위해 데이터 몇 개만 수정함

-- [사전준비] JOIN 을 테스트 하기 위해 랜덤으로 NULL 값을 넣음
UPDATE hero SET 가입날짜 = NULL WHERE id = 10;
UPDATE hero SET 가입날짜 = NULL WHERE id = 20;
UPDATE hero SET 가입날짜 = NULL WHERE id = 25;
UPDATE hero SET job_id = NULL WHERE id = 30;
UPDATE hero SET job_id = NULL WHERE id = 40;
UPDATE hero SET job_id = NULL WHERE id = 50;
UPDATE hero SET company_id = NULL WHERE id = 64;
UPDATE hero SET company_id = NULL WHERE id = 75;
UPDATE hero SET company_id = NULL WHERE id = 88;
UPDATE hero SET country_id = NULL WHERE id = 16;
UPDATE hero SET 치country_id = NULL WHERE id = 46;
UPDATE hero SET country_id = NULL WHERE id = 57;

-- CROSS JOIN: 두 테이블의 모든 가능한 조합을 선택함
-- -> 결과 개수는 두 테이블의 행의 개수를 곱한 개수

SELECT * from hero;
SELECT * from job;

-- 5. hero, job 테이블 CROSS JOIN
SELECT hero.id, hero.이름, job.직업, hero.가입날짜
FROM hero, job;

-- INNER JOIN: 두 테이블에서 일하는 값을 가진 행들만 선택
-- 6. hero, job 테이블 INNER JOIN
SELECT hero.id, hero.이름, job.직업, hero.가입날짜
FROM hero, job
WHERE hero.job_id = job.id;

-- 6.1 권장 방식
-- DB 종류에 따라 성능이 더 좋을 수 있음
-- 가독성, 유지보수 등의 이유로 더 권장되는 INNER JOIN 방식
SELECT hero.id, hero.이름, job.직업, hero.가입날짜
FROM hero
INNER JOIN job
ON hero.job_id = job.id;

-- [연습] 6.2 hero, power 테이블 INNER JOIN
SELECT hero.id, hero.이름, power.능력
FROM hero, power
WHERE hero.id = power.hero_id;

-- 6.3 테이블명 생략하기
-- 앞의 hero 는 두 테이블 모두가 가진 컬럼이라 명시를 해줘야한다.
-- 한 쪽에만 가진 컬럼은 테이블 명 생략해도 됨
SELECT hero.id, 이름, 직업, 가입날짜 FROM hero
INNER JOIN job
ON hero.job_id = job.id;

-- LEFT JOIN: 왼쪽 테이블의 모든 행과 오른쪽 테이블에서 일치하는 값을 가진 행을 선택
-- 일치하는 값이 없는 경우에는 NULL 값을 가짐
-- 7. hero, country 테이블 LEFT JOIN
SELECT hero.id, 이름, 국적 FROM hero
LEFT JOIN country
ON hero.country_id = country.id;

-- 7.1 INNER JOIN 처럼 구현하기
--  (NULL 값 삭제하기)
SELECT hero.id, 이름, 국적 FROM hero
LEFT JOIN country
ON hero.country_id = country.id
WHERE country_id IS NOT NULL;

----------------------------------

-- SQLITE 에는 RIGHT JOIN 과 FULL OUTER JOIN 지원안한다!
-- 성능 이슈: right join과 full outer join은 두 개의 테이블을 모두 스캔해야 하기 때문에 성능 이슈가 발생할 가능성이 높습니다.
-- 구현 복잡도: right join과 full outer join은 inner join과 left join보다 구현이 복잡합니다. 따라서 SQLite에서는 단순한 구현을 유지하기 위해 이 두 가지 join을 지원하지 않습니다.
-- ANSI SQL 표준 이슈: SQLite는 ANSI SQL 표준을 따르고 있습니다. 그러나 ANSI SQL 표준에서 right join과 full outer join을 선택적으로 지원하기 때문에 SQLite에서는 이 두 가지 join을 지원하지 않는 것으로 결정되었습니다.
-- 참고: mysql 은 FULL OUTER JOIN 지원 안함
-- 참고2: oricle 은 다 해 줌

-- [참고] 다른 DB 에서는 아래와 같이 사용함
SELECT hero.id, 이름, 직업, 가입날짜 FROM hero
RIGHT JOIN job
ON hero.job_id = job.id;

SELECT hero.id, 이름, 직업, 국적
FROM hero
FULL OUTER JOIN country
ON hero.country_id = country.id;

-- 8. FULL OUTER JOIN 구현 방법
SELECT hero.*, job.*
FROM hero
LEFT JOIN job
    ON hero.job_id = job.id
UNION
SELECT hero.*, job.*
FROM job
LEFT JOIN hero
    ON hero.job_id = job.id;

-- 3개의 테이블 조회하기
-- 9. hero 의 id 와 이름, 직업과 소속회사를 조회하여라.
--      (단, NULL 값을 제거)
-- [방법1] WHERE 조건문 2번 사용하기
-- [방법2] JOIN 2번 사용하기

SELECT hero.id, hero.이름, job.직업, company.소속회사
FROM hero, job, company
WHERE hero.job_id = job.id 
    AND hero.company_id = company.id;

SELECT hero.id, hero.이름, job.직업, company.소속회사
FROM hero
    INNER JOIN job
    ON hero.job_id = job.id
    INNER JOIN company
    ON hero.company_id = company.id;