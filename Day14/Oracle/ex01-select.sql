/*
파일명 : HR-Day03-Select.sql
SQL (Structured Query Language) - 구조적 질의 언어
    관계형 데이터베이스 시스템(RDBMS)에서 자료를 관리 및 처리하기 위해 설계된 언어
    
SELECT 문
    데이터베이스에서 정보 검색
*/

-- 모든 열 선택 * 
SELECT * 
FROM departments;

-- 특정 열 선택
SELECT department_id, location_id
FROM departments;

/*
산술식
    산술 연산자를 사용하여 숫자/날짜 데이터 표현식 작성
    
    + 더하기
    - 빼기
    * 곱하기
    / 나누기
*/

-- 산술 연산자 사용
SELECT LAST_NAME, SALARY, SALARY + 300
FROM employees;

/* 
연산자 우선순위
    곱하기와 나누기는 더하기 빼기보다는 먼저 수행
*/

SELECT last_name, salary, 12*salary+100
FROM employees;

SELECT last_name, salary, 12*(salary+100)
FROM employees;

/*
산술식의 Null 값
    null 값을 포함하는 산술식은 null로 계산
*/

SELECT last_name, 12*salary*commission_pct, salary, commission_pct
FROM employees;

/*
열 alias 정의 - 별명
    열 머리글의 이름을 바꿉니다.
    계산에서 유용합니다.
    열 이름 바로 뒤에 나옵니다. (열 이름과 alias 사이에 선택 사항인 AS 키워드가 올 수도 있습니다.)
    공백이나 특수 문자를 포함하거나 대소문자를 구분하는 경우 큰 따옴표가 필요합니다.
*/
SELECT last_name AS name, commission_pct comm, salary * 10 as 급여10배
FROM employees;

SELECT last_name "Name", salary*12 "Annual Salary"
FROM employees;

/*
연결 연산자
    열이나 문자열을 다른열에 연결합니다.
    두 개의 세로선(||)으로 나타냅니다.
    결과 열로 문자 표현식을 작성 합니다.
*/ 
SELECT last_name||job_id AS "Employees", last_name, job_id
FROM employees;

/*
리터럴 문자열
    리터럴은 SELECT 문에 포함된 문자, 숫자 또는 날짜입니다.
    날짜 및 문자 리터럴 값은 작은 따옴표로 묶어야 합니다.
    각 문자열은 반환되는 각 행에 한 번 출력됩니다.
*/
SELECT last_name || ' is a ' || job_id AS "Employee Details"
FROM employees;

/*
대체 인용(q) 연산자
    자신의 따옴표 구분자를 지정합니다.
    구분자를 임의로 선택합니다.
    가독성 및 사용성이 증가합니다.
*/
SELECT department_name || q'[ Department's Manager Id: ]' || manager_id
AS "Department and Manager"
FROM departments;


/*
중복행
    기본적으로 query 결과에는 중복 행을 포함한 모든행이 표시됩니다.
DISTINCT 
    결과에서 중복행 제거
*/

-- 중복행
SELECT department_id
FROM employees;

-- 중복제거
SELECT DISTINCT department_id
FROM employees;

/*
테이블 구조표시
    DESCRIBE 명령을 사용하여 테이블 구조를 표시합니다.
*/
DESCRIBE employees;



/*
선택을 사용하여 행 제한
    WHERE 절을 사용하여 반환되는 행을 제한합니다.
WHERE 
    조건을 충족하는 행으로 query를 제한합니다.
    
    세가지 요소
    - 열이름
    - 비교 조건
    - 열 이름, 상수 또는 값 리스트
*/

-- WHERE 절 사용
SELECT employee_id, last_name, job_id, department_id
FROM employees
WHERE department_id = 90;

