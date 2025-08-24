import random
import math

# Sigmoid and its derivative
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Initialize weights and biases
def init_weights(rows, cols):
    return [[random.uniform(-1, 1) for _ in range(cols)] for _ in range(rows)]

def init_biases(size):
    return [random.uniform(-1, 1) for _ in range(size)]

# Dot product
def dot_product(a, b):
    return sum(x*y for x, y in zip(a, b))

# XOR input and output
X = [[0,0], [0,1], [1,0], [1,1]]
Y = [0, 1, 1, 0]

# Structure
input_size = 2
hidden_size = 2
output_size = 1
learning_rate = 0.5
epochs = 10000

# Initialize network parameters
W1 = init_weights(input_size, hidden_size)
B1 = init_biases(hidden_size)
W2 = init_weights(hidden_size, output_size)
B2 = init_biases(output_size)

# Training loop
for epoch in range(epochs):
    for i in range(len(X)):
        # Forward pass
        hidden_input = [dot_product(X[i], [W1[j][k] for j in range(input_size)]) + B1[k] for k in range(hidden_size)]
        hidden_output = [sigmoid(h) for h in hidden_input]

        final_input = [dot_product(hidden_output, [W2[j][k] for j in range(hidden_size)]) + B2[k] for k in range(output_size)]
        final_output = [sigmoid(f) for f in final_input]

        # Compute error
        error = Y[i] - final_output[0]

        # Backpropagation
        d_output = error * sigmoid_derivative(final_output[0])
        d_hidden = [d_output * W2[j][0] * sigmoid_derivative(hidden_output[j]) for j in range(hidden_size)]

        # Update weights and biases
        for j in range(hidden_size):
            for k in range(output_size):
                W2[j][k] += learning_rate * d_output * hidden_output[j]
        for k in range(output_size):
            B2[k] += learning_rate * d_output

        for j in range(input_size):
            for k in range(hidden_size):
                W1[j][k] += learning_rate * d_hidden[k] * X[i][j]
        for k in range(hidden_size):
            B1[k] += learning_rate * d_hidden[k]

# Testing
print("Predictions after training:")
for i in X:
    hidden_input = [dot_product(i, [W1[j][k] for j in range(input_size)]) + B1[k] for k in range(hidden_size)]
    hidden_output = [sigmoid(h) for h in hidden_input]
    final_input = [dot_product(hidden_output, [W2[j][k] for j in range(hidden_size)]) + B2[k] for k in range(output_size)]
    final_output = [sigmoid(f) for f in final_input]
    print(f"{i} => {round(final_output[0])}")