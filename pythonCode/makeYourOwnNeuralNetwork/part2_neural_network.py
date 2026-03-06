
import numpy
import scipy.special
import matplotlib.pyplot

class neuralNetwork:

    # initialise the neural network 신경망초기화하기
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):

        # 입력, 은닉, 출력 계층의 노드 개수 설정
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes

        # link weight matrices, wih and who 가중치 행렬 정의 wih 와 who
        self.wih = numpy.random.normal(0.0, pow(self.inodes, -0.5), (self.hnodes, self.inodes))
        self.who = numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.onodes, self.hnodes))

        # learning rate 학습률
        self.lr = learningrate

        # activation function is the sigmoid function 활성화 함수로는 시그모이드 함수를 이용
        self.activation_function = lambda x: scipy.special.expit(x)

        print("신경망 초기화 끝")
        pass


    # train the neural network 신경망 학습시키기
    def train(self, inputs_list, targets_list):
        
        # convert inputs list to 2d array\n",
        inputs = numpy.array(inputs_list, ndmin=2).T
        targets = numpy.array(targets_list, ndmin=2).T

        # calculate signals into hidden layer
        hidden_inputs = numpy.dot(self.wih, inputs) 
        # calculate the signals emerging from hidden layer
        hidden_outputs = self.activation_function(hidden_inputs)
    
        # calculate signals into final output layer
        final_inputs = numpy.dot(self.who, hidden_outputs)
        # calculate the signals emerging from final output layer
        final_outputs = self.activation_function(final_inputs)

        # output layer error is the (target - actual)
        output_errors = targets - final_outputs
        # hidden layer error is the output_errors, split by weights, recombined at hidden nodes
        hidden_errors = numpy.dot(self.who.T, output_errors)
    
        # update the weights for the links between the hidden and output layers
        self.who += self.lr * numpy.dot((output_errors * final_outputs * (1.0 - final_outputs)), numpy.transpose(hidden_outputs))
        # update the weights for the links between the input and hidden layers
        self.wih += self.lr * numpy.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)), numpy.transpose(inputs))
    
        print("self.who: ", self.who)
        print("self.wih: ", self.wih)
        print("신경망 train 끝")
        pass
    
    # query the neural network 신경망 질의하기
    def query(self, inputs_list):
        # convert inputs list to 2d array\n"
        inputs = numpy.array(inputs_list, ndmin=2).T

        # calculate signals into hidden layer
        hidden_inputs = numpy.dot(self.wih, inputs)
        # calculate the signals emerging from hidden layer
        hidden_outputs = self.activation_function(hidden_inputs)

        # calculate signals into final output layer
        final_inputs = numpy.dot(self.who, hidden_outputs)
        # calculate the signals emerging from final output layer
        final_outputs = self.activation_function(final_inputs)

        print(final_outputs)
        print("신경망 query 끝")
        return final_outputs
    print("신경망 train 끝")
    
# 신경망 클래스 끝

nnwk = neuralNetwork(784, 100, 10, 0.3)
nnwk.query([1.0]*784)
nnwk.train([1.0]*784, [0.0]*10)
print("Neural Network class 정의 및 테스트 완료 ~~~")
