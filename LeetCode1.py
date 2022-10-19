# 샘플 Python 스크립트입니다.
import collections
import copy
import datetime

# Shift+F10을(를) 눌러 실행하거나 내 코드로 바꿉니다.
# 클래스, 파일, 도구 창, 액션 및 설정을 어디서나 검색하려면 Shift 두 번을(를) 누릅니다.
import math
import re
import time


def solution(nums:list, target:int) -> list:
    result = []
    for i in range(len(nums) - 1):
        operation_num = target - nums[i]
        operation_list = nums[i+1:]
        operation_dict = {num:target-num for num in operation_list}
        if operation_num in operation_dict:
            result.append(i)
            result.append(i+1)
            break
    return result



# 스크립트를 실행하려면 여백의 녹색 버튼을 누릅니다.
if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    solution(nums, target)
# https://www.jetbrains.com/help/pycharm/에서 PyCharm 도움말 참조



