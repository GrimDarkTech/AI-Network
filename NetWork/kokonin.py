from neuronpy import Neuron
from neuronpy import Activations

from layerpy import Layer  

from networkpy import Network

inputValues = []

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

inputValues = [0, 0, 1,
              0, 0, 1,
              0, 0, 1]

neurons = []

leftLine = Neuron(inputValues, weightsL, Activations.sigmoid, False)
neurons.append(leftLine)

middleLine = Neuron(inputValues, weightsM, Activations.sigmoid, False)
neurons.append(middleLine)

rightLine = Neuron(inputValues, weightsR, Activations.sigmoid, False)
neurons.append(rightLine)

layer = Layer(neurons = neurons)

layer.calculate()
print(layer.outputs)

layer.calculate_kohonin()
print(layer.outputs)

print("Press any key to exit")
input()
