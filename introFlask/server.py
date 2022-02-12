from flask import Flask
# Create a new instance of the Flask class called "app"
app = Flask(__name__)



@app.route('/resource/<id>')
def variable_example(id):
    return f"requested resource with id {id}"

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def another_route():
    return 'Dojo!'

@app.route('/say/<id>')
def say_hi(id):
    return f"Hi {id} !"

@app.route('/repeat/<num>/<id>')
def repeat_hello(num, id):
    temp = ""
    for i in range (0, int(num)):
        temp += f"<h3>{id}</h3>"
    return temp
    ##make sure return is inteded correctly



# @app.route('/')
# def ():
#     return

if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
