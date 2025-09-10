import pickle

# Load the saved model
with open("salary_model.pkl", "rb") as file:
    model = pickle.load(file)

print("=== Employee Salary Prediction App ===")

# Collect inputs from user
emp_id = int(input("Enter Employee ID (any number): "))
experience = float(input("Enter years of experience: "))
age = float(input("Enter age: "))
gender = input("Enter gender (Male/Female): ").strip().lower()

# Encode gender (same way as during training)
gender_val = 1 if gender == "male" else 0

# Arrange features in same order as training
features = [[emp_id, experience, age, gender_val]]

# Predict salary
prediction = model.predict(features)

print(f"\nPredicted Salary: {prediction[0]:.2f}")
