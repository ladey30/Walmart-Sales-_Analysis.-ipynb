#!/usr/bin/env python
# coding: utf-8

# ### Project-Walmart_Sales Project
# By- Amarachi Ohabuiro
# Date-06/17/2023

# 
# ### About :
# The dataset contains Weekly_Sales information of 45 Walmart stores across different regions in the country.
# The purpose of this project is Exploratory Data Analysis(EDA), to determine if factors like, Temperature,Fuel price,holidays,unemployment and changes in customer price index, infleunce the weekly sales recorded.
# 
# This data from kaggle datasets download -d yasserh/walmart-dataset,updated a year ago.
# 

# #### Import Libraries

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_


# #### Process-
# I did some cleaning in Excel. I removed the dollar sign($) and Comma(,) from 'Weekly_Sales and 'Fuel_Price' columns by changing the data type to General.

# Import dataset

# In[ ]:


df=pd.read_csv('Walmart1.csv')
df


# In[7]:


df.info()


# In[8]:


df.head(10)


# In[9]:


df.tail(10)


# In[10]:


df.shape


# #### checking for nulls in dataset

# In[11]:


df.isnull().sum()


# In[12]:


df.nunique()


# #### Checking for outliers in the dataset by using  boxplot to identify them.

# In[3]:


df=pd.read_csv('Walmart1.csv')
sns.boxplot(df['Unemployment'])


# In[ ]:


df=pd.read_csv('Walmart1.csv')
sns.boxplot(df['Weekly_Sales'])


# In[4]:


df=pd.read_csv('Walmart1.csv')
sns.boxplot(df['Fuel_Price'])


# In[5]:


df=pd.read_csv('Walmart1.csv')
sns.boxplot(df['CPI'])


# In[6]:


df=pd.read_csv('Walmart1.csv')
sns.boxplot(df['Temperature'])


# In[2]:


df=pd.read_csv('Walmart1.csv')
sns.boxplot(df['Weekly_Sales'])


# #### As seen above 'Unempoyment' and 'Weekly_Sales' columns have outliers.
# #### Weekly_Sales outliers were off only in "Holiday_Flag.
# #### In other charts, "Weekly_Sales" corresponded with other variables.
# #### The lower outliers in "Unemployment" were recorded in store 4, while the 
# #### upper outliers were recorded by store 12 and 38.
# #### Further investigation can be carried out to detect the causes.

# In[45]:


df.loc[df["Unemployment"] <= 04.02]


# In[39]:


df.loc[df["Unemployment"] >= 11.000000]


# In[38]:


df.loc[df["Weekly_Sales"] >= 2700000]


# #### Sorting Values by 'weekly_Sales' to get the top stores with the highest weekly sales.
# #### Store 14 recorded the highest sales.

# In[13]:


df=df.sort_values(by='Weekly_Sales',ascending= False)
df


# #### Sorting values by 'weekly_Sales' to get the stores that registered the lowest weekly sales.
# #### Store 33 recorded the lowest weekly sales.

# In[14]:


df2=df.sort_values(by='Weekly_Sales')
df2


# #### Statistics Summary

# In[15]:


df.describe()


# In[16]:


df.corr()


# In[23]:


df1=df.groupby('Store').mean()
df1


# In[24]:


df3=df1[['Unemployment','CPI','Fuel_Price','Temperature']]
df3


# In[25]:


sns.heatmap(df3.corr(),annot=True)

plt.show()
           


# In[26]:


df3.plot()


# In[29]:


df4=df[["Store","Date","Weekly_Sales","Temperature"]]

df31=df4.sort_values(by ='Temperature',ascending = False)
df31


# In[30]:


df31.plot.scatter(x='Weekly_Sales',y='Temperature',s=200,c='Orange',title='Temperature Vs Weekly_Sales')


# In[31]:


df4=df[["Store","Date","Weekly_Sales","Unemployment"]]
df41=df4.sort_values(by ='Unemployment',ascending = False)
df41


# In[32]:


df41.plot.scatter(x='Weekly_Sales',y='Unemployment',s=200,c='Blue',title='Unemployment Vs Weekly_Sales')


# In[9]:


df5=df[["Store","Date","Weekly_Sales","Fuel_Price"]]
df51=df5.sort_values(by ='Fuel_Price',ascending = False)
df51


# In[ ]:





# In[10]:


df51.plot.scatter(x='Weekly_Sales',y='Fuel_Price',s=200,c='Red',title='Fuel Vs Weekly_Sales')


# In[12]:


df6=df[["Store","Date","Weekly_Sales","CPI"]]
df61=df6.sort_values(by ='CPI',ascending = False)
df61


# In[13]:


df61.plot.scatter(x='Weekly_Sales',y='CPI',s=200,c='Blue',title='CPI Vs Weekly_Sales')


# In[14]:


df7=df[["Store","Date","Weekly_Sales","Holiday_Flag"]]
df71=df7.sort_values(by ='Holiday_Flag',ascending = False)
df71


# In[15]:


df71.plot.scatter(x='Weekly_Sales',y='Holiday_Flag',s=200,c='Red',title='Holiday_Flag Vs Weekly_Sales')


# ### Summary:
# .The correlation table and and heat map,shows no correlation among variables, but as we view them in   .scatter plots, the following can be observed,
# . Highest sales were recorded when temperature was between 25 and 60 degrees,and sales was lowest when .temperate was 0 degrees.
# .Sales was between highest and average when employment was below 10, sales had a declining effect .above 10.
# .Theres a decline in sales when fuel price is higher than 4.00 dollars.Lower fuel price positively .impacts sales.
# .There is no significant relationship between CPI (Customer Price Index) and weekly sales.
# .There is a significant positive impact on sales on holidays.
# 
# 
