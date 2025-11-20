from typing import List

words = ["hello", "leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"


def isAlienSorted(words: List[str], order: str) -> bool:
    order_map = {}

    for i in range(len(order)):
        order_map[order[i]] = i

    for i in range(len(words) - 1):
        for j in range(len(words[i])):
            if j >= len(words[i + 1]):
                return False
            if words[i][j] != words[i + 1][j]:
                currlet = order_map[words[i][j]]
                next_let = order_map[words[i + 1][j]]
                if next_let < currlet:
                    return False
                else:
                    break


    return True


print(isAlienSorted(words, order))
