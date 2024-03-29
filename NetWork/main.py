from neuronpy import Neuron
from neuronpy import Activations

import layerpy

import networkpy

#Inits weights

weightsL = [1, -0.1, -1,
            1, -0.1, -1,
            1, -0.1, -1,
]
weightsM = [-0.1, 1, -0.1,
            -0.1, 1, -0.1,
            -0.1, 1, -0.1,
]
weightsR = [-1, -0.1, 1,
            -1, -0.1, 1,
            -1, -0.1, 1,
]

input_values = [1, 1, 1,
               1, 1, 1,
               1, 1, 1]

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

layer = layerpy.Layer(neurons)

layers.append(layer)

#Creating network

network = networkpy.Network(layers)
network.inputs = input_values

network.calculate()

print(network.outputs)

print("Press any key to exit")
input()
