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

## Classification

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

## Types of Neural Networks

Hopfield:
- Every neuron in the network sends its output to all other neurons in the network. 

Feedforward:
- Multiple inputs.
- Series of signals propagating forward through layers of neurons
- e.g. Multilayer perceptron

Convolutional:
-  Takes in data, then creates modifications based on previously seen data. Then outputs these modifications to the original data. 

## Multilayer Perceptrons

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

My implementation:
self.layers => List with no. of neurons per layer
self.network => List of the perceptrons of each layer (starts at layer 1, as layer 0 has no neurons)
self.values => List of output values

## Training the Network

Fit types:
- Underfitting => Misclassifies too often 
- Just right => Rarely misclassifies and is generalised
- Overfitting => Never misclassifies but too ungeneralised

Datasets: 
- Collection of samples with features and labels {X,Y}
- Features = input data
- Labels = known categories of each sample
- 3 datasets:
	- Training
	- Validation
	- Testing
	
Training steps:
1. Feed input X
2. Compare output to correct label Y
3. Calculate error (overall and output errors)
4. Adjust weights for error

Mean square output error (MSOE) = sum((y-out)**2)/n , where n is no. of samples

Learning rate:
- Proportionalises the change in each weight. 
- Needs to be tuned depending on how fast weights are converging to result in desired output. 

Delta Rule:
- Method to find what to change the weight by. 
- delta(w) = learning_rate*output_error*input_value

Backpropagation algorithm:
1. Feed a sample to the network
2. Calculate MSOE
3. Calculate error term of each neuron
4. Calculate error term of each layer
5. Apply delta rule
6. Adjust weights