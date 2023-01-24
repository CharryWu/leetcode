class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.vlist = [v1, v2]
        self.ptrs = [0, 0]
        self.use_next = 0

    def next(self) -> int:
        val = None
        while self.ptrs[self.use_next] == len(self.vlist[self.use_next]):
            self.use_next = (self.use_next + 1) % len(self.vlist)
        val = self.vlist[self.use_next][self.ptrs[self.use_next]]
        self.ptrs[self.use_next] += 1
        self.use_next = (self.use_next + 1) % len(self.vlist)
        return val
        

    def hasNext(self) -> bool:
        found = False
        count = 0
        while count < len(self.vlist) and self.ptrs[self.use_next] == len(self.vlist[self.use_next]):
            self.use_next = (self.use_next + 1) % len(self.vlist)
            if self.ptrs[self.use_next] < len(self.vlist[self.use_next]):
                return True
            count += 1

        return self.ptrs[self.use_next] < len(self.vlist[self.use_next])

###### 简单的 if else 代码控制获取下个元素，不能对多个列表进行操作
# class ZigzagIterator:
#     def __init__(self, v1: List[int], v2: List[int]):
#         self.v1 = v1
#         self.v2 = v2
#         self.p1 = 0
#         self.p2 = 0
#         self.use_p1 = True

#     def next(self) -> int:
#         val = None
#         if self.use_p1:
#             if self.p1 == len(self.v1):
#                 val = self.v2[self.p2]
#                 self.p2 += 1
#             else:
#                 val = self.v1[self.p1]
#                 self.p1 += 1
#             self.use_p1 = False
#         else:
#             if self.p2 == len(self.v2):
#                 val = self.v1[self.p1]
#                 self.p1 += 1
#             else:
#                 val = self.v2[self.p2]
#                 self.p2 += 1
#             self.use_p1 = True
#         return val
        

#     def hasNext(self) -> bool:
#         if self.use_p1:
#             if self.p1 == len(self.v1):
#                 return self.p2 < len(self.v2)
#             else:
#                 return True
#         else:
#             if self.p2 == len(self.v2):
#                 return self.p1 < len(self.v1)
#             else:
#                 return True


# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())