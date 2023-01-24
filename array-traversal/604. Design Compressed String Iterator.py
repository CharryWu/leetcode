class StringIterator:
    def advance(self):
        self.count = 0
        self.cur_char = self.str[self.p]
        self.p += 1
        while self.p < len(self.str) and self.str[self.p].isdigit():
            self.count = self.count * 10 + int(self.str[self.p])
            self.p += 1

    def __init__(self, compressedString: str):
        self.str = compressedString

        self.count = 0
        self.p = 0
        self.cur_char = ' '
        self.advance()

    def next(self) -> str:
        if self.p >= len(self.str) and self.count == 0:
            return ' '
        if self.count > 0:
            self.count -= 1
            return self.cur_char
        else:
            self.advance()
            self.count -= 1
            return self.cur_char

    def hasNext(self) -> bool:
        if self.p >= len(self.str) and self.count == 0:
            return False
        if self.count > 0:
            return True
        else:
            self.advance()
            return True