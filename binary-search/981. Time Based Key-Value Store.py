class TimeMap:

    def __init__(self):
        self.store = {} # KEY = STRING, value = [list of [value, timestamp]]


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])

        l, r = 0, len(values)-1
        while l <= r:
            mid = (l+r) // 2
            if values[mid][0] == timestamp:
                return values[mid][1]
            elif values[mid][0] < timestamp:
                res = values[mid][1]
                l = mid+1
            else:
                r = mid-1

        return res
