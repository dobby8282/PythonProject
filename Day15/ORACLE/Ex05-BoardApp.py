import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox as msg
import cx_Oracle

'''
CREATE TABLE HR.PY_BOARD (
  BOARD_ID         NUMBER(11)        PRIMARY KEY, 
  BOARD_TITLE      VARCHAR2(255)    DEFAULT NULL         NULL, 
  BOARD_WRITER     VARCHAR2(255)    DEFAULT NULL         NULL, 
  BOARD_CONTENT    CLOB                  NULL, 
  BOARD_DATE       DATE             DEFAULT SYSDATE                  NULL
);


CREATE SEQUENCE "PY_BOARD_SEQ";

'''

# 데이터베이스 접속 정보
username = 'hr'
password = 'hr'
host = 'localhost'
port = '31521'
sid = 'xe'
dsn = cx_Oracle.makedsn(host, port, sid)

class BoardApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('BoardApp')

        # 컨트롤 변수 선언
        self.combobox_search = ttk.Combobox(self)
        self.textfield_search = tk.Entry(self)
        self.button_search = tk.Button(self, text='검색', command=self.onclick_search)
        self.button_insert = tk.Button(self, text='신규', command=self.onclick_insert)
        self.button_delete = tk.Button(self, text='삭제', command=self.onclick_delete)
        self.button_update = tk.Button(self, text='수정', command=self.onclick_update)
        self.treeview_boardlist = ttk.Treeview(self, columns=('id','title', 'writer', 'date'), show="headings")


        # 컨트롤 배치
        self.combobox_search.grid(row=0, column=0,  padx=5, pady=5, sticky="nsew")
        self.textfield_search.grid(row=0, column=1,  padx=5, pady=5, sticky="nsew")
        self.button_search.grid(row=0, column=2, padx=5, pady=5, sticky="ns")
        self.treeview_boardlist.grid(row=1, column=0, rowspan=3, columnspan=2, padx=5, pady=5, sticky="nsew")
        self.button_insert.grid(row=1, column=2, padx=5, pady=5, sticky="ns")
        self.button_update.grid(row=2, column=2, padx=5, pady=5, sticky="ns")
        self.button_delete.grid(row=3, column=2, padx=5, pady=5, sticky="ns")

        # 트리뷰 컬럼 설정
        self.treeview_boardlist.heading('id', text='ID')
        self.treeview_boardlist.column('id', width=50)
        self.treeview_boardlist.heading('title', text='제목')
        self.treeview_boardlist.column('title', width=300)
        self.treeview_boardlist.heading('writer', text='작성자')
        self.treeview_boardlist.column('writer', width=100)
        self.treeview_boardlist.heading('date', text='작성일')
        self.treeview_boardlist.column('date', width=150)


        # 초기화
        self.init_boardlist()

    def get_boardlist(self, keyword='', search_option=''):
        # 데이터베이스 연결
        conn = cx_Oracle.connect(username, password, dsn)
        cur = conn.cursor()

        # 검색 조건에 따른 WHERE절 구성
        if search_option == '작성자':
            where_clause = "WHERE BOARD_WRITER LIKE '%' || :1 || '%'"
        else:
            where_clause = "WHERE BOARD_TITLE LIKE '%' || :1 || '%'"

        # SQL 문 실행
        sql = f"SELECT BOARD_ID, BOARD_TITLE, BOARD_WRITER, BOARD_DATE FROM PY_BOARD {where_clause} ORDER BY BOARD_ID DESC"
        cur.execute(sql, (keyword,))

        rows = []
        for row in cur:
            row = list(row)
            rows.append(row)

        # 데이터베이스 연결 해제
        cur.close()
        conn.close()

        return rows

    def init_boardlist(self):
        # 게시글 목록 조회
        rows = self.get_boardlist()

        # 트리뷰 초기화
        self.treeview_boardlist.delete(*self.treeview_boardlist.get_children())
        self.treeview_boardlist.bind('<Double-Button-1>', self.onclick_view)

        # 게시글 목록 출력
        for i, row in enumerate(rows):
            # num = len(rows) - i
            self.treeview_boardlist.insert('', 'end', text='', values=row)

        # 검색 기준 설정
        self.combobox_search['values'] = ('제목', '작성자')
        self.combobox_search.current(0)

    def onclick_search(self):
        # 검색어 가져오기
        keyword = self.textfield_search.get()

        # 검색 기준 가져오기
        search_option = self.combobox_search.get()

        # 검색 실행
        rows = self.get_boardlist(keyword, search_option)

        # 트리뷰 초기화
        self.treeview_boardlist.delete(*self.treeview_boardlist.get_children())

        # 게시글 목록 출력
        for i, row in enumerate(rows):
            num = len(rows) - i
            self.treeview_boardlist.insert('', 'end', text=str(num), values=row[:3])

    def onclick_insert(self):
        # 글쓰기 창 열기
        insert_dialog = BoardInsertDialog(self)
        self.wait_window(insert_dialog)

    def onclick_update(self):
        selection = self.treeview_boardlist.selection()
        if not selection:
            msg.showwarning('경고', '수정할 게시글을 선택하세요.')
            return
        board_id = self.treeview_boardlist.item(selection, 'values')[0]
        row, contents = self.get_board(board_id)
        # 글쓰기 창 열기
        update_dialog = BoardUpdateDialog(self, row, contents)
        self.wait_window(update_dialog)

    def get_board(self, board_id):
        # 데이터베이스 연결
        conn = cx_Oracle.connect(username, password, dsn)
        cur = conn.cursor()

        # SQL 문 실행
        sql = "SELECT * FROM PY_BOARD WHERE BOARD_ID=:1"
        cur.execute(sql, (board_id,))
        row = cur.fetchone()

        # CLOB 데이터 가져오기
        contents = row[3].read()

        # 데이터베이스 연결 해제
        cur.close()
        conn.close()

        return row, contents

    def onclick_delete(self):
        # 선택된 게시글 ID 가져오기
        selection = self.treeview_boardlist.selection()
        if not selection:
            msg.showwarning('경고', '삭제할 게시글을 선택하세요.')
            return
        board_id = self.treeview_boardlist.item(selection, 'values')[0]

        # 데이터베이스 연결
        conn = cx_Oracle.connect(username, password, dsn)
        cur = conn.cursor()

        # SQL 문 실행
        sql = 'DELETE FROM PY_BOARD WHERE BOARD_ID=:1'
        cur.execute(sql, (board_id,))
        conn.commit()

        # 데이터베이스 연결 해제
        cur.close()
        conn.close()

        # 게시글 목록 초기화
        self.init_boardlist()

    def onclick_view(self, event):
        # 선택된 게시글 ID 가져오기
        selection = self.treeview_boardlist.selection()
        if not selection:
            return
        board_id = self.treeview_boardlist.item(selection, 'values')[0]

        # 데이터베이스 연결
        conn = cx_Oracle.connect(username, password, dsn)
        cur = conn.cursor()

        # SQL 문 실행
        sql = "SELECT * FROM PY_BOARD WHERE BOARD_ID=:1"
        cur.execute(sql, (board_id,))
        row = cur.fetchone()
        if not row:
            cur.close()
            conn.close()
            return

        # CLOB 데이터 가져오기
        contents = row[3].read()
        # 데이터베이스 연결 해제
        cur.close()
        conn.close()

        # 게시글 상세보기 창 열기
        view_dialog = BoardViewDialog(self, row, contents)
        self.wait_window(view_dialog)

