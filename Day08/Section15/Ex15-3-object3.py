class Book:
    def set_info(self, title, author):
        self.title = title
        self.author = author

    def print_info(self):
        print('책 제목: {}'.format(self.title))
        print('책 저자: {}'.format(self.author))


# book1, book2 인스턴스의 생성
book1 = Book()
book2 = Book()

# book1, book2 제목과 저자 정보 저장
book1.set_info('파이썬', '민경태')
book2.set_info('어린왕자', '생텍쥐페리')

book_list = [book1, book2]
for book in book_list:
    book.print_info()   # book1.print_info()
                        # book2.print_info()
