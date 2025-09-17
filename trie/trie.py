def toIdx(c: str):
    base = ord('a')
    return ord(c) - base


class Trie:

    def __init__(self, isValid : bool = True):
        self.children: list[None | Trie] = [None] * 26
        self.isValid = isValid

    def insert(self, word: str) -> None:
        current = self
        for c in word:
            newNode = current.children[toIdx(c)]
            if not newNode:
                newNode = Trie(False)
                current.children[toIdx(c)] = newNode
            current = newNode
        current.isValid = True
        return

    def search(self, word: str) -> bool:
        current = self
        for c in word:
            current = current.children[toIdx(c)]
            if not current:
                return False
        return current.isValid

    def startsWith(self, prefix: str) -> bool:
        current = self
        for c in prefix:
            current = current.children[toIdx(c)]
            if not current:
                return False
        return True



def run_testcase(commands: list[str], args: list[str], expectedOutputs=None):
    if not expectedOutputs:
        expectedOutputs = [-1] * len(commands)
    t = Trie()
    log = []
    i = -1
    command = None
    arg = None
    try:
        for i, (command, arg, expected) in enumerate(zip(commands, args, expectedOutputs)):
            if i == 3:
                pass
            out = ''
            if command == "Trie":
                t = Trie()
                out = None
            elif command == "insert":
                out = t.insert(arg[0])

            elif command == "search":
                out = t.search(arg[0])
            elif command == "startsWith":
                out = t.startsWith(arg[0])
            if out != expected and expected != -1:
                print(
                    f"wrong anwser at step n°{i} with command '{command}' and arg '{arg}'")
                print(f"expected '{expected}' got '{out}'")
            log.append(out)
    except Exception as e:
        print(f"failed at step n°{i} with command '{command}' and arg '{arg}'")
        raise e
    finally:
        print(log)


def test_case1():
    commands = ["Trie", "insert", "search",
                "search", "startsWith", "insert", "search"]
    args = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
    expectedOutputs = [None, None, True, False, True, None, True]
    run_testcase(commands, args, expectedOutputs)


def test_case2():
    commands = ["Trie", "startsWith"]
    args = [[], ["a"]]
    expectedOutputs = [None, False]
    run_testcase(commands, args, expectedOutputs)


if __name__ == "__main__":
    test_case2()


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
