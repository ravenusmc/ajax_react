#Importing the required files 
from flask import Flask
from flask import Flask, jsonify, render_template, request

#Setting up Flask
app = Flask(__name__)
 
#This function will bring the user to the home page
@app.route("/")
def home():
    return render_template('home.html')

#This function is where I will be calculating the sum of the two numbers. 
@app.route('/_add_numbers', methods=['GET', 'POST'])
def add_numbers():
    a = request.form['a']
    b = request.form['b']
    print(a)
    return a
    # a = request.args.get('a', 0, type=int)
    # b = request.args.get('b', 0, type=int)
    # return jsonify(result=a + b)

#The functions for num and add_num are a new way to apply ajax to my site. Thus, the reason for the repitiion. 

@app.route("/num")
def num():
    return render_template('num.html')


@app.route('/add_num')
def add_num():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)


#This line will actually run the app.
if __name__ == '__main__':
    app.run(debug=True)