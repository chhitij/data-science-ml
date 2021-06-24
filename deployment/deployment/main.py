from logging import debug
from flask import Flask , render_template

# behind the seen file will run main.py
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('base.html')

@app.route('/contact')
def contact():
    return 'contact Page'

@app.route('/feedback')
def feedback():
    return 'feedBack Page'


# debug = true for every change it will  run live watch mode
app.run(debug=True)