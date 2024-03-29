from layerpy import Layer

class Network:
    "Contains a list of neuron layers"
    
    inputs: list
    """Input layer"""
    layers: list
    """List of layers in neural network"""
    outputs: list
    """Network output value"""
    
    def __init__(self):
        self.layers = []
        self.outputs = []
        self.inputs = []

    def __init__(self, layers):
        self.layers = layers
        self.outputs = []
        self.inputs = []

    def calculate(self):
        """Calculates output values for network"""
        self.layers[0].set_inputs(self.inputs)
        self.layers[0].calculate()
        for i in range(1, len(self.layers) - 1):
            self.layers[i].calculate()
            self.layers[i + 1].set_inputs(self.outputs)
        self.outputs = self.layers[len(self.layers) - 1].outputs
            