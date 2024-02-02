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

inputArray = []
print("Enter input values (3x3 array)")
for i in range(0,3):
    inputArray.append(input().split(","))
for arr in inputArray:
    for val in arr:
        inputValues.append(float(val))

leftLine = Neuron(inputValues, weightsL, Activations.sigmoid, False)
middleLine = Neuron(inputValues, weightsM, Activations.sigmoid, False)
rightLine = Neuron(inputValues, weightsR, Activations.sigmoid, True)

leftLine.calculate()
middleLine.calculate()
rightLine.calculate()


print(f"Predictions: \n Column 1: {leftLine.output} \n Column 2: {middleLine.output} \n Column 3: {rightLine.output}")

print("Press any key to exit")
input()
