from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])


        def up(i, j, visited) -> tuple[int, int, bool]:
            return i - 1, j, i - 1 >= 0 and (i - 1, j) not in visited

        def right(i, j, visited):
            return i, j + 1, j + 1 < n and (i, j + 1) not in visited

        def down(i, j, visited):
            return i + 1, j, i + 1 < m and (i + 1, j) not in visited

        def left(i, j, visited):
            return i, j - 1, j - 1 >= 0 and (i, j - 1) not in visited
        def aux(i, j, index, visited):


            moves = [up, right, down, left]

            # buffer += f"{[k, l]};"
            if index == len(word):
                return True
            for move in moves:
                k, l, isValid = move(i, j, visited)
                if isValid and board[k][l] == word[index]:
                    if aux(k, l, index + 1, visited.union([(k, l)])):
                        return True
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if aux(i, j, 1, set([(i, j)])):
                        return True
        return False


def test_case1():
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    expected = True
    output = Solution().exist(board, word)
    print(f"expected {expected}\ngot {output}")


def test_case2():
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCB"
    expected = False
    output = Solution().exist(board, word)
    print(f"expected {expected}\ngot {output}")


def test_case3():
    board = [["a", "a"]]
    word = "aaa"
    expected = False
    output = Solution().exist(board, word)
    print(f"expected {expected}\ngot {output}")


def test_case4():
    board = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]
    word = "ABCEFSADEESE"
    expected = True
    output = Solution().exist(board, word)
    print(f"expected {expected}\ngot {output}")


if __name__ == "__main__":
    test_case4()
