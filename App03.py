#!/usr/bin/env python
# coding: utf-8

# ### Personal Website Application
# 
# #### Building a Static Website

# In[56]:


#--------------------------------------------
# Import the applicable libraries
#--------------------------------------------
#import numpy as np
#i#mport pandas as pd

# Import flask class of objects from Flask library
from flask import Flask, render_template


# In[57]:


app  = Flask(__name__)  # Instantiate flask object. "__main__" is assigned to the __name__ variable

@app.route('/') # Output is mapped to the URL. '/' is localhost:5000
def home():
    return render_template("home.html")  # renders the html from the templates folder

@app.route('/about/') # Output is mapped to the URL. localhost:5000/about/
def about():
    return render_template("about.html")  # renders the html from the templates folder
#-------------------------------------------------------------------------------------------
# __name__ is '__main__' when running from this script. Will be another if importing from 
# a different script.
#-------------------------------------------------------------------------------------------
if __name__ == "__main__":  
    app.run(debug=True)
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




