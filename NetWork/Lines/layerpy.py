from neuronpy import Neuron
from neuronpy import Activations


class Layer:
    """Contains a list of neurons"""

    neurons: list
    """List of neurons contained in layer"""
    outputs: list
    """List of output values of neurons contained in layer"""
    
    def __init__(self):
        self.neurons = []
        self.outputs = []
        
    def __init__(self, neurons):
        self.neurons = neurons
        self.outputs = []
    
    def set_inputs(self, inputs: list):
        """Sets input values for layer"""
        for i in range(len(self.neurons)):
            self.neurons[i].inputs = inputs
    
    def calculate(self):
        """Calculates output values for layer"""
        self.outputs = []
        for neuron in self.neurons:
            neuron.calculate()
            self.outputs.append(neuron.output)
            
            