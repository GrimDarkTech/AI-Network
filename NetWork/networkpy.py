from layerpy import Layer

class Network:
    "Contains a list of neuron layers"
    
    inputs = []
    """Input layer"""
    layers = []
    """List of layers in neural network"""
    outputs = []
    """Network output value"""
    
    def calculate(self):
        """Calculates output values for network"""
        self.layers[0].setInputs(self.inputs)
        for i in range(1, len(self.layers) - 1):
            self.layers[i].calculate()
            self.layers[i + 1].setInputs(self.outputs)
        self.layers[len(self.layers) - 1]
        self.outputs = self.layers.outputs
            