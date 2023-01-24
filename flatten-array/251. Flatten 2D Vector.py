class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.p1 = 0 # 外层指针
        self.p2 = 0 # 内层指针
        self.vec = vec

    def next(self) -> int:
        retval = self.vec[self.p1][self.p2]
        if self.p2 + 1 < len(self.vec[self.p1]):
            self.p2 += 1
        else:
            self.p2 = 0
            self.p1 += 1
            while self.p1 < len(self.vec):
                if len(self.vec[self.p1]) > 0:
                    break
                self.p1 += 1
            
        return retval
        

    def hasNext(self) -> bool:
        if not self.vec:
            return False
        if self.p1 > len(self.vec) - 1:
            return False
        elif self.p1 == len(self.vec) - 1:
            return self.p2 < len(self.vec[-1])
        else: # self.p1 < len(self.vec) - 1， 外层指针不是最后一个元素
            if self.p2 < len(self.vec[self.p1]):
                return True
            while self.p1 < len(self.vec):
                if len(self.vec[self.p1]) > 0:
                    return True
                self.p1 += 1
            return False