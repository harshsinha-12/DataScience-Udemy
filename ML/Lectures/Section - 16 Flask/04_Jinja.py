# Building URL Dynamically
# Variable Rule
# Jnja2 Template Engine

from flask import Flask, render_template, request , redirect, url_for
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

@app.route('/index', methods=['GET'])
def welcome_index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')



@app.route('/submit', methods = ['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return 'Hello ' + name
    return render_template('form.html')

# Variable Rule
@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score >= 50:
        res = "passed"
    else:
        res = "failed"

    return render_template('result.html', result = res)


@app.route('/successres/<int:score>')
def successres(score):
    res = ""
    if score >= 50:
        res = "passed"
    else:
        res = "failed"
    
    exp = {'score':score, 'res':res}

    return render_template('result1.html', result = exp)


@app.route('/fail/<int:score>')
def fail(score):


    return render_template('result.html', result = score)

@app.route('/submit2', methods = ['POST', 'GET'])
def submit2():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])

        total_score=(science+maths+c+data_science)/4
    else:
        return render_template('getresult.html')
    return redirect(url_for('successres',score=total_score))



# if condition
@app.route('/successif/<int:score>')
def successif(score):
    return render_template('result.html', result = score)


if __name__ == '__main__':
    app.run(debug=True) # This will run the Flask application on the development server.

# GET request is used to send data to the server.
# POST request is used to receive data from the server.

# There are ,ultiple ways to read the datafrom backed in the html page using jinja 2
# 1. Using double curly braces {{ }} for expressions
# Expression to print output in HTML
# 2. Using curly braces with percentage {%....%} for conditions and loops
# 3. Using curly braces with hash # for comments {#....#}
