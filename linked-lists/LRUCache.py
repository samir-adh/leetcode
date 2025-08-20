from typing import Optional


class Node:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.prev: Optional[Node] = None
        self.next: Optional[Node] = None

    def __str__(self) -> str:
        current = self
        output = "["
        while current != None:
            output += f"({current.key}:{current.value}), "
            current = current.next
        output += "]"

        return output


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.occupied = 0
        self.table: dict[int, Node] = {}
        self.head = None
        self.tail = None

    def insert(self, node: Node):
        head = self.head
        self.table[node.key] = node
        node.next = head
        if head is not None:
            head.prev = node
        self.head = node
        if self.tail is None:
            self.tail = node

    def remove(self, node: Node):
        prev = node.prev
        nextNode = node.next
        if prev is not None:
            prev.next = nextNode
        if nextNode is not None:
            nextNode.prev = prev
        else:
            self.tail = prev
        node.prev = None
        node.next = None
        if node.key in self.table.keys():
            self.table.pop(node.key)

    def get(self, key: int) -> int:
        node = self.table.get(key)
        if node is None:
            return -1
        if node.prev is not None:
            self.remove(node)
            self.insert(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.table.keys():
            node = self.table[key]
            node.value = value
            self.get(key)
        else:
            node = Node(key, value)
            self.insert(node)
            self.occupied += 1
            if self.occupied > self.capacity:
                if self.tail is not None:
                    self.remove(self.tail)
                self.occupied -= 1

    def __str__(self) -> str:
        return f"{self.head} - capacity: {self.occupied}/{self.capacity} keys: {list(self.table.keys())}"


def parse_commands(commands, args, expected, limit):
    cache = LRUCache(0)
    out = None
    for i in range(len(commands)):
        if i >= limit and limit > 0:
            break
        command = commands[i]
        arg = args[i]
        if command == "LRUCache":
            cache = LRUCache(arg[0])
            out = None
        if command == "put":
            cache.put(arg[0], arg[1])
            out = None
        if command == "get":
            out = cache.get(arg[0])
        print(f"executed {command} with {arg}")
        print(f"output : {out}, expected : {expected[i]}")
        print(f"cache: {cache}")
        print()


def test_case1():
    commands = [
        "LRUCache",
        "put",
        "put",
        "get",
        "put",
        "get",
        "put",
        "get",
        "get",
        "get",
    ]
    args = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    null = None
    expected = [null, null, null, 1, null, -1, null, -1, 3, 4]
    parse_commands(commands, args, expected, limit=-11)


def test_case2():
    commands = ["LRUCache", "put", "put", "get", "put", "put", "get"]
    args = [[2], [2, 1], [2, 2], [2], [1, 1], [4, 1], [2]]
    null = None
    expected = [null, null, null, 2, null, null, -1]
    parse_commands(commands, args, expected, limit=-11)


def test_case3():
    commands = ["LRUCache", "put", "put", "get", "put", "get", "get"]
    args = [[2], [2, 1], [1, 1], [2], [4, 1], [1], [2]]
    null = None
    expected = [null, null, null, 1, null, -1, 1]
    parse_commands(commands, args, expected, limit=-11)


if __name__ == "__main__":
    test_case3()

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
