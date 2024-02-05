from neuronpy import Neuron
from neuronpy import Activations


class Layer:
    """Contains a list of neurons"""

    neurons = []
    """List of neurons contained in layer"""
    outputs = []
    """List of output values of neurons contained in layer"""
    
    def setInputs(self, inputs):
        """Sets input values for layer"""
        for neuron in self.neurons:
            neuron.inputs = inputs
    
    def calculate(self):
        """Calculates output values for layer"""
        outputs = []
        for neuron in self.neurons:
            neuron.calculate()
            outputs.append(neuron.output)
            
            