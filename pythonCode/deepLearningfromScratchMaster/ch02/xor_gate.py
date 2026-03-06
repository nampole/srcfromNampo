# 배타적 논리합 
# XOR 게이트는 입력이 둘 다 0이거나 둘 다 1일 때는 0을 출력하고, 그 외의 경우에는 1을 출력하는 논리 회로입니다.
# 선형으로 분리할 수 없는 문제이므로, NAND 게이트와 OR 게이트를 조합하여 XOR 게이트를 구현합니다.
# 비선형으로 분리할 수 없는 문제는 단일 퍼셉트론으로는 해결할 수 없지만, 여러 퍼셉트론을 조합하여 해결할 수 있습니다.

# coding: utf-8
# 파일에서 NAND, OR, AND 게이트를 가져와서 XOR 게이트를 구현합니다.
from and_gate import AND
from or_gate import OR
from nand_gate import NAND

# nand, or, nand 게이트를 조합하여 xor 게이트를 구현

def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y

if __name__ == '__main__':
    for xs in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        y = XOR(xs[0], xs[1])
        print(str(xs) + " -> " + str(y))