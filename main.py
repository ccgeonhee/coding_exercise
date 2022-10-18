# 샘플 Python 스크립트입니다.
import collections
import copy


# Shift+F10을(를) 눌러 실행하거나 내 코드로 바꿉니다.
# 클래스, 파일, 도구 창, 액션 및 설정을 어디서나 검색하려면 Shift 두 번을(를) 누릅니다.
import math
import re


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

# https://www.jetbrains.com/help/pycharm/에서 PyCharm 도움말 참조



