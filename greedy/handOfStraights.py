from typing import DefaultDict, List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freq = DefaultDict(int)
        if len(hand) % groupSize != 0:
            return False
        for card in hand:
            freq[card] += 1
        stack = sorted(freq.keys())
        while stack:
            current = stack[0]
            # print("====STEP====")
            # print(f"stack {stack}")
            # print(f"freq {freq}")
            # print(f"current {current}")
            if freq[current] == 0:
                stack.pop(0)
                continue
            for i in range(groupSize):
                if freq[current+i] == 0:
                    print(f"freq of {current+i} = 0")
                    return False
                else:
                    freq[current+i] -= 1
        return True


def test_case1():
    hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
    groupSize = 3
    output = Solution().isNStraightHand(hand, groupSize)
    expected = True
    assert output == expected


def test_case2():
    hand = [1, 2, 3, 4, 5]
    groupSize = 4
    output = Solution().isNStraightHand(hand, groupSize)
    expected = False
    assert output == expected

def test_case3():
    hand = [1,1,2,2,3,3] 
    groupSize = 3
    output = Solution().isNStraightHand(hand, groupSize)
    expected = True
    assert output == expected


test_case3()
