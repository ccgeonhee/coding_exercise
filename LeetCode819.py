import collections
import copy


# Shift+F10을(를) 눌러 실행하거나 내 코드로 바꿉니다.
# 클래스, 파일, 도구 창, 액션 및 설정을 어디서나 검색하려면 Shift 두 번을(를) 누릅니다.
import math
import re


def solution(paragraph, banned):
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
    count_dict = collections.defaultdict(int)

    for word in words:
        count_dict[word] += 1
    counter = collections.Counter(count_dict)
    result = counter.most_common()[0][0]

    return result

# 스크립트를 실행하려면 여백의 녹색 버튼을 누릅니다.
if __name__ == '__main__':
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    solution(paragraph, banned)