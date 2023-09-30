from flask import Flask, render_template, request
import numpy as np
import pickle
import pandas as pd

app = Flask(__name__)


model = pickle.load(open('Titanic.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    pclass = float(request.form['pclass'])
    sex = request.form['sex']
    age = float(request.form['age'])

    # Convert 'Sex' to numeric
    sex_numeric = 1 if sex == 'male' else 0

    if pclass =='1':
        pclass_1 = 1
    elif pclass =='2':
        pclass_1 =2
    else:
        pclass_1 = 3

    # Create a DataFrame for prediction
    data = pd.DataFrame({
        'Pclass': [pclass_1],
        'Sex': [sex_numeric],   
        'Age': [age]
    })

    # Make the prediction
    prediction = model.predict(data)
    if prediction[0] == 0:
        result = '!SORRY! You Are A Loser! You Cannot Survive'
        
    else:
        result = '!CONGRATULATIONS! You Are A Legend! You Can Survive'

    return render_template('result.html', prediction=result)


if __name__ == '__main__':
    app.run(debug=True)

