CREATE TABLE HR.PY_BOARD (
  BOARD_ID         NUMBER(11)        PRIMARY KEY,
  BOARD_TITLE      VARCHAR2(255)    DEFAULT NULL         NULL,
  BOARD_WRITER     VARCHAR2(255)    DEFAULT NULL         NULL,
  BOARD_CONTENT    CLOB                  NULL,
  BOARD_DATE       DATE             DEFAULT SYSDATE                  NULL
);


CREATE SEQUENCE "PY_BOARD_SEQ";