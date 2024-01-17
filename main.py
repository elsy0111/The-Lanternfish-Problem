#        +ﾟ☆* ﾖｼｯ！キミに
#      ｡;*｜∧ ∧ レートを
#    ･ﾟ＊* ∩ ･ω･ )与えよう
#  ☆:+｡･  ﾉ    ⊃
# +*:*+*･ し --J

import io
import sys

_INPUT = """\
5
1 2 3 3 4
10
18
80

"""

sys.stdin = io.StringIO(_INPUT)

# ? ===========================================
from copy import deepcopy as copy
from collections import defaultdict

n = int(input())
li = list(map(int,input().split()))
q = int(input())

def solve(li, x):
    for _ in range(x):
        for i in range(len(li)):
            if li[i] - 1 < 0:
                li.append(8)
                li[i] = 6
            else:
                li[i] -= 1
    return li

def cnt(li):
    dic = defaultdict(lambda:0)
    for i in li:
        dic[i] += 1
    return dic

# for i in range(q):
    # x = int(input())
for x in range(q + 1):
    a = copy(li)
    c = 0
    print(solve(a, x))
    D = cnt(solve(a, x))
    for i in D:
        c += D[i]
    # print(c)