/*
문자열 및 날짜
    문자열 및 날짜 값은 작은 따옴표로 묶습니다.
    문자 값은 대소문자를 구분하고 날짜 값은 형식을 구분합니다.
    기본 날짜 표시 형식은 DD-MON-RR입니다.
*/
SELECt last_name, job_id, department_id
FROM employees
WHERE last_name = 'Whalen';

SELECT last_name, hire_date
FROM employees
WHERE 1= 1
AND hire_date = '03/06/17'
;

/*
비교 연산자
    특정 표현식을 다른값이나 표현식과 비교하는 조건에서 사용됩니다.
    
    =   같음
    >   보다 큼
    >=  보다 크거나 같음
    <   보다 작음
    <=  보다 작거나 같음
    <>  같지 않음
    BETWEEN ... AND ...     두 값 사이(경계값 포함)
    IN(set)                 값 리스트 중 일치하는 값 검색
    LIKE                    일치하는 문자 패턴 검색
    IS NULL                 NULL 값인지 여부
*/

-- 비교 연산자 사용
SELECT last_name, salary
FROM employees
WHERE salary <= 3000;

-- BETWEEN 연산자를 사용하는 범위 조건
SELECT last_name, salary
FROM employees
WHERE salary BETWEEN 2500 AND 3500;

-- IN 연산자를 사용하는 멤버조건
SELECT employee_id, last_name, salary, manager_id
FROM employees
WHERE manager_id IN (100, 101, 201);

/*
LIKE 연산자를 사용하여 패턴 일치
    LIKE 연산자를 사용하여 유효한 검색 문자열 값의 대체 문자 검색을 수행합니다.
    검색조건에는 리터럴 문자나 숫자가 포함될 수 있습니다.
        - % 는 0개 이상의 문자를 나타냅니다
        - _ 은 한 문자를 나타냅니다.
*/
SELECT first_name
FROM employees
WHERE first_name LIKE 'A%';

-- 대체 문자 결합
SELECT last_name
FROM employees
WHERE last_name LIKE '_o%';

-- ESCAPE 식별자 
SELECT employee_id, last_name, job_id
FROM employees 
WHERE job_id LIKE '%SA\_%' ESCAPE '\';

/*
NULL 조건 사용
    IS NULL 연산자로 null을 테스트 합니다
*/
SELECT last_name, manager_id
FROM employees
WHERE manager_id IS NULL;

/*
논리 연산자를 사용하여 조건정의
    AND : 구성 요소 조건이 모두 참인 경우 TRUE 반환
    OR  : 구성 요소 조건 중 하나가 참인 경우 TRUE 반환
    NOT : 조건이 거짓인 경우 TRUE를 반환합니다.
*/
-- AND 연산자 사용
SELECT employee_id, last_name, job_id, salary
FROM employees
WHERE salary >= 10000
AND job_id LIKE '%MAN%';

-- OR 연산자 사용
SELECT employee_id, last_name, job_id, salary
FROM employees
WHERE salary >= 10000
OR job_id LIKE '%MAN%';

-- NOT 연산자 사용
SELECT last_name, job_id
FROM employees
WHERE job_id NOT IN ('IT_PROG', 'ST_CLERK', 'SA_REP');

/*
ORDER BY 절
    ORDER BY 절을 사용하여 검색된 행을 정렬합니다.
    - ASC : 오름차순, 기본값
    - DESC : 내림차순
    SELECT 문의 맨 마지막에 옵니다.    
*/
SELECT last_name, job_id, department_id, hire_date
FROM employees
ORDER BY hire_date;

-- 내림차순 정렬
SELECT last_name, job_id, department_id, hire_date
FROM employees
ORDER BY hire_date DESC;

-- 열  alias를 기준으로 정렬
SELECT employee_id, last_name, salary*12 annsal
FROM employees
ORDER BY annsal;

-- 열 숫자 위치를 사용하여 정렬
SELECT last_name, job_id, department_id, hire_date
FROM employees
ORDER BY 3;

-- 여러 열을 기준으로 정렬
SELECT last_name, job_id, department_id, salary
FROM employees
ORDER BY department_id, salary DESC;


