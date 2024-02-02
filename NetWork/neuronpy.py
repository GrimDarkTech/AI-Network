from enum import Enum
import math

class Activations(Enum):
    relu = 1
    sigmoid = 2
    
class Neuron:
    """Сlass that implements behavior similar to a nerve cell (neuron). Based on the mathematical model of the McCulloch—Pitts neuron"""
    
    inputs = [float]
    weights = [float]
    activation = Activations.relu
    output = .0
    
    def __init__(self, inputs, weights, activation):
        self.inputs = inputs
        self.weights = weights
        self.activation = activation
    
    def calculate(self):
        weightedInputs = [float]
        self.output = 0
        if(len(self.inputs) == len(self.weights)):
            weightedInputs = self.inputs
            for i in range(0, len(weightedInputs)):
                weightedInputs[i] *= self.weights[i]
                self.output += weightedInputs[i]
        if(self.activation == Activations.sigmoid):
            self.output = 1 / (1 + math.pow(math.e, -self.output))
        elif(self.activation == Activations.relu):
            if(self.output < 0):
                self.output = 0
                
                
            
        
                
                
            
            
    