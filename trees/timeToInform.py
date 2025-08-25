class Tree:
    def __init__(self, manager, informTime, children):
        self.manager = manager
        self.informTime = informTime
        self.children = children

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        nodes = [Tree(None, t, []) for t in informTime]
        for i in range(len(nodes)):
            if manager[i] != -1:
                nodes[manager[i]].children.append(nodes[i])
        root = nodes[headID]

        stack = [root]
        maxt = 0

        while stack:
            node = stack.pop()
            for child in node.children:
                    child.informTime += node.informTime
                    maxt = max(maxt, child.informTime)
                    stack.append(child)
        return maxt


            


