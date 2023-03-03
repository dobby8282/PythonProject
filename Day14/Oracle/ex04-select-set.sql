/*
집합 연산자
    SELECT 리스트의 표현식은 개수가 일치해야 합니다.
    데이터 유형은 첫번째 query 데이터 유형과 일치해야 합니다.
    UNION, UNION ALL, INTERSECT, MINUS
*/

/*
UNION 연산자
    중복 행이 제거된 두 query의 행
*/
SELECT employee_id, job_id
FROM employees
UNION
SELECT employee_id, job_id
FROM job_history
;

/*
UNION ALL 연산자
    중복 행이 포함된 두 query의 행
*/
SELECT employee_id, job_id, department_id
FROM employees
UNION ALL
SELECT employee_id, job_id, department_id
FROM job_history
ORDER BY employee_id;

/*
INTERSECT 연산자
    두 query에 공통적인 행
*/

SELECT employee_id, job_id
FROM employees
INTERSECT
SELECT employee_id, job_id
FROM job_history;

/*
MINUS 연산자
    첫번째 query에 있는 행 중 두번째 query에 없는 행 
*/
SELECT employee_id
FROM employees
MINUS
SELECT employee_id
FROM job_history;

/*
!주의> 데이터 유형을 일치시켜야 합니다.
*/

SELECT location_id, department_name "Department", 
TO_CHAR(NULL) "Warehouse location" 
FROM departments
UNION
SELECT location_id, TO_CHAR(NULL) "Department", 
state_province
FROM locations;


SELECT employee_id, job_id,salary
FROM employees
UNION
SELECT employee_id, job_id,0
FROM job_history;




/*

[기본형식]
  SELECT 컬럼명1, 컬럼명2.....					        .5
  FROM 테이블명					       	            .1
  WHERE 조건절							            .2		
  GROUP BY 칼럼명						                .3
  HAVING 조건절 (GROUP묶은 다음에 조건 줄 때	)		    .4
  ORDER BY 칼럼명[ASC|DESC] => 오름차순 혹은 내림차순		.6

*/

