#Importing the required files 
from flask import Flask
from flask import render_template

#Setting up Flask
app = Flask(__name__)
 
#This function will bring the user to the home page
@app.route("/")
def home():
    return render_template('home.html')

 
#This line will actually run the app.
if __name__ == '__main__':
    app.run(debug=True)