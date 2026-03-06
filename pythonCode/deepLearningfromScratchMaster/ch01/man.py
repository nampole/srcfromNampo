import numpy as np
# coding: utf-8
class Man:
    """サンプルクラス"""

    def __init__(self, name):
        self.name = name
        print("Initilized! 초기화 되었습니다!")

    def hello(self):
        print("Hello " + self.name + "!")

    def goodbye(self):
        print("Good-bye " + self.name + "!")

m = Man("대한민국")
m.hello()
m.goodbye()

x = np.array([1.0, 2.0, 3.0])
print(x)
print (type(x))
y = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
print(y)
print (type(y))
print (y/3.0)
