from flask import Flask, render_template
# Flask is a web framework that provides some tools to make web development easier.
"""
It creates an instance of the Flask class for our web application.
which will be the WSGI (Web Server Gateway Interface) application.
"""
# WSGI Application: 
#It is a specification that describes how a web server communicates with web applications, 
# and how web applications can be chained together to process one request.

app = Flask(__name__)

@app.route('/') # This is a decorator that creates a mapping between the 
                    # URL and the function.
def welcome():
    return " <html> <h1> Welcome to the Flask World This is Harsh! This is the first Flask App. Hi! </h1></html>" 

@app.route('/index')
def welcome_index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True) # This will run the Flask application on the development server.