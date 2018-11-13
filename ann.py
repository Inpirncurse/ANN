import random
import fileinput

#gives the initial random weights.
def random_weights(d):
    w = []
    for i in range(0, d + 1):
        w.append(random.random())
    return w

def main():
    #read file and grab info.
    file_input = fileinput.input()
    training_set = []
    test_example = []
    #read dimentionality (d), size of training set (m), size of test set (n).
    d = int(file_input[0])
    m = int(file_input[1])
    n = int(file_input[2])

    print("d:",d)
    print("m:",m)
    print("n:",n)
    
    #read to line 4 + m that are the training examples.
    for i in range(m):
        line = input().replace(" ", "")
        line = line.split(',')
        line = [float(i) for i in line]
        training_set.append(line)
    
    print("training_set:",training_set)
    
    #read 4 + m + 1 that are the test examples.
    for i in range(n):
        line = input().replace(" ", "")
        line = line.split(',')
        line = [float(i) for i in line]
        test_example.append(line)

    print("test_example:",test_example)

    print("random_weights:",random_weights(d))

if __name__ == '__main__':
    main()