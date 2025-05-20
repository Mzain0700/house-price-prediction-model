from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import pandas as pd
import os

app = Flask(__name__)

# Load the trained model
with open('house_price_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Load model info
with open('model_info.pkl', 'rb') as file:
    model_info = pickle.load(file)

# Load locations and cities
def load_options(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return [line.strip() for line in f.readlines()]
    return []

locations = load_options('static/data/locations.txt')
cities = load_options('static/data/cities.txt')

@app.route('/')
def home():
    return render_template('index.html', 
                          locations=locations, 
                          cities=cities,
                          model_name=model_info['model_name'],
                          accuracy=model_info['accuracy'])

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        property_type = request.form.get('property_type')
        city = request.form.get('city')
        location = request.form.get('location')
        bedrooms = int(request.form.get('bedrooms'))
        baths = int(request.form.get('baths'))
        size_marla = float(request.form.get('size_marla'))
        
        # Create a dataframe with the input data
        input_data = pd.DataFrame({
            'property_type': [property_type],
            'location': [location],
            'city': [city],
            'baths': [baths],
            'bedrooms': [bedrooms],
            'size_marla': [size_marla]
        })
        
        # Make prediction
        prediction = model.predict(input_data)
        
        # Ensure prediction is not negative
        prediction = max(0, prediction[0])
        
        # Format the prediction
        formatted_prediction = f"{prediction:,.2f}"
        
        return jsonify({
            'success': True,
            'prediction': formatted_prediction,
            'message': 'Prediction successful'
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'prediction': 0,
            'message': f'Error: {str(e)}'
        })

if __name__ == '__main__':
    app.run(debug=True)