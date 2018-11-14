import random
import fileinput

#gives the initial random weights.
def random_weights(d):
    w = []
    for i in range(0, d + 1):
        w.append(random.random())
    return w

# Training algorithm
def train(training_set, ex_outputs, test_example, weights, limit):
    learning_rate = 0.01
    error = True
    iter = 0
    # If there is an error, error = True
    while (error != False and iter < limit):
        error = False
        for i in range(0, len(training_set)):
            output = 0
            for j in range(0, len(training_set[i])):
                # Adition  function
                output += training_set[i][j] * weights[j]

            # Activation function
            if(output >= 0):
                output = 1
            else:
                output = 0

            # Get the error in the ouput to adjust the weights
            difference = ex_outputs[i] - output
            if (difference != 0):
                error = True

            # Adjust the weights with the difference and the learning rate
            for j in range(0, len(weights)):
                weights[j] += training_set[i][j] * difference * learning_rate
        iter += 1
    # If the while was broken due to excessive iterations, prints "No solution found"
    if (error != 0):
        print("no solution found")
    # If the while was broken due to the error being False, computes the test data
    else:
        test(test_example, weights)

# Test function that receives the test data and prints the output
def test(test_example, weights):
    for input in test_example:
        output = 0
        for i in range(0, len(input)):
            output += input[i] * weights[i]

        # Activation function
        if (output >= 0):
            print("1")
        else:
            print("0")

def main():
    #read file and grab info.
    file_input = fileinput.input()
    training_set = []
    test_example = []
    expected_outputs = []
    #read dimentionality (d), size of training set (m), size of test set (n).
    d = int(file_input[0])
    m = int(file_input[1])
    n = int(file_input[2])
    iterations = 0
    limit = 10000
    bias = 1.0

    #read to line 4 + m that are the training examples.
    for i in range(m):
        line = input().replace(" ", "")
        line = line.split(',')
        for i in range(0, len(line)):
            if(i == d):
                expected_outputs.append(float(line[i]))
                line[i] = bias
            else:
                line[i] = float(line[i])
        training_set.append(line)

    #read 4 + m + 1 that are the test examples.
    for i in range(n):
        line = input().replace(" ", "")
        line = line.split(',')
        line = [float(i) for i in line]
        line.append(bias)
        test_example.append(line)

    weights = random_weights(d)
    train(training_set, expected_outputs, test_example, weights, limit)

if __name__ == '__main__':
    main()
