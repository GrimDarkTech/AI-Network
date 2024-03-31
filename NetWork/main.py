from neuronpy import Neuron
from neuronpy import Activations

from layerpy import Layer  

from networkpy import Network

#Inits weights

weightsL = [0.1, -0.1, -0.3,
            0.2, -0.2, -0.101,
            0.3, -0.3, -0.125,
]
weightsM = [-0.12, 1.11, -1.1,
            -0.22, 0, -0.21,
            -0.563, 0.153, -0.41,
]
weightsR = [-0.1256, -0.222, 0.12,
            -0.45, -0.531, 0.2154,
            -0.374, -0.1253, 0.1454,
]

input_values = [0.1, 2, 0.1,
               0.2, 1, 0.2,
               0.1, 1, 0.1]

#Creating neurons

neurons = []

neuron = Neuron(input_values, weightsL, Activations.sigmoid, False)
neurons.append(neuron)

neuron = Neuron(input_values, weightsM, Activations.sigmoid, False)
neurons.append(neuron)

neuron = Neuron(input_values, weightsR, Activations.sigmoid, False)
neurons.append(neuron)

#Creating layers

layers = []

layer = Layer(neurons = neurons)
layers.append(layer)

layer = Layer(number_of_neurons = 5, number_of_inputs = 3, activation = Activations.sigmoid, normalize = False)
layers.append(layer)

layer = Layer(number_of_neurons = 1, number_of_inputs = 5, activation = Activations.sigmoid, normalize = False)
layers.append(layer)

#Creating network

network = Network(layers)
network.inputs = input_values


network.calculate()
print(network.outputs)

network.learn([0.66], 0.05, 1000)
network.calculate()

print(network.outputs)

print("Press any key to exit")
input()
