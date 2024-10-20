# Feed Forward Back propagation Neural Network 
# ●Implement the Feed Forward Back propagation algorithm to train a neural network
# ●Use a given dataset to train the neural network for a specific task

from doctest import OutputChecker
import numpy as np

class NeuralNetwork:
    def __init__(self):
        np.random.seed()
        self.synaptic_weights = 2 * np.random.random((3, 1)) - 1  # Initialize weights

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def train(self, training_inputs, training_outputs, training_iterations):
        for iteration in range(training_iterations):
            output = self.think(training_inputs)
            error = training_outputs - output
            adjustments = np.dot(training_inputs.T, error * self.sigmoid_derivative(output))  # Adjust weights
            self.synaptic_weights += adjustments

    def think(self, inputs):
        inputs = inputs.astype(float)
        output = self.sigmoid(np.dot(inputs, self.synaptic_weights))  # Compute output
        return output

if __name__ == "__main__":
    
    neural_network = NeuralNetwork()
    print("Beginning Randomly Generated Weights: ")
    print(neural_network.synaptic_weights)

    
    training_inputs = np.array([[0, 0, 1],[1, 1, 1], [1, 0, 1],[0, 1, 1]])
    training_outputs = np.array([[0], [1], [1], [0]])

    neural_network.train(training_inputs, training_outputs, 15000)
    print("Ending Weights After Training: ")
    print(neural_network.synaptic_weights)

    user_input_one = float(input("User Input One: "))
    user_input_two = float(input("User Input Two: "))
    user_input_three = float(input("User Input Three: "))
    print("Considering New Situation: ", user_input_one, user_input_two, user_input_three)

    user_input = np.array([[user_input_one, user_input_two, user_input_three]])
    print("New Output data: ")
    print(neural_network.think(user_input))


# Feed Forward Backpropagation Neural Network - Short Answer:

# A Feed Forward Backpropagation Neural Network is a type of artificial neural network where data flows in one direction—from input to output—and errors are propagated backward to update the network's weights.

# Feed Forward Process:
# Input Layer: Data is fed into the input nodes.
# Hidden Layers: The input data passes through one or more hidden layers, where neurons apply an activation function (like ReLU or Sigmoid) to introduce non-linearity.
# Output Layer: The final output is generated, representing predictions or classifications.
# Backpropagation Process:
# Error Calculation: After the output is generated, the error (difference between predicted and actual output) is computed using a loss function (e.g., Mean Squared Error for regression).
# Weight Adjustment: The error is propagated backward through the network. Using the gradient descent algorithm, the weights of the connections are updated to minimize the error.
# Repeat: This process of forward pass and backpropagation continues until the network learns and the error converges to a minimum.
# Use Case: Feed Forward Backpropagation is widely used in applications like image recognition, natural language processing, and predictive modeling.
