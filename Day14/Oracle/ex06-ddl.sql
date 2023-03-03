/*
DDL(데이터 정의어)
    데이터 베이스 내의 객체(테이블,시퀀스...) 등을 생성하고 변경하고 삭제하기 위해서 사용되는 SQL문
*/

/*

CREATE TABLE 문
    데이터를 저장할 테이블을 생성합니다.
*/

CREATE TABLE dept
        (deptno NUMBER(6),
        dname VARCHAR2(200),
        loc VARCHAR2(200),
        create_date DATE DEFAULT SYSDATE);
    

DESC dept;


/*
데이터유형
    VARCHAR2(size) 가변 길이 문자 데이터 (4000)
    NUMBER(p,s) 가변 길이 숫자 데이터
    CHAR(size) 고정 길이 문자 데이터 (2000)
    DATE 날짜 및 시간 값
    LONG 가변 길이 문자 데이터(최대 2GB)
    CLOB 문자 데이터(최대 4GB)
    RAW and LONG RAW 원시 이진 데이터
    BLOB 바이너리 데이터(최대 4GB)
    BFILE 외부 파일에 저장된 바이너리 데이터(최대 4GB)
    ROWID 테이블에 있는 행의 고유한 주소를 나타내는 base-64 숫자 체계

*/

-- departments 테이블을 dept에 복사하기
INSERT INTO dept SELECT department_id, department_name , location_id, sysdate FROM departments;

-- dept테이블을 dept2에 복사하기
INSERT INTO dept2 SELECT * FROM dept;


-- 테이블 복사하기2 (CTAS 기법) => 제약조건은 복사가 안된다
CREATE TABLE dept3 AS SELECT * FROM dept;

-- 테이블의 구조만 복사 (조건이 항상 거짓이 되는 편법사용)
CREATE TABLE dapt4 AS SELECT * FROM dept WHERE 1=2;


/*
ALTER 
    객체를 변경할 때 사용합니다.
*/

CREATE TABLE simple(num NUMBER);    --테이블 생성

ALTER TABLE simple ADD(name VARCHAR2(3)); 
ALTER TABLE simple MODIFY(name VARCHAR2(30));
ALTER TABLE simple DROP COLUMN name;

ALTER TABLE simple ADD(addr VARCHAR2(50)); 
ALTER TABLE simple MODIFY(addr VARCHAR2(100));
ALTER TABLE simple DROP(addr);

DROP TABLE simple;


/*
제약조건(Constraint)
    테이블의 해당칼럼에 원하지 않는 데이터를 입력/수정/삭제 되는 것을 방지하기
    위해 테이블 생성 또는 변경시 설정하는 조건입니다.(저장된 테이터의 신뢰성을 높이기 위해)
    
    NOT NULL
        NULL로 입력이 되어서는 안되는 칼럼에 부여하는 
        조건으로 칼럼 레벨에서만 부여할 수 있는 제약조건입니다.
    UNIQUE KEY(유일키)
        저장된 값이 중복되지 않고 오직 유일하게 
        유지되어야 할 때 사용하는 제약조건입니다.
        (NULL은 허용된다)

    PRIMARY KEY(대표키)
        NOT NULL조건과 UNIQUE KEY를 합친 조건입니다.
        (테이블 하나당 하나는 있어야 한다)
    CHECK 
        조건에 맞는 데이터만 입력되도록 조건을 부여하는 제약조건입니다.
    FOREIGN KEY(외래키) 
        부모 테이블의 PRIMARY KEY를 참조하는 칼럼에 붙이는 제약조건입니다.   
*/
create table dept2
(dept number(2) constraint dept2_deptno_pk primary key,
dname varchar2(15) default'영업부',
loc char(1) constraint dept2_loc_ck check(loc in('1','2')));

DROP TABLE dept3;
CREATE TABLE dept3
(dept NUMBER(2) PRIMARY KEY,
dname VARCHAR2(15) DEFAULT'영업부',
loc CHAR(1) CHECK(loc IN('1','2')));


-- 외래키를 만들기 위해서는 부모테이블을 먼저 만들어야한다
-- 부모테이블 만들기
DROP TABLE dept2; 
CREATE TABLE dept2(
deptno NUMBER(2) PRIMARY KEY,
dname VARCHAR2(15) NOT NULL);

-- 부모테이블 참조하는 자식테이블 만들기
DROP TABLE emp2;
CREATE TABLE emp2(
empno NUMBER(4) PRIMARY KEY,
ename VARCHAR2(15) NOT NULL,
deptno NUMBER(2) REFERENCES dept2(deptno));

-- 제약 조건 이름 검색하기
SELECT * FROM user_constraints
--WHERE table_name ='EMP2'
;
-- 제약조건 검색
select constraint_name from user_constraints;

-- 제약조건은 수정 불가능, 삭제만 가능하다
alter table dept2 drop constraint 제약조건명;

-- 제약조건 추가하기
alter table dept2 add(constraint 제약조건명 primary key(deptno));




/*
시퀀스(Sequence)
    연속적인 숫자 값을 자동으로 증감 시켜서 값을 리턴하는 객체
*/
CREATE SEQUENCE my_seq;
SELECT my_seq.NEXTVAL FROM dual;
DROP SEQUENCE my_seq;
SELECT my_seq.CURRVAL FROM dual;

SELECT * FROM dept2;

INSERT INTO dept2 VALUES (my_seq.NEXTVAL, 'A', 1);
INSERT INTO dept2 VALUES (my_seq.NEXTVAL, 'B', 2);
INSERT INTO dept2 VALUES (my_seq.NEXTVAL, 'C', 1);
