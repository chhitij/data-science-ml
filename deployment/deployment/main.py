from logging import debug
from flask import Flask , render_template , request
import joblib

# behind the seen file will run main.py
app = Flask(__name__)

# load the modal 

model = joblib.load('hiring_model.pkl')

@app.route('/')
def welcome():
    return render_template('base.html')

@app.route('/contact')
def contact():
    return 'contact Page'

@app.route('/feedback')
def feedback():
    return 'feedBack Page'

@app.route('/predict', methods= ['POST'])
def predict():
    exp = request.form.get('experience')
    score = request.form.get('test_score')
    interview_score = request.form.get('interview_score')

    prediction = model.predict([[int(exp),int(score),int(interview_score)]])

    print(prediction)

    output = round(prediction[0],2)
    
    return render_template('base.html', prediction_text= f'Employee Salary will be $ {output}')


# debug = true for every change it will  run live watch mode
app.run(debug=True)