/*
함수(Function)
    매개변수를 받아 특정 계산(작업)을 수행하고 결과를 반환하는 구조로 되어있습니다.

함수 유형
    - 단일행 함수 - 단일행 매개변수를 받아 결과 값 반환
    - 여러행 함수 - 여러행 매개변수를 받아 결과 값 반환
*/

-- 단일행 함수

/*
대소문자 변환 함수
*/
-- LOWER() 함수 - 소문자로 변환
SELECT employee_id, last_name, department_id
FROM employees
WHERE last_name = 'higgins';

SELECT employee_id, last_name, department_id
FROM employees
WHERE LOWER(last_name) = 'higgins';

-- UPPER() 함수 - 대문자로 변환
SELECT UPPER('higgins') FROM dual;

-- INITCAP() 함수 - 첫글자만 대문자로 변환
SELECT employee_id, last_name, department_id
FROM employees
WHERE last_name = INITCAP('higgins');

/*
문자 조작 함수
*/
-- CONCAT() 함수 - 두개 파라미터 값을 연결합니다.
SELECT 'Hello'||'World' FROM dual;
SELECT CONCAT('Hello', 'World') FROM dual;

-- SUBSTR() - 지정된 길이의 문자열을 추출합니다.
SELECT SUBSTR('HelloWorld', 1, 5) FROM dual;

-- LENGTH() - 문자열 길이를 숫자 값으로 표시합니다.
SELECT LENGTH('HelloWorld') FROM dual;

-- INSTR() - 이름이 지정된 문자의 숫자 위치를 찾습니다.
SELECT INSTR('HelloWorld', 'W') FROM dual;

-- LPAD() - 길이가 n이 되도록 왼쪽부터 문자식으로 채운 표현식을 반환합니다.
SELECT LPAD('salary', 10, '*') FROM dual;

-- RPAD() - 길이가 n이 되도록 오른쪽부터 문자식으로 채운 표현식을 반환합니다.
SELECT RPAD('salary', 10, '*') FROM dual;

-- REPLACE() - 문자열 치환
SELECT REPLACE('JACK and JUE', 'J', 'BL') FROM dual;

-- TRIM() - 문자열에서 선행 문자나 후행 문자를 자릅니다.
SELECT TRIM('H' FROM 'HelloWorld') FROM dual;

/*
숫자 함수
*/
-- ROUND() - 지정된 소수점 자릿수로 값을 반올림 합니다.
SELECT ROUND(45.926, 2) FROM dual;

-- TRUNC() - 지정된 소수점 자릿수로 값을 truncate 합니다.
SELECT TRUNC(45.926, 2) FROM dual;

-- MOD() - 나눈 나머지를 반환 합니다.
SELECT MOD(1600, 300) FROM dual;

/*
날짜 함수
*/
/*
SYSDATE() 함수
    반환값 - 날짜, 시간
*/
SELECT sysdate FROM dual;

/*
날짜 연산 
    - 날짜에 숫자를 더하거나 빼서 결과 날짜 값을 구합니다.
    - 두 날짜 사이의 일수를 알아내기 위해 빼기 연산을 합니다.
    - 시간 수를 24로 나눠 날짜에 시간을 더합니다.
*/
SELECT last_name, (sysdate -hire_date)/7 AS WEEKS
FROM employees
WHERE department_id = 90;

/*
날짜 조작 함수

MONTHS_BETWEEN() - 두 날짜 간의 월수
ADD_MONTHS() - 날짜에 월 추가
NEXT_DAY() - 지정된 날짜의 다음날
LAST_DAY() - 월의 마지막 날
ROUND() - 날짜 반올림
TRUNC() - 날짜 truncate
*/

