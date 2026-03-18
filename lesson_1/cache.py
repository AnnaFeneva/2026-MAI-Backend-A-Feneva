from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int = 10) -> None:
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: str) -> str:
        if key not in self.cache:
            return ""

        # делаем элемент "самым свежим"
        self.cache.move_to_end(key)
        return self.cache[key]

    def set(self, key: str, value: str) -> None:
        if key in self.cache:
            # обновляем и двигаем в конец
            self.cache.move_to_end(key)

        self.cache[key] = value

        # если превышен лимит — удаляем самый старый
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

    def rem(self, key: str) -> None:
        if key in self.cache:
            del self.cache[key]