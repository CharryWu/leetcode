
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.cur_idx = -1
        self.flat = []
        
        def dfs(l):
            if l.isInteger():
                self.flat.append(l.getInteger())
            else:
                for item in l.getList():
                    dfs(item)
        
        for item in nestedList:
            dfs(item)
        self.N = len(self.flat)

    def next(self) -> int:
        if self.hasNext():
            self.cur_idx += 1
            return self.flat[self.cur_idx]
        return None

    def hasNext(self) -> bool:
        return self.cur_idx + 1 < self.N

