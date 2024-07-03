#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


data=pd.read_csv(r'C:\Users\Lenovo\OneDrive\Documents\ANJALI DOCUMENTS\ANALYTICS\GOOGLE PLAY STORE\googleplaystore.csv\googleplaystore.csv')


# # Top 5 rows of the dataset

# In[5]:


data.head()


# # Last 3 rows of the dataset 

# In[6]:


data.tail(3)


# #  Shape of the dataset(number of rows and number of columns)

# In[7]:


data.shape


# In[8]:


print("Number of rows ",data.shape[0])
print("Number of columns ",data.shape[1])


# #  Get Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement

# In[9]:


data.info()


# # Get Overall Statistics About The Dataframe

# In[11]:


data.describe(include="all")


# # Total Number of App Titles Contain Astrology

# In[14]:


data.columns


# In[15]:


data['App']


# In[19]:


data['App'].str.contains('Astrology')  #case sensitive -Astrology


# In[20]:


data['App'].str.contains('Astrology',case=False)  #case insensitive


# In[21]:


data[data['App'].str.contains('Astrology',case=False)]


# In[22]:


len(data[data['App'].str.contains('Astrology',case=False)])


# # Find Average App Rating

# In[23]:


data.columns


# In[24]:


data['Rating']


# In[25]:


data['Rating'].mean()


# # Find Total Number of Unique Category

# In[26]:


data.columns


# In[27]:


data['Category']


# In[28]:


data['Category'].unique()


# In[29]:


len(data['Category'].unique())


# In[30]:


data['Category'].nunique()


# # Which Category Getting The Highest Average Rating? 

# In[31]:


data.columns


# In[32]:


data.groupby('Category')['Rating'].mean().sort_values(ascending=False)


# # Find Total Number of App having 5 Star Rating

# In[33]:


data.columns


# In[34]:


data['Rating']


# In[35]:


data['Rating']==5.0


# In[36]:


data[data['Rating']==5.0]


# In[38]:


len(data[data['Rating']==5.0])


# # Find Average Value of Reviews

# In[39]:


data.columns


# In[40]:


data['Reviews']


# In[43]:


data['Reviews'].dtype


# In[44]:


data['Reviews'].astype('float')


# In[46]:


data['Reviews']=data['Reviews'].replace('3.0M','3.0')


# In[48]:


data['Reviews']=data['Reviews'].astype('float')


# In[49]:


data['Reviews'].mean()


# # Find Total Number of Free and Paid Apps 

# In[50]:


data.columns


# In[54]:


data['Type'].value_counts()


# #  Which App Has Maximum Reviews?

# In[73]:


data.groupby('App')['Reviews'].max().sort_values(ascending=False)


# In[70]:


data[data['Reviews'].max()==data['Reviews']]['App']


# # Display Top 5 Apps Having Highest Reviews

# In[74]:


data.groupby('App')['Reviews'].max().sort_values(ascending=False).head()


# In[76]:


index=data['Reviews'].sort_values(ascending=False).head().index


# In[77]:


data.iloc[index]['App']


# #  Find Average Rating of Free and Paid Apps

# In[78]:


data.columns


# In[79]:


data['Type'].value_counts()


# In[80]:


data.groupby('Type')['Rating'].mean()


# #  Display Top  5 Apps Having Maximum Installs

# In[81]:


data.columns


# In[87]:


data['Installs'].dtype


# In[88]:


data['Installs']


# In[89]:


data['Installs_1']=data['Installs'].str.replace(',','')


# In[90]:


data['Installs_1']


# In[91]:


data['Installs_1']=data['Installs_1'].str.replace('+','')


# In[92]:


data['Installs_1']


# In[93]:


data.columns


# In[94]:


data[data['Installs_1']=='Free']


# In[98]:


data['Installs_1']=data['Installs_1'].str.replace('Free','0')


# In[99]:


data['Installs_1']


# In[100]:


data.loc[10472]


# In[101]:


data['Installs']=data['Installs'].str.replace('Free','0')


# In[102]:


data['Installs']


# In[103]:


data.loc[10472]


# In[104]:


data['Installs_1'].dtype


# In[112]:


data['Installs_1']=data['Installs_1'].astype('float')


# In[113]:


index=data['Installs_1'].sort_values(ascending=False).head().index


# In[114]:


data.iloc[index]['App']


# In[ ]:




