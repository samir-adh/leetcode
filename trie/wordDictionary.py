class WordDictionary:

    def __init__(self, isValid: bool = True) -> None:
        self.isValid = isValid
        self.children: list[WordDictionary | None] = [None] * 26

    def __getitem__(self, c: str):
        return self.children[ord(c) - ord('a')]

    def __setitem__(self, c: str, node):
        self.children[ord(c) - ord('a')] = node

    def addWord(self, word: str) -> None:
        current = self
        for c in word:
            nextNode = current[c]
            if nextNode:
                current = nextNode
            else:
                nextNode = WordDictionary(False)
                current[c] = nextNode
            current = nextNode
        current.isValid = True

    def search(self, word: str) -> bool:
        def dfs(node: WordDictionary, index: int):
            if index >= len(word):
                return node.isValid
            if word[index] != '.':
                nextNode = node[word[index]]
                if nextNode:
                    return dfs(nextNode,  index + 1)
                else:
                    return False
            else:
                for child in node.children:
                    if child and dfs(child,  index + 1):
                        return True
                return False
        return dfs(self, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
