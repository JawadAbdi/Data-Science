#!/usr/bin/env python
# coding: utf-8

# In[2]:


from bokeh.plotting import figure, show

# Create a new figure
p = figure(title="My Bokeh Plot", x_axis_label="X", y_axis_label="Y")

# Add glyphs to the figure
p.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=12, color='red', alpha=0.6)

# Customize the plot
p.title.text_color = "navy"
p.title.text_font_size = "16px"
p.xaxis.axis_label_text_font_style = "italic"
p.yaxis.major_label_text_color = "orange"

# Display the plot
show(p)


# In Bokeh, glyphs are the visual shapes or markers that are added to a plot to represent data points or other graphical elements. Glyphs can include circles, squares, lines, rectangles, patches, wedges, and more. They allow you to visually represent your data in a variety of ways.

# In[3]:


from bokeh.plotting import figure, show

# Create a new figure
p = figure(title="My Bokeh Plot", x_axis_label="X", y_axis_label="Y")

# Add circle and line glyphs to the figure
p.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=12, color='red', alpha=0.6)
p.line([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], line_color='blue', line_width=2)

# Customize the plot
p.title.text_color = "navy"
p.title.text_font_size = "16px"
p.xaxis.axis_label_text_font_style = "italic"
p.yaxis.major_label_text_color = "orange"

# Display the plot
show(p)


# In[4]:


from bokeh.plotting import figure, show

# Create a new figure
p = figure(title="My Bokeh Plot", x_axis_label="X", y_axis_label="Y")

# Customize the appearance
p.title.text_color = "navy"
p.title.text_font_size = "16px"
p.xaxis.axis_label_text_font_style = "italic"
p.yaxis.major_label_text_color = "orange"
p.xaxis.major_tick_line_color = "red"
p.yaxis.minor_tick_line_color = "green"
p.legend.label_text_font_size = "12px"
p.legend.label_text_color = "purple"

# Display the plot
show(p)


# In[5]:


from bokeh.plotting import figure, curdoc
from bokeh.models import Slider
from bokeh.layouts import column

# Create a new figure
p = figure()

# Define the initial plot
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]
p.line(x, y)

# Define the update function
def update_data(attr, old, new):
    # Get the updated value from the slider
    value = slider.value
    
    # Modify the data source or other plot properties
    p.line(x, [i * value for i in y])

# Create a slider widget
slider = Slider(title="Multiplier", start=1, end=10, step=0.1, value=1)
slider.on_change("value", update_data)

# Add the figure and slider to the document
curdoc().add_root(column(slider, p))


# In[6]:


from flask import Flask, render_template
from bokeh.plotting import figure
from bokeh.embed import components

app = Flask(__name__)

@app.route("/")
def index():
    # Create a Bokeh plot
    p = figure()
    p.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5])

    # Export the Bokeh plot
    script, div = components(p)

    # Render the HTML template with the Bokeh plot
    return render_template("index.html", plot_script=script, plot_div=div)


# In[7]:


from django.shortcuts import render
from bokeh.plotting import figure
from bokeh.embed import components

def index(request):
    # Create a Bokeh plot
    p = figure()
    p.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5])

    # Export the Bokeh plot
    script, div = components(p)

    # Render the template with the Bokeh plot
    return render(request, "index.html", {"plot_script": script, "plot_div": div})


# In[ ]:




