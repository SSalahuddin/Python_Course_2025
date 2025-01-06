class AIModel:
    def __init__(self, name, algorithm):
        self.name = name
        self.algorithm = algorithm

    def train(self):
        print(f'Training {self.name} using {self.algorithm} algorithm.')

# Example
model = AIModel('Predictor', 'Linear Regression')
model.train()