class BoardInsertDialog(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title('새 글 쓰기')

        # 컨트롤 변수 선언
        self.textfield_title = tk.Entry(self)
        self.textfield_writer = tk.Entry(self)
        self.textarea_content = scrolledtext.ScrolledText(self)
        self.button_save = tk.Button(self, text='저장', command=self.onclick_save)
        self.button_cancel = tk.Button(self, text='취소', command=self.destroy)

        # 컨트롤 배치
        tk.Label(self, text='제목').pack(side=tk.TOP, padx=5, pady=5)
        self.textfield_title.pack(side=tk.TOP, padx=5, pady=5, fill=tk.X)
        tk.Label(self, text='작성자').pack(side=tk.TOP, padx=5, pady=5)
        self.textfield_writer.pack(side=tk.TOP, padx=5, pady=5, fill=tk.X)
        tk.Label(self, text='내용').pack(side=tk.TOP, padx=5, pady=5)
        self.textarea_content.pack(side=tk.TOP, padx=5, pady=5, fill=tk.BOTH, expand=True)
        self.button_save.pack(side=tk.LEFT, padx=5, pady=5)
        self.button_cancel.pack(side=tk.RIGHT, padx=5, pady=5)

        # 부모 윈도우 중앙에 위치
        self.geometry('+%d+%d' % (parent.winfo_rootx() + parent.winfo_width() / 2 - self.winfo_width() / 2,
                                  parent.winfo_rooty() + parent.winfo_height() / 2 - self.winfo_height() / 2))

    def onclick_save(self):
        # 입력값 가져오기
        title = self.textfield_title.get()
        writer = self.textfield_writer.get()
        content = self.textarea_content.get('1.0', tk.END)

        # 데이터베이스 연결
        conn = cx_Oracle.connect(username, password, dsn)
        cur = conn.cursor()

        # 시퀀스에서 새로운 ID 생성
        cur.execute('SELECT PY_BOARD_SEQ.NEXTVAL FROM DUAL')
        board_id = cur.fetchone()[0]

        # SQL 문 실행
        sql = 'INSERT INTO PY_BOARD (BOARD_ID, BOARD_TITLE, BOARD_WRITER, BOARD_CONTENT) VALUES (:1, :2, :3, :4)'
        cur.execute(sql, (board_id, title, writer, content))
        conn.commit()

        # 데이터베이스 연결 해제
        cur.close()
        conn.close()

        # 다이얼로그 닫기
        self.destroy()

        # 게시글 목록 초기화
        self.master.init_boardlist()


class BoardViewDialog(tk.Toplevel):
    def __init__(self, parent, row, contents):
        super().__init__(parent)

        self.title('게시글 보기')

        # 컨트롤 변수 선언
        self.label_title = tk.Label(self, text=row[1], font=('Arial', 14, 'bold'))
        self.label_writer = tk.Label(self, text=row[2], font=('Arial', 12))
        self.textarea_content = scrolledtext.ScrolledText(self)
        self.button_close = tk.Button(self, text='닫기', command=self.destroy)

        # 컨트롤 배치
        self.label_title.pack(side=tk.TOP, padx=5, pady=5)
        self.label_writer.pack(side=tk.TOP, padx=5, pady=5)
        self.textarea_content.pack(side=tk.TOP, padx=5, pady=5, fill=tk.BOTH, expand=True)
        self.button_close.pack(side=tk.RIGHT, padx=5, pady=5)

        # 게시글 내용 출력
        self.textarea_content.insert(tk.END, contents)

        # 부모 윈도우 중앙에 위치
        self.geometry('+%d+%d' % (parent.winfo_rootx() + parent.winfo_width() / 2 - self.winfo_width() / 2,
                                  parent.winfo_rooty() + parent.winfo_height() / 2 - self.winfo_height() / 2))


class BoardUpdateDialog(tk.Toplevel):
    def __init__(self, parent, row, contents):
        super().__init__(parent)

        self.title('게시글 수정')

        # 수정할 게시글 정보 가져오기
        self.board_id = row[0]
        self.title = row[1]
        self.writer = row[2]
        self.content = contents

        # 컨트롤 변수 선언
        self.textfield_title = tk.Entry(self)
        self.textfield_writer = tk.Entry(self)
        self.textarea_content = scrolledtext.ScrolledText(self)
        self.button_save = tk.Button(self, text='저장', command=self.onclick_save)
        self.button_cancel = tk.Button(self, text='취소', command=self.destroy)

        # 컨트롤 초기값 설정
        self.textfield_title.insert(0, self.title)
        self.textfield_writer.insert(0, self.writer)
        self.textarea_content.insert(tk.END, self.content)

        # 컨트롤 배치
        tk.Label(self, text='제목').pack(side=tk.TOP, padx=5, pady=5)
        self.textfield_title.pack(side=tk.TOP, padx=5, pady=5, fill=tk.X)
        tk.Label(self, text='작성자').pack(side=tk.TOP, padx=5, pady=5)
        self.textfield_writer.pack(side=tk.TOP, padx=5, pady=5, fill=tk.X)
        tk.Label(self, text='내용').pack(side=tk.TOP, padx=5, pady=5)
        self.textarea_content.pack(side=tk.TOP, padx=5, pady=5, fill=tk.BOTH, expand=True)
        self.button_save.pack(side=tk.LEFT, padx=5, pady=5)
        self.button_cancel.pack(side=tk.RIGHT, padx=5, pady=5)

        # 부모 윈도우 중앙에 위치
        self.geometry('+%d+%d' % (parent.winfo_rootx() + parent.winfo_width() / 2 - self.winfo_width() / 2,
                                  parent.winfo_rooty() + parent.winfo_height() / 2 - self.winfo_height() / 2))

    def onclick_save(self):
        # 입력값 가져오기
        title = self.textfield_title.get()
        writer = self.textfield_writer.get()
        content = self.textarea_content.get('1.0', tk.END)

        # 데이터베이스 연결
        conn = cx_Oracle.connect(username, password, dsn)
        cur = conn.cursor()

        # SQL 문 실행
        sql = 'UPDATE PY_BOARD SET BOARD_TITLE=:1, BOARD_WRITER=:2, BOARD_CONTENT=:3 WHERE BOARD_ID=:4'
        cur.execute(sql, (title, writer, content, self.board_id))
        conn.commit()

        # 데이터베이스 연결 해제
        cur.close()
        conn.close()

        # 다이얼로그 닫기
        self.destroy()

        # 게시글 목록 초기화
        self.master.init_boardlist()


if __name__ == '__main__':
    app = BoardApp()
    app.mainloop()

