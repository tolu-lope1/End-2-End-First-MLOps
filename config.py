dataset_url = "https://raw.githubusercontent.com/plotly/datasets/master/diabetes.csv"
train_path = "./model_data/train.csv"
test_path = "./model_data/test.csv"
split_size = 0.8
model_path = "./model_output/diabetes_model.pkl"
scaler_path = "./model_output/diabetes_scaler.pkl"
features = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
target = ['Outcome']
