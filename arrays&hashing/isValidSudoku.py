from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def boxId(i, j):
            return 3*(i//3) + j//3
        rows = [[0 for i in range(9)] for i in range(9)]
        cols = [[0 for i in range(9)] for i in range(9)]
        boxes = [[0 for i in range(9)] for i in range(9)]
        for i in range(9):  # rows
            for j in range(9):  # columns
                s = board[i][j]
                # print(f"{i, j,boxId(i,j)}={item}")
                nbox = boxId(i,j)
                if s != ".":
                    print(nbox)
                    print(boxes)
                    item = int(s) - 1
                    # check row
                    if rows[i][item] == 0:
                        rows[i][item] += 1
                    else:
                        return False
                    # check column
                    if cols[j][item] == 0:
                        cols[j][item] += 1
                    else:
                        return False
                    # check box
                    if boxes[nbox][item] == 0:
                        boxes[nbox][item] += 1
                    else:
                        return False
        return True


def test_case1():
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",
                                                                                                                                                                                                          ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    expected = True
    output = Solution().isValidSudoku(board)
    print(f"expected {expected}, got {output}")


if __name__ == "__main__":
    test_case1()
