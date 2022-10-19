import re
import collections


def solution(strs: list)->list:
    count_dict = collections.defaultdict(list)
    for string in strs:
        sorted_string = "".join(sorted(string))
        count_dict[sorted_string].append(string)
    result = sorted([value for key, value in count_dict.items()], key=lambda x:len(x))
    print(result)
    return result

# 스크립트를 실행하려면 여백의 녹색 버튼을 누릅니다.
if __name__ == '__main__':
    strs = ["eat","tea","tan","ate","nat","bat"]
    solution(strs)