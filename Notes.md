# Notes

## Choosing a Neural Network

3 paradigms of ML:
- Supervised learning
- Unsupervised Learning
- Reinforcement Learning

Supervised Learning:
- Regression
- Classification:
	
Unsupervised Learning:
- Clustering
- Anomaly detection

Reinforcement Learning:
- Video game playing AI

### Classification

Logistic Regression:
- Input vector with single return value between 0 or 1. 
- Binary classifier

K-nearest Neighbors:
- 2 clusters of data. 
- When a new, unknown, data sample is added, the algorithm determines its type using how many of its neighbors are of which type. 

Support Vector Machine (SVM):
- Constructs a line which divides 2 sets of data to minimise overlapping. 

Decision Trees:
- Go down a tree asking questions to classify data. Algorithm uses probability to make classification possible using the least number of questions. 

### Types of Neural Networks

Hopfield:
- Every neuron in the network sends its output to all other neurons in the network. 

Feedforward:
- Multiple inputs.
- Series of signals propagating forward through layers of neurons
- e.g. Multilayer perceptron

Convolutional:
-  Takes in data, then creates modifications based on previously seen data. Then outputs these modifications to the original data. 

### Multilayer Perceptrons

Consists of 3 layers:
1. Input 
2. Hidden (composed of neurons)
3. Output 

## Building blocks of NN's

Brain neurons:
- Dendrite => Take electrical signals 
- Nucleus => Processing of input occurs for an output
- Axon terminal => Output path to the desired location

Simple neuron model:
- Weighting of x_0 to x_n-1 inputs 
- Summing these inputs
- Need a bias term independent of inputs (x_n) to shift the line (i.e y intercept)
- Activation Function => Provide nonlinearity, constrain output value and model desired threshold behaviour

Activation functions:
- Binary step => u(x); 0 if x<0, 1 if x>=0.
- Logistic/Sigmoid => 1/(1+e^-x); all values between 0 and 1. 
- Hyperbolic tangent => tanh(x); all values between -1 and 1.  