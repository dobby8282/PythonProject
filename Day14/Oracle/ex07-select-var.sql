/*
치환 변수
    - 단일 앰퍼샌드(&) 및 이중 앰퍼샌드(&&) 치환을 사용 값 임시저장
*/

/*
단일 앰퍼샌드 치환 변수 사용
    변수앞에  & 붙이면 유저가 값을 입력하도록 할 수 있습니다.
*/
SELECT employee_id, last_name, salary, department_id
FROM employees
WHERE employee_id = &employee_num;


/*
문자 및 날짜 값을 치환 변수로 지정
    날짜 값 및 문자 값에 대해 작은 따옴표를 사용합니다.
*/
SELECT last_name, department_id, salary*12
FROM employees
WHERE job_id = '&job_title';


-- 열 이름, 표현식 및 텍스트 지정
SELECT employee_id, last_name, job_id, &column_name
FROM employees
WHERE &condition
ORDER BY &order_column;

/*
이중 앰퍼샌드 치환 변수 사용
    유저가 매번 값을 입력할 필요 없이 재사용할 경우 이중 앰퍼샌드(&&) 사용합니다.
*/
SELECT employee_id, last_name, job_id, &&column_name
FROM employees
ORDER BY &column_name;

/*
DEFINE 명령 사용
    DEFINE 명령 사용하여 변수 생성하고 값 할당합니다.
    UNDEFINE 명령 사용하여 변수 제거합니다.
*/
DEFINE employee_num = 200

SELECT employee_id, last_name, salary, department_id
FROM employees
WHERE employee_id = &employee_num;

UNDEFINE employee_num;

/*
VERIFY 명령 사용
    VERIFY 명령을 사용하여 SQL Developer가 
    치환 변수를 값으로 바꾸기 전후에 치환 변수의 
    표시를 토글합니다.
*/
SET VERIFY ON
SELECT employee_id, last_name, salary
FROM employees
WHERE employee_id = &employee_num;

/*
바인드 변수
    오라클에서 사용하는 변수
    치환변수보다 성능 좋다 적극사용!!!
    
    자바 개발자 JDBC 
         -> STATEMENT 치환변수
         -> PREPARESTATMENT 바인드변수
         마이바티스
         -> #변수명
*/
VAR employee_num NUMBER
EXEC :employee_num := 101
SELECT employee_id, last_name, salary
FROM employees
WHERE employee_id = :employee_num;
