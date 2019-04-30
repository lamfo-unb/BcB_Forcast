from flask import Flask
from flask import render_template
import graphs

app = Flask(__name__)

@app.route('/')
def home():
    bar = graphs.create_plot('2019-03-22', 'IGP-DI')
    return render_template('index.html', plot=bar)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', titulo="Home")


app.run(debug=True)
