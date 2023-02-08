class Book:
    def set_info(self, title, author):
        self.title = title
        self.author = author

    def print_info(self):
        print('책 제목: {}'.format(self.title))
        print('책 저자: {}'.format(self.author))