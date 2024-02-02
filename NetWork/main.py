from neuronpy import Neuron
from neuronpy import Activations

input = [1, 0, 0,
          1, 0, 0,
          1, 0, 0
]

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

leftLine = Neuron(input, weightsL, Activations.sigmoid)
middleLine = Neuron(input, weightsM, Activations.sigmoid)
rightLine = Neuron(input, weightsR, Activations.sigmoid)

leftLine.calculate()
middleLine.calculate()
rightLine.calculate()


print(f"Вероятности: \n Первый столбец: {leftLine.output} \n Второй столбец: {middleLine.output} \n Третий столбец: {rightLine.output}")
