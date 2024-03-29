from layerpy import Layer

class Network:
    "Contains a list of neuron layers"
    
    inputs: list
    """Input layer"""
    layers: list[Layer]
    """List of layers in neural network"""
    outputs: list
    """Network output value"""
    
    def __init__(self):
        self.inputs = []
        self.layers: list[Layer] = []
        self.outputs = []
        
    def __init__(self, layers):
        self.inputs = []
        self.layers: list[Layer] = layers
        self.outputs = []
    
    def __init__(self, layers, inputs):
        self.inputs = inputs
        self.layers: list[Layer] = layers
        self.outputs = []
    
    def calculate(self):
        """Calculates output values for network"""
        self.layers[0].set_inputs(self.inputs)
        
        for i in range(1, len(self.layers) - 1):
            self.layers[i].calculate()
            self.layers[i + 1].set_inputs(self.outputs)
        
        self.layers[len(self.layers) - 1].calculate()
        self.outputs = self.layers[len(self.layers) - 1].outputs
            