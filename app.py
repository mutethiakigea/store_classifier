from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

# Initialize the Flask app
app = Flask(__name__)

# Load the trained model
with open('outlet_category_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define the category mapping
category_mapping = {0: 'Bronze', 1: 'Silver', 2: 'Gold'}

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route for making predictions
@app.route('/predict', methods=['POST'])
def predict():
    # Extracting input from the HTML form
    footflow = int(request.form['footflow'])
    amount_purchased = int(request.form['amount_purchased'])
    county = request.form['county']

    # Create a DataFrame for the input
    input_data = pd.DataFrame({
        'FootFlow': [footflow],
        'AmountPurchased': [amount_purchased],
        'County': [county]
    })

    # Make prediction using the trained model
    predicted_category_numeric = model.predict(input_data)[0]
    predicted_category_name = category_mapping[predicted_category_numeric]

    # Return the result to the front-end
    return render_template('result.html', prediction=predicted_category_name)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
