from typing import List


def findLucky(arr: List[int]) -> int:
    freq = {}

    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    answer = -1

    for num in arr:
        if freq[num] == num:
            answer = max(answer, num)

    return answer


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    print(findLucky(arr))