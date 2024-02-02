from enum import Enum
import math

class Activations(Enum):
    relu = 1
    sigmoid = 2
    
class Neuron:
    """Сlass that implements behavior similar to a nerve cell (neuron). Based on the mathematical model of the McCulloch—Pitts neuron"""
    
    inputs = [float]
    """Neuron input values"""
    weights = [float]
    """Neuron weights values"""
    activation = Activations.relu
    """Neuron activation function. Relu is default"""
    normalize = False
    """If true, neuron input values will normalized from 0 to 1"""
    output = .0
    """Neuron input values"""
    
    def __init__(self, inputs, weights, activation, normalize):
        """Inits new neuron"""
        self.inputs = inputs
        self.weights = weights
        self.activation = activation
        self.normalize = normalize
    
    def calculate(self):
        """Calculates output value for neuron"""
        weightedInputs = [float]
        self.output = 0
        if(len(self.inputs) == len(self.weights)):
            if(self.normalize):
                for i in range(0, len(self.inputs)):
                    self.inputs[i] = self.inputs[i] / float(len(self.inputs))
            weightedInputs = self.inputs
            for i in range(0, len(weightedInputs)):
                weightedInputs[i] *= self.weights[i]
                self.output += weightedInputs[i]
            if(self.activation == Activations.sigmoid):
                self.output = 1 / (1 + math.pow(math.e, -self.output))
            elif(self.activation == Activations.relu):
                if(self.output < 0):
                    self.output = 0
        else:
            print("Error: Arrays of input values and weights have different lengths")
                
                
            
        
                
                
            
            
    