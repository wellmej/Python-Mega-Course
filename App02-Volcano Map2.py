#!/usr/bin/env python
# coding: utf-8

# #### Build a web map for volcanos

# In[4]:


#--------------------------------------------
# Import the applicable libraries
#--------------------------------------------
import numpy as np
import pandas as pd
import folium


# In[12]:


folder_name = 'C:/Users/jrwel/Documents/Udemy/Python Mega Course/Data/App02-Volcano Map/'
file_name = 'Map2.html'
image_file = folder_name + file_name


# In[13]:


#--------------------------------------------
#  Save map image
#--------------------------------------------
map.save(image_file)


# In[ ]:


TILES = "Stamen Terrain"
map = folium.Map(location=[39.97199, -83.00275], zoom_start=10.5, tiles=TILES)
map


# In[38]:


#---------------------------------
# Iterating thru two lists
#---------------------------------
lat = [1, 2, 3]
lon = [4, 5, 6]
for lt, ln in zip(lat, lon):
    print (lt, " and ", ln)


# In[37]:


#-----------------------------------------------------------
# Read Volcano information location file
#-----------------------------------------------------------
folder_name = 'C:/Users/jrwel/Documents/Udemy/Python Mega Course/Data/App02-Volcano Map/'
file_name = 'Volcanoes.txt'
data_file = folder_name + file_name
data = pd.read_csv(data_file)
#data.head(10)


# In[41]:


#------------------------------------------
#  Iterate thru data to add volcanoes
#------------------------------------------
map = folium.Map(location=[39.3, -111.7], zoom_start=6, tiles=TILES)
fg = folium.FeatureGroup(name="My Map")
lat = list(data["LAT"])
lon = list(data["LON"])
for lt, ln in zip(lat, lon):
    fg.add_child(folium.Marker(location=[lt, ln], popup="Volcano", icon=folium.Icon(color='red')))
map.add_child(fg)

#--------------------------------------------
#  Save map image
#--------------------------------------------
map.save(image_file)

#--------------------------------------------
#  Show map image
#--------------------------------------------
map


# In[ ]:





# In[ ]:




