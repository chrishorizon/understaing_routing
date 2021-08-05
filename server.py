from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<user>')
def hi_user(user):
    print(user)
    return "Hi " + user + "!"
    # return f"Hi {name.capitalize()}!"

@app.route('/repeat/<int:number>/<string:word>')
def multiply(number, word):
    print(number)
    print(word)
    return word * number
    #return f"{word * number}"

if __name__ == '__main__':
    app.run(debug=True)