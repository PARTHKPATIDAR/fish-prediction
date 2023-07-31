from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
import joblib

app = Flask(__name__)

# Load your fish dataset
data = pd.read_csv('Fish.csv')

# Prepare the features and target
X = data.drop(columns=['Species'])
y = data['Species']

# Initialize the Decision Tree classifier and fit the model on the entire dataset
model = DecisionTreeClassifier()
model.fit(X, y)

# Save the model to a file
joblib.dump(model, 'fish_species_model.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the parameters from the request's JSON body
    data = request.json
    weight = float(data['Weight'])
    length1 = float(data['Length1'])
    length2 = float(data['Length2'])
    length3 = float(data['Length3'])
    height = float(data['Height'])
    width = float(data['Width'])

    # Convert the parameters to a NumPy array for prediction
    input_features = np.array([[weight, length1, length2, length3, height, width]])

    # Make the prediction using the loaded model
    species_id = model.predict(input_features)[0]

    # Using generic species labels
    species_label = f"Species {species_id}"

    # Return the prediction as a JSON response
    return jsonify({'species': species_label})

if __name__ == '__main__':
    app.run(debug=True)
