# 주어진 값이 팰린드롬 구조인지 판별하라
import collections


def solution(a: str) -> int:
    arr = a.split("->")
    arr = collections.deque(arr)
    left, right = 0, len(arr) - 1

    while left < right:
        if arr[left] != arr[right]:
            return False
        left += 1
        right -= 1

    return True


# 스크립트를 실행하려면 여백의 녹색 버튼을 누릅니다.
if __name__ == '__main__':
    a = "1->2"
    result = solution(a)
    print(result)
