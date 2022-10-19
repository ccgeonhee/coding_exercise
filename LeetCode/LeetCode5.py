# 샘플 Python 스크립트입니다.
import collections
import copy
# Shift+F10을(를) 눌러 실행하거나 내 코드로 바꿉니다.
# 클래스, 파일, 도구 창, 액션 및 설정을 어디서나 검색하려면 Shift 두 번을(를) 누릅니다.
import math
import re


def solution(s: str)->str:
    result = []
    for i in range(0, len(s)-1):
        for j in range(i+1, len(s)+1):
            text = s[i:j]
            if len(text) < 2:
                continue
            if text == text[::-1]:
                result.append(text)

    result = sorted(result, key=lambda x:len(x))[0]
    return result


# 스크립트를 실행하려면 여백의 녹색 버튼을 누릅니다.
if __name__ == '__main__':
    s = "cbbd"
    solution(s)