SELECT MONTHS_BETWEEN('22-12-16', '21-12-16') FROM dual;
SELECT ADD_MONTHS('22-12-16', 1) FROM dual;
SELECT NEXT_DAY('22-12-16', 1) FROM dual;
SELECT LAST_DAY('23-02-16') FROM dual;
SELECT ROUND(SYSDATE, 'MONTH') FROM dual;
SELECT TRUNC(SYSDATE, 'MONTH') FROM dual;


/*
변환함수
*/

/*
TO_CHAR() 함수 - 날짜 또는 숫자 사용가능

    YYYY - 숫자로 된 전체 연도
    YEAR - 영어 철자로 표기된 연도
    MM   - 월의 2자리 값
    MONTH - 전체 월 이름
    MON  - 월의 3자 약어
    DY   - 3문자로 된 요일 약어
    DAY  - 요일의 전체 이름
    DD   - 숫자 형식의 월간 일
    AM 또는 PM  - 자오선 표시
    A.M. 또는 P.M. - 마침표가 있는 자오선 표시
    HH 또는 HH12 또는 HH24 - 하루 시간 또는 반일 시간(1-12) 또는 전일 시간(0-23)
    MI   - 분(0-59)
    SS   - 초(0-59)
    
    TIMESTAMP 타입
    FF   - 밀리세컨드

*/
SELECT last_name, TO_CHAR(hire_date, 'YYYY/MM/DD HH24:MI:SS') AS HIREDATE
FROM employees;

SELECT TO_CHAR(SYSTIMESTAMP, 'YYYY-MM-DD HH24:MI:SS.FF2') FROM dual;


/*
TO_CHAR() 숫자에 사용

    9    - 숫자로 나타냄
    0    - 0이 표시되도록 강제 적용
    $    - 부동 달러 기호 배치
    L    - 부동 로컬 통화 기호 사용
    .    - 소수점 출력
    ,    - 천단위 표시자로 쉼표 출력

*/
SELECT TO_CHAR(salary, 'L99,999.00') SALARY
FROM employees
WHERE last_name = 'Ernst';

-- TO_DATE() - 문자를 DATE 타입으로 반환
SELECT last_name, TO_CHAR(hire_date, 'YYYY-MM-DD')
FROM employees 
WHERE hire_date < TO_DATE('2005-01-01', 'YYYY-MM-DD')
;

/*
함수 중첩
    단일 행 함수는 어떠한 레벨로도 중첩될 수 있습니다.
    중첩된 함수는 가장 깊은 레벨에서 가장 낮은 레벨로 평가됩니다.
*/
SELECT last_name, UPPER(CONCAT(SUBSTR(LAST_NAME, 1, 8), '_US'))
FROM employees
WHERE department_id = 60;


/*
NVL() 함수
    null 값을 실제 값으로 반환합니다.
    null은 연산이 안됩니다.
*/

SELECT last_name, salary, NVL(commission_pct, 0),
    (salary*12) + (salary*12*NVL(commission_pct, 0)) AN_SAL
FROM employees;

/*
NVL2() 함수
    첫번째 표현식을 검사합니다. 첫번째 표현식이 null이 아니면 NVL2 함수는 두번째 표현식을 반환합니다.
    첫번째 표현식이 null이면 세번째 표현식이 반환하빈다.
*/
SELECT last_name, salary, commission_pct,
    NVL2(commission_pct,
            'SAL+COMM', 'SAL') income
FROM employees
WHERE department_id IN (50, 80)
;

/*
NULLIF() 함수
    두 표현식을 비교 같으면 null 반환, 다르면 expr1을 반환 합니다.
    그러나 expr1에 대해 리터럴 NULL을 지정할 수 없습니다.
*/

SELECT first_name, LENGTH(first_name) "expr1",
    last_name, LENGTH(last_name) "expr2",
    NULLIF(LENGTH(first_name), LENGTH(last_name)) result
FROM employees
;


/*
COALESCE() 함수
    리스트에서 null이 아닌 첫번째 표현식을 반환합니다
*/
SELECT last_name, employee_id,
COALESCE(TO_CHAR(commission_pct),TO_CHAR(manager_id),
'No commission and no manager') 
FROM employees;


