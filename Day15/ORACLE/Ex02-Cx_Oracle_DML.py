'''
Ex02-Cx_Oracle_DML.py
'''
import cx_Oracle
from datetime import datetime

hire_date = datetime.strptime('2022-03-01', '%Y-%m-%d').strftime('%Y-%m-%d')

# 데이터베이스 접속 정보
username = 'hr'
password = 'hr'
host = 'localhost'
port = '31521'
sid = 'xe'
dsn = cx_Oracle.makedsn(host, port, sid)

# 데이터베이스 연결
conn = cx_Oracle.connect(username, password, dsn)
cur = conn.cursor()

conn = cx_Oracle.connect(username, password, dsn)
cur = conn.cursor()
sql = "INSERT INTO employees (employee_id, first_name, last_name, email, hire_date, job_id, salary, department_id) " \
      "VALUES (:1, :2, :3, :4, TO_DATE(:5, 'YYYY-MM-DD'), :6, :7, :8)"

cur.execute(sql, (1003, 'John', 'Doe', 'johndoe1@example.com', '2022-03-01',
                  'IT_PROG', 5000, 90))
conn.commit()
cur.close()
conn.close()