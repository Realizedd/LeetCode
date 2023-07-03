class TimeMap:
    def __init__(self):
        self.map = {}

    def search(self, ls, timestamp):
        start, end = 0, len(ls) - 1

        while start <= end:
            mid = (start + end) // 2

            if ls[mid][0] == timestamp:
                return mid
            elif ls[mid][0] > timestamp:
                end = mid - 1
            else:
                start = mid + 1

        return start - 1 if start != 0 else start

    def set(self, key: str, value: str, timestamp: int) -> None:
        ls = self.map.get(key, [])
        ls.append((timestamp, value))
        self.map[key] = ls

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map or not self.map[key]:
            return ""

        ls = self.map[key]
        idx = self.search(ls, timestamp)

        if idx == 0 and timestamp < ls[idx][0]:
            return ""

        return ls[idx][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
sol = TimeMap()
sol.set("love","high",10)
sol.set("love","low",20)
print(sol.get("love", 5))
print(sol.get("love", 10))
print(sol.get("love", 15))
print(sol.get("love", 20))
print(sol.get("love", 25))