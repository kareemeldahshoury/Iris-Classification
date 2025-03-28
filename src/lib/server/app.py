from flask import Flask, request, jsonify
from flask_cors import CORS
import torch
import numpy as np
import torch.nn as nn
import torch.nn.functional as F

# This is the structure of the NN
class Model(nn.Module):
  # Input layes(4 types of flowers) -->
  # Hidden Layer 1 (number of neurons) -->
  # Hidden Layer 2 (number of neurons) -->
  # output (3 classes of irises)
  def __init__(self, in_features = 4, h1=8, h2=9, out=3):
    super().__init__() # instantiates our nn.Module
    self.fc1 = nn.Linear(in_features, h1)
    self.fc2 = nn.Linear(h1, h2)
    self.out = nn.Linear(h2, out)

  def forward(self, x):
    x = F.relu(self.fc1(x))
    x = F.relu(self.fc2(x))
    x = F.relu(self.out(x))
    return x
  
# Load your PyTorch model
torch.manual_seed(42)

model = Model()
model.load_state_dict(torch.load('../../../static/iris_neural_network.pt'))
model.eval()

app = Flask(__name__)
CORS(app, resources={r"/predict": {"origins": ["https://www.flowerprediction.com"], "methods": ["POST"]}})

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        inputs = np.array(data['inputs'], dtype=np.float32) # makes sure the inputs are in the format of the model
        inputs = torch.tensor(inputs).unsqueeze(0)  # Add batch dimension
        
        # Runs the inputs in the model
        with torch.no_grad(): 
            outputs = model(inputs)
            predicted_class = torch.argmax(outputs).item()
        
        if predicted_class == 0:
            return jsonify({'prediction': "Setosa"})
        elif predicted_class == 1:
            return jsonify({'prediction': "Versicolor"})
        else:
            return jsonify({'prediction': "Virginica"})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)