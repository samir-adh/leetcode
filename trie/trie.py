class Trie:

    def __init__(self, isValid: bool = False):
        self.isValid = isValid
        self.children: dict[str, Trie] = {}

    def __getitem__(self, key: str):
        return self.children[key]

    def __setitem__(self, key: str, val: Trie):
        self.children[key] = val

    def insert(self, word: str) -> None:
        def aux(index: int, node: Trie):
            if index >= len(word):
                node.isValid = True
                return
            c = word[index]
            if c in node.children:
                aux(index+1, node[c])
            else:
                nextNode = Trie()
                node[c] = nextNode
                aux(index+1, nextNode)
        aux(0, self)

    def search(self, word: str) -> bool:
        def aux(index: int, node: Trie) -> bool:
            if index >= len(word):
                return node.isValid
            c = word[index]
            if c not in node.children:
                return False
            else:
                return aux(index+1, node[c])
        return aux(0, self)

    def startsWith(self, prefix: str) -> bool:
        def aux(index: int, node: Trie) -> bool:
            if index >= len(prefix):
                return True
            c = prefix[index]
            if c not in node.children:
                return False
            else:
                return aux(index+1, node[c])
        return aux(0, self)

        # Your Trie object will be instantiated and called as such:
        # obj = Trie()
        # obj.insert(word)
        # param_2 = obj.search(word)
        # param_3 = obj.startsWith(prefix)
