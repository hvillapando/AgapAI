# Python Flask Application

# Import necessary libraries
from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import joblib

# Initialize the Flask application
app = Flask(__name__)

# --- Mock Data and Model Loading (Replace with actual data/model loading) ---
# In a real application, you would load your trained model and actual data here.
# For this example, we'll use placeholder data and a mock prediction function.

mock_employees = [
    {"id": "001", "name": "Employee #001", "title": "Software Engineer", "department": "IT", "risk": "high", "score": 85, "tenure": 3.5, "factors": ["High workload", "Limited growth opportunities"], "actions": ["Schedule 1:1", "Mentorship program"]},
    {"id": "002", "name": "Employee #002", "title": "Branch Manager", "department": "Retail Banking", "risk": "medium", "score": 60, "tenure": 5.1, "factors": ["Recent team restructuring"], "actions": ["Compensation review"]},
    {"id": "003", "name": "Employee #003", "title": "UX Designer", "department": "Operations", "risk": "medium", "score": 55, "tenure": 1.2, "factors": ["New to company", "Limited project exposure"], "actions": ["Onboarding check-in", "Assign mentor"]}
]

def load_model():
    # This function would load your pre-trained ML model (e.g., using joblib.load)
    # For now, it's a placeholder.
    print("Loading mock ML model...")
    return "mock_model"

ml_model = load_model()

# --- Routes ---

@app.route('/')
def index():
    # Render the main HTML page
    return render_template('index.html')

@app.route('/analytics')
def analytics():
    # Render the analytics page
    return render_template('analytics.html')

@app.route('/reports')
def reports():
    # Render the reports page
    return render_template('reports.html')

@app.route('/actions')
def actions():
    # Render the action items page
    return render_template('actions.html')

@app.route('/settings')
def settings():
    # Render the settings page
    return render_template('settings.html')

@app.route('/api/employees')
def get_employees():
    # This endpoint would ideally fetch data from a database or a more complex data source.
    # For now, return the mock employee data.
    search_query = request.args.get('search', '').lower()
    department_filter = request.args.get('department', '').lower()
    risk_filter = request.args.get('risk', '').lower()

    filtered_employees = [emp for emp in mock_employees if
                          (search_query in emp['department'].lower() or search_query in emp['id'].lower() or search_query in emp['name'].lower())
                          and (department_filter == '' or emp['department'].lower() == department_filter)
                          and (risk_filter == '' or emp['risk'].lower() == risk_filter)
                         ]
    return jsonify(filtered_employees)

@app.route('/api/employee/<employee_id>')
def get_employee_detail(employee_id):
    employee = next((emp for emp in mock_employees if emp["id"] == employee_id), None)
    if employee:
        return jsonify(employee)
    return jsonify({"error": "Employee not found"}), 404

@app.route('/api/predict_risk', methods=['POST'])
def predict_risk():
    # This is a placeholder for your actual ML prediction endpoint.
    # You would receive employee data, preprocess it, and use your ML model to predict risk.
    data = request.json
    # Example: Preprocess data, make prediction with ml_model
    # For now, just return a mock prediction
    mock_prediction = {"risk_score": np.random.randint(20, 90), "risk_level": np.random.choice(["high", "medium", "low"])}
    return jsonify(mock_prediction)

# --- Run the application ---
if __name__ == '__main__':
    app.run(debug=True) 