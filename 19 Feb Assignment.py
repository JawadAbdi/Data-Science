#!/usr/bin/env python
# coding: utf-8

# Flask was created by Armin Ronacher. Flask is considered a micro web framework is written in Python programming. The word “micro” means focusing to keep the core extensible but straightforward. It is not dependent upon external libraries to perform the tasks of a framework. Flask framework is more independent, flexible, and simple; so many developers prefer to start with Flask.
# 
# Lightweight: Flask is a lightweight framework because it is independent of external libraries and it gives a quick start for web development having complex applications.
# Compatible: Flask is compatible with the latest technologies such as machine learning, agile development, cloud technologies, etc.
# Independent: Flask allows full control to the developers for creating web applications. A developer can do the experiment with the libraries and architecture of the framework.
# Integrated Unit Testing: Flask offers an integrated unit testing feature that helps in faster debugging, robust development, and independence to do experiments.
# Flexible and Scalable: Flask supports WSGI templates that help in flexibility and scalability in the web development process.
# Secure Cookies: Secure cookie is an attribute of an HTTP request that enables the security of channels and ensures no unauthorized person has access to the text. Flask supports the feature of secure cookies. 

# In[ ]:


get_ipython().system('pip install flask')
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!!'

if __name__ == '__main__':
    app.run()


# In Flask, app routing refers to the process of mapping URLs (Uniform Resource Locators) to specific functions or views in your web application. It allows you to define different routes that correspond to different pages or actions within your application.
# 
# Flask uses a decorator called @app.route() to associate a URL with a function. The decorator specifies the URL pattern and HTTP methods that should trigger the execution of the associated function.

# In[ ]:


from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return 'Welcome to ABC Corporation'

@app.route('/')
def company_details():
    details = {
        'Company Name': 'ABC Corporation',
        'Location': 'India',
        'Contact Detail': '999-999-9999'
    }
    
    response = ""
    for key, value in details.items():
        response += f"{key}: {value}<br>"
    
    return response

if __name__ == '__main__':
    app.run()


# In Flask, the url_for() function is used for URL building. It allows you to generate URLs dynamically based on the route functions defined in your application.
# 
# The url_for() function takes the name of a view function as an argument and returns the corresponding URL for that function. It can also accept additional arguments if your route has dynamic components (e.g., /user/<username>).

# In[ ]:




