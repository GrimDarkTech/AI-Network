from neuronpy import Neuron
from neuronpy import Activations

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

leftLine = Neuron(inputValues, weightsL, Activations.sigmoid, False)
middleLine = Neuron(inputValues, weightsM, Activations.sigmoid, False)
rightLine = Neuron(inputValues, weightsR, Activations.sigmoid, False)

leftLine.calculate()
middleLine.calculate()
rightLine.calculate()


print(f"Predictions: \n Column 1: {leftLine.output} \n Column 2: {middleLine.output} \n Column 3: {rightLine.output}")

print("Press any key to exit")
input()
