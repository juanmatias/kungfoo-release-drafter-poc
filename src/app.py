#!/usr/bin/env python3

from flask import Flask

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'release drafter sample app'

@app.route('/about')
# ‘/’ URL is bound with hello_world() function.
def about_world():
    return 'this is the about'

@app.route('/useit')
# ‘/’ URL is bound with hello_world() function.
def useit():
    return 'this is some usefull function'


# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application
    # on the local development server.
    app.run()
