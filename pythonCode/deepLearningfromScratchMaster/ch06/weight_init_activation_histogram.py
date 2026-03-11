# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def ReLU(x):
    return np.maximum(0, x)

# 입력된 배열(또는 스칼라)의 각 요소에 대해 하이퍼볼릭 탄젠트(Hyperbolic Tangent, tanh) 값을 계산합
def tanh(x):    #双曲線正接関数 입력값을 -1에서 1 사이로 변환하는 함수 tanh
    return np.tanh(x)

# np.random.randn은 평균 0, 표준편차 1인 표준정규분포(Gaussian)에서 
# 난수를 추출하여 지정된 형태의 N차원 배열(array)을 생성하는 함수

input_data = np.random.randn(1000, 100)  # 1000個のデータ
node_num = 100  # 各隠れ層のノード（ニューロン）の数
hidden_layer_size = 5  # 隠れ層が5層
activations = {}  # ここにアクティベーションの結果を格納する

print("input_data.shape: " + str(input_data.shape))
print("input_data: " + str(input_data))

x = input_data

for i in range(hidden_layer_size):
    if i != 0:
        x = activations[i-1]

    # 初期値の値をいろいろ変えて実験しよう！
    # w = np.random.randn(node_num, node_num) * 1 # 1倍
    # w = np.random.randn(node_num, node_num) * 0.01 # 0.01倍 표준편차 0.01
    # w = np.random.randn(node_num, node_num) * np.sqrt(1.0 / node_num)
    
    w = np.random.randn(node_num, node_num) * np.sqrt(2.0 / node_num) 
    # He 초기값 표준편차 sqrt(2/n) ReLU에 적합한 초기값 
    # xavier 초기값 표준편차 sqrt(1/n) sigmoid, tanh에 적합한 초기값


    a = np.dot(x, w)

    # 活性化関数の種類も変えて実験しよう！
    # z = sigmoid(a)
    z = ReLU(a)
    # z = tanh(a)

    activations[i] = z

# ヒストグラムを描画
for i, a in activations.items():
    plt.subplot(1, len(activations), i+1)
    plt.title(str(i+1) + " - 계층 ヒストグラム")
    if i != 0: plt.yticks([], [])
    # plt.xlim(0.1, 1)
    # plt.ylim(0, 7000)
    plt.hist(a.flatten(), 30, range=(0,1))
plt.show()
