
# Step function (activation)
def step(x):
    return 1 if x >= 0 else 0

# Train Perceptron
def train_gate(inputs, outputs, learning_rate=0.1, epochs=10):
    weights = [0, 0]  # Two inputs
    bias = 0

    for _ in range(epochs):
        for x, y in zip(inputs, outputs):
            # Weighted sum
            z = sum(xi * wi for xi, wi in zip(x, weights)) + bias
            pred = step(z)
            error = y - pred

            # Update weights and bias
            weights = [w + learning_rate * error * xi for w, xi in zip(weights, x)]
            bias += learning_rate * error

    return weights, bias

# Predict function
def predict(inputs, weights, bias):
    results = []
    for x in inputs:
        z = sum(xi * wi for xi, wi in zip(x, weights)) + bias
        results.append(step(z))
    return results

# Input and expected outputs
X = [[0, 0], [0, 1], [1, 0], [1, 1]]
Y_and = [0, 0, 0, 1]
Y_or  = [0, 1, 1, 1]

# Train models
w_and, b_and = train_gate(X, Y_and)
w_or, b_or = train_gate(X, Y_or)

# Predictions
print("AND Gate:")
for x, y in zip(X, predict(X, w_and, b_and)):
    print(f"{x} => {y}")

print("\nOR Gate:")
for x, y in zip(X, predict(X, w_or, b_or)):
    print(f"{x} => {y}")
