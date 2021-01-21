#!/usr/bin/env python
# coding: utf-8

# ### Personal Website Application
# 
# #### Building a Static Website

# In[56]:


#--------------------------------------------
# Import the applicable libraries
#--------------------------------------------
import numpy as np
import pandas as pd
from flask import Flask  # Import flask class of objects from Flask library


# In[57]:


app  = Flask(__name__)  # Instantiate flask object. "__main__" is assigned to the __name__ variable

@app.route('/') # Output is mapped to the URL. '/' is localhost:5000
def home():
    return "This is the static Homepage: localhost:5000"

@app.route('/about/')  # Output is mapped to the URL. localhost:5000/about/
def about(): 
    return "This is the about page"

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




