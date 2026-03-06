# 3계층의 신경망으로 MNIST 데이터를 학습하는 코드
import numpy
# scipy.special for the sigmoid function expit()
import scipy.special
# library for plotting arrays
import matplotlib.pyplot
# %matplotlib inline

# neural network class definition
class neuralNetwork:

    # initialise the neural network 초기화
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        # set number of nodes in each input, hidden, output layer
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes
        
        # link weight matrices, wih and who
        # weights inside the arrays are w_i_j, where link is from node i to node j in the next layer,
        # w11 w21
        # w12 w22 etc
        self.wih = numpy.random.normal(0.0, pow(self.inodes, -0.5), (self.hnodes, self.inodes))
        self.who = numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.onodes, self.hnodes))

        # learning rate,
        self.lr = learningrate
    
        # activation function is the sigmoid function,
        self.activation_function = lambda x: scipy.special.expit(x)
        
        pass

    # train the neural network,
    def train(self, inputs_list, targets_list):
        # convert inputs list to 2d array
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
        
        # update the weights for the links between the input and hidden layers,
        self.wih += self.lr * numpy.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)), numpy.transpose(inputs))
        
        pass

    # query the neural network
    def query(self, inputs_list):
        # convert inputs list to 2d array
        inputs = numpy.array(inputs_list, ndmin=2).T
        
        # calculate signals into hidden layer
        hidden_inputs = numpy.dot(self.wih, inputs)
        # calculate the signals emerging from hidden layer
        hidden_outputs = self.activation_function(hidden_inputs)
        
        # calculate signals into final output layer
        final_inputs = numpy.dot(self.who, hidden_outputs)
        # calculate the signals emerging from final output layer
        final_outputs = self.activation_function(final_inputs)
        
        print("***** final_outputs 내용 :: ", final_outputs)
        return final_outputs

# number of input, hidden and output nodes,
input_nodes = 784
hidden_nodes = 100
output_nodes = 10

# learning rate
# learning_rate = 0.1
learning_rate = 0.8

# create instance of neural network,
n = neuralNetwork(input_nodes,hidden_nodes,output_nodes, learning_rate)

# load the mnist training data CSV file into a list
# training_data_file = open("mnist_dataset/mnist_train.csv", 'r')
training_data_file = open("mnist_dataset/mnist_train_100.csv", 'r')
training_data_list = training_data_file.readlines()
training_data_file.close() 

print ("***** training_data_list 길이 :: ",len(training_data_list))
# train the neural network,

# go through all the records in the test data set
for record in training_data_list:
    # split the record by the ',' commas
    all_values = record.split(',')
    # correct answer is first value 첮번째 값이 라벨 = 정답 이므로,
    #correct_label = int(all_values[0])
    #print("\correct_label =\ ", correct_label)
    # scale and shift the inputs 입력될 값의 범위와 값을 조정 0.01~0.99,
    inputs = (numpy.asarray(all_values[1:], dtype=float) / 255.0 * 0.99) + 0.01
    
    targets = numpy.zeros(output_nodes) + 0.01
    # all_values[0] is the target label for this record,
    targets[int(all_values[0])] = 0.99
    n.train(inputs, targets)
    pass

print ("***** targets 내용 :: ",targets)

# load the mnist test data CSV file into a list
# test_data_file = open("mnist_dataset/mnist_test.csv", 'r')

test_data_file = open("mnist_dataset/mnist_test_10.csv", 'r')
test_data_list = test_data_file.readlines()
test_data_file.close()

print ("***** test_data_list 길이 :: ",len(test_data_list))

all_values = test_data_list[0].split(',')
print ("***** all_values[0] 내용 :: ",all_values[0])

image_array = numpy.asarray(all_values[1:], dtype=float).reshape((28,28))
matplotlib.pyplot.imshow(image_array, cmap='Greys', interpolation='None')

n.query((numpy.asarray(all_values[1:], dtype=float) / 255.0 * 0.99) + 0.01)

# test the neural network
# scorecard for how well the network performs, initially empty
scorecard = []      
for record in test_data_list:
    # split the record by the ',' commas
    all_values = record.split(',')
    correct_label = int(all_values[0])
    print("correct_label = ", correct_label)
    # scale and shift the inputs
    inputs = (numpy.asarray(all_values[1:], dtype=float) / 255.0 * 0.99) + 0.01
    # query the network
    outputs = n.query(inputs)
    # the index of the highest value corresponds to the label
    label = numpy.argmax(outputs)
    print("network's answer = ", label)
    # append correct or incorrect to list
    if (label == correct_label):
        # network's answer matches correct answer, add 1 to scorecard
        scorecard.append(1)
    else:
        # network's answer doesn't match correct answer, add 0 to scorecard
        scorecard.append(0)
        pass
    pass        

print ("scorecard 내용 :: ",scorecard)
# calculate the performance score, the fraction of correct answers
scorecard_array = numpy.asarray(scorecard)
print ("performance = ", scorecard_array.sum() / scorecard_array.size)  

