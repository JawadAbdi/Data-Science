#!/usr/bin/env python
# coding: utf-8

# The GET method is limited to a maximum number of characters, while the POST method has no such limitation. This is because the GET method sends data through the resource URL, which is limited in length, while the POST method sends data through the HTTP message body, which has no such limitation.

# The Request, in Flask, is an object that contains all the data sent from the Client to Server. This data can be recovered using the GET/POST Methods.

# Flask redirect is defined as a function or utility in Flask which allows developers to redirect users to a specified URL and assign a specified status code. When this function is called, a response object is returned, and the redirection happens to the target location with the status code.

# Templates are files that contain static data as well as placeholders for dynamic data. A template is rendered with specific data to produce a final document.
# render_template is a Flask function from the flask. templating package. render_template is used to generate output from a template file based on the Jinja2 engine that is found in the application's templates folder. Note that render_template is typically imported directly from the flask package instead of from flask.

# In[ ]:


from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def hello():
    response = {'message': 'Hello, world!'}
    return jsonify(response)

if __name__ == '__main__':
    app.run()


# In[ ]:




