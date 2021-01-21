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
from flask import Flask


# In[57]:


app  = Flask(__name__)
@app.route('/')
def home():
    return "Website content goes here!"

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




