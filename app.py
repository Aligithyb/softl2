from flask import Flask, render_template, request

app = Flask(__name__)

# Home route to display the form
@app.route('/')
def index():
    return render_template('index.html')

# Submit route to handle form data
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    return f'Hello, {name}! Thanks for submitting the form.'

if __name__ == "__main__":
    app.run(debug=True)
