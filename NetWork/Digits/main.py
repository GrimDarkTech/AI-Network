from neuronpy import Neuron
from neuronpy import Activations

import layerpy
import networkpy

import cv2

inputValues = []

image = cv2.imread('Test2.png', cv2.IMREAD_GRAYSCALE)

height, width = image.shape

for y in range(height):
    for x in range(width):
        pixel = image[y, x]
        inputValues.append(1 - (pixel / 255))

cv2.imshow('Image', cv2.resize(image, (width * 50, height * 50), interpolation = cv2.INTER_AREA))
cv2.waitKey(0)
cv2.destroyAllWindows()


one_weight = [-5, -5, -1, 0.5, 1,
              -5, -5, -1, 1, 1,
              -5, -5, -1, 0, 1,
              -5, -5, -1, 0, 1,
              -5, -5, -1, 0.5, 1
              ]

two_weight = [-1, 1, 1, 1, 0,
              -1, -0.5, 0, 0, 1,
              -1, -0.5, 0, 1, 0,
              -1, -0.5, 1, 0, 0,
              -1, 1, 1, 1, 1
              ]

three_weight = [-0.5, 1, 1, 1, 0,
              -1, 0, 0, 0, 1,
              -1, 0.1, 0.5, 1, 0,
              -1, 0, 0, 0, 1,
              -0.5, 1, 1, 1, 0
              ]

four_weight = [-1, 1, 0.5, -0.3, 1,
              -1, 1, 0.5, -1, 1,
              -1, 1, 1, 1, 1,
              -1, 0, 0, 0.2, 1,
              -1, -1, -1, 0.2, 1
              ]

neurons = []

neuron = Neuron(one_weight, Activations.sigmoid, False)
neurons.append(neuron)

neuron = Neuron(two_weight, Activations.sigmoid, False)
neurons.append(neuron)

neuron = Neuron(three_weight, Activations.sigmoid, False)
neurons.append(neuron)

neuron = Neuron(four_weight, Activations.sigmoid, False)
neurons.append(neuron)

layers = []

layer = layerpy.Layer(neurons)
layers.append(layer)

network = networkpy.Network(layers, inputValues)

network.calculate()

print(network.outputs)

print("Press any key to exit")
input()