/*
조건부 표현식
    SQL 문에서 IF-THEN-ELSE 논리를 사용할 수 있습니다
    - CASE 식
    - DECODE 함수

*/


/*
CASE 식
    IF-THEN-ELSE 문 작업을 수행하여 조건부 조회를 편리하게
    수행하도록 합니다
*/
SELECT last_name, job_id, salary,
    CASE job_id WHEN 'IT_PROG' THEN 1.10*salary
                WHEN 'ST_CLERK' THEN 1.15*salary
                WHEN 'SA_REP' THEN 1.20*salary
    ELSE salary END "REVISED_SALARY"
FROM employees;

/*
DECODE() 함수
*/

SELECT last_name, job_id, salary,
    DECODE(job_id, 'IT_PROG', 1.10*salary,
                    'ST_CLERK', 1.15*salary,
                    'SA_REP', 1.20*salary,
            salary)
    REVISED_SALARY
FROM employees;

/*
그룹 함수란
    그룹 함수는 행 집합 연산을 수행하여 그룹별로 하나의 결과를 산출합니다.

    AVG() : n의 평균값. null 값은 무시합니다.
    COUNT() : 행 개수 null이 아닌 값을 평가합니다.
    MAX() : 최대값. null 값은 무시합니다.
    MIN() : 최소값. null 값은 무시합니다
    STDDEV() : 표준 편차. null 값은 무시합니다
    SUM() : 합계 값. null 값은 무시합니다.
    VARIANCE() : 분산. null 값은 무시합니다.
    
*/

SELECT AVG(salary), MAX(salary),
    MIN(salary), SUM(salary)
FROM employees
WHERE job_id LIKE '%REP%';

SELECT COUNT(*)
FROM employees
WHERE department_id = 50;

SELECT COUNT(*)
FROM employees
WHERE department_id = 50;

SELECT COUNT(commission_pct)
FROM employees
WHERE department_id = 80;

-- COUNT(DISTINCT expr)은 expr의 null이 아닌 구분 값의 수를 반환합니다
SELECT COUNT(DISTINCT department_id)
FROM employees;

-- NVL 함수는 강제로 그룹 함수에 null 값이 포함되도록 합니다.
SELECT AVG(NVL(commission_pct, 0))
FROM employees;

/*
GROUP BY 절 사용
   GROUP BY 절을 사용하여 테이블의 행을 그룹으로 나눌 수 있습니다.
*/
-- 그룹 함수에 속하지 않는 SELECT 리스트의 모든 열은 GROUP BY 절에 있어야 합니다
SELECT department_id, AVG(salary)
FROM employees
GROUP BY department_id ;

-- GROUP BY 열은 SELECT 리스트에 없어도 됩니다.
SELECT AVG(salary)
FROM employees
GROUP BY department_id ;

-- 여러 열에서 GROUP BY 절 사용
SELECT department_id, job_id, SUM(salary)
FROM employees
WHERE department_id > 40
GROUP BY department_id, job_id 
ORDER BY department_id;


/*
HAVING 절
    HAVING 절을 사용할 경우 Oracle 서버는 다음과 같이 그룹을 제한합니다
    1. 행이 그룹화됩니다.
    2. 그룹 함수가 적용됩니다.
    3. HAVING 절과 일치하는 그룹이 표시됩니다
*/

SELECT department_id, MAX(salary)
FROM employees
GROUP BY department_id
HAVING MAX(salary)>10000 ;

SELECT job_id, SUM(salary) PAYROLL
FROM employees
WHERE job_id NOT LIKE '%REP%'
GROUP BY job_id
HAVING SUM(salary) > 13000
ORDER BY SUM(salary);

-- 그룹 함수 중첩
SELECT MAX(AVG(salary))
FROM employees
GROUP BY department_id;
