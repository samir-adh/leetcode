class ListNode:
    def __init__(self, key=-1, val=-1, prev=None, next=None) -> None:
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self) -> str:
        nextkey = self.next.val if self.next is not None else None
        prevkey = self.prev.val if self.prev is not None else None
        return f"node {self.key} : next {nextkey} - prev {prevkey}"


class LRUCache:
    def __init__(self, capacity: int):
        self.head = None
        self.tail = None
        self.table: dict[int, ListNode] = {}
        self.capacity = capacity
        self.occupied = 0

    def get(self, key: int):
        if key not in self.table.keys():
            return -1
        else:
            node = self.table[key]
            # if the node is already on top
            if self.head.key == node.key:  # type: ignore
                return node.val
            # if the node is at the bottom
            elif self.tail.key == node.key:  # type: ignore
                # set previous node as tail
                node.prev.next = None  # type: ignore
                self.tail = node.prev
            # if the node is int the middle
            else:
                # join the previous and next node
                node.prev.next = node.next  # type: ignore
                node.next.prev = node.prev  # type: ignore
            # put node at the top
            node.prev = None
            node.next = self.head
            self.head.prev = node  # type: ignore
            self.head = node
            return node.val
        

    def put(self, key: int, value: int) -> None:
        # if the key already exists
        if key in self.table.keys():
            node = self.table[key]
            node.val = value
            # we use 'get' to put the key back on top
            _ = self.get(key)
        else:
            newNode = ListNode(key=key, val=value)
            self.table[key] = newNode
            # if this is the first value that we insert in the cache
            if self.head is None:
                self.head = newNode
                self.tail = newNode
                self.occupied += 1
            else :
                self.head.prev = newNode
                newNode.next = self.head
                self.head = newNode
                self.occupied += 1
                # If the cache is full
                if self.capacity < self.occupied:
                    # print(f"tail being popped: {self.tail.key}")
                    self.table.pop(self.tail.key)  # type: ignore
                    self.tail = self.tail.prev  # type: ignore
                    self.tail.next = None  # type: ignore
                    self.occupied -= 1

    def __str__(self) -> str:
        current = self.head
        out = "["
        while current is not None:
            out += f"({current.key}:{current.val}),"
            current = current.next
        out += "]"
        out += f" - cap: {self.capacity - self.occupied}"
        out += f" - keys: {self.table.keys()}"

        return out


def parse_test_case(
    commands: list[str], args: list[list[int]], limit: int, expected=None
):
    cache: LRUCache = LRUCache(0)
    for i in range(len(commands)):
        if limit > 0 and i >= limit:
            break
        arg = args[i]
        command = commands[i]
        out = None
        try:
            print(f"{command}({arg}): ")
            if command == "LRUCache":
                cache = LRUCache(arg[0])
            elif command == "get":
                node = cache.table.get(arg[0], None)
                # print(f"[BEFORE] {node}")
                out = cache.get(arg[0])
                node = cache.table.get(arg[0], None)
                # print(f"[AFTER] {node}")
            elif command == "put":
                cache.put(arg[0], arg[1])
            else:
                raise Exception(f"unknown command : {command}")
            if expected is not None:
                print(f"out: {out} - expected : {expected[i]}")
            else:
                print(f"out: {out}")
            print(f"cache : {cache}")
            # if i == 6:
            #     print(f"[+] {cache.table[2]}")
            # if i == 7:
            #     node = cache.table[4]
            #     print(f"[+] {node}")
            print("")
        except Exception as e:
            e.add_note(f"command {i + 1} '{command}' with arg '{arg}' failed.")
            e.add_note(f"Cache : {cache}")
            raise e


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
    parse_test_case(commands, args, limit=-3)


def test_case2():
    commands = ["LRUCache", "put", "put", "put", "put", "get", "get"]
    args = [[2], [2, 1], [1, 1], [2, 3], [4, 1], [1], [2]]
    parse_test_case(commands, args, limit=-1)


def test_case3():
    commands = [
        "LRUCache",
        "put",
        "put",
        "put",
        "put",
        "get",
        "get",
        "get",
        "get",
        "put",
        "get",
        "get",
        "get",
        "get",
        "get",
    ]
    args = [
        [3],
        [1, 1],
        [2, 2],
        [3, 3],
        [4, 4],
        [4],
        [3],
        [2],
        [1],
        [5, 5],
        [1],
        [2],
        [3],
        [4],
        [5],
    ]
    expected = [None, None, None, None, None, 4, 3, 2, -1, None, -1, 2, 3, -1, 5]
    parse_test_case(commands, args, limit=-1, expected=expected)


if __name__ == "__main__":
    test_case3()
