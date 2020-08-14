#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from pydataset import data
import matplotlib.pyplot as plt


# ### 1. Load the mpg dataset. Read the documentation for it, and use the data to answer these questions

# In[2]:


mpg = data('mpg')
mpg.head()


# ### 1-1. On average, which manufacturer has the best miles per gallon?

# In[3]:


# Calculate the mean of city and highway mileages

avereage_mileages = (mpg.cty + mpg.hwy)/2
avereage_mileages


# In[4]:


# Add the average_mileages as a new column

mpg['avereage_mileages'] = avereage_mileages
mpg


# In[5]:


# Groupby manufacturera and calculate the mean of avereage mileages of all its models

manufacturer_mileages = mpg.groupby('manufacturer').avereage_mileages.mean()
manufacturer_mileages


# In[6]:


# Find out which manufacturer has the best miles per gallon?

manufacturer_mileages.nlargest(n=1,keep='all')


# ### 1-2. How many different manufacturers are there?

# In[7]:


manufacturer_mileages.size


# In[8]:


mpg.manufacturer.value_counts().size


# In[9]:


mpg_manufacturer = pd.DataFrame(mpg.groupby('manufacturer'))
mpg_manufacturer.shape[0]


# ### 1-3. How many different models are there?

# In[10]:


mpg.model.value_counts().size


# ### 1-4. Do automatic or manual cars have better miles per gallon?

# In[11]:


trans_mileages = mpg.groupby('trans').avereage_mileages.mean()
trans_mileages


# In[12]:


auto_mileages = trans_mileages.loc['auto(av)':'auto(s6)'].mean()
auto_mileages


# In[13]:


man_mileages = trans_mileages.loc['manual(m5)':'manual(m6)'].mean()
man_mileages


# ### 2. Joining and Merging
# 
# Copy the users and roles dataframes from the examples above. What do you think a right join would look like? An outer join? What happens if you drop the foreign keys from the dataframes and try to merge them?

# In[14]:


users = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]
})
users


# In[15]:


roles = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['admin', 'author', 'reviewer', 'commenter']
})
roles


# ### users right join roles

# In[16]:


pd.merge(users, roles, left_on = 'role_id', right_on = 'id', how = 'right')


# ### users outer join roles

# In[17]:


pd.merge(users, roles, left_on = 'role_id', right_on = 'id', how = 'outer')


# ### If the foreign key, the role_id is dropped, What will the users and roles join on? 

# ### 3. Getting data from SQL databases

# ### 1. Create a function named get_db_url. It should accept a username, hostname, password, and database name and return a url formatted like in the examples in this lesson.

# In[18]:


from env import host, user, password

url = f'mysql+pymysql://{user}:{password}@{host}'
    
get_db_url = f'mysql+pymysql://{user}:{password}@{host}/employees'


# ### 2. Use your function to obtain a connection to the employees database.

# In[20]:


query = 'show tables'

pd.read_sql(query, get_db_url)


# ### 3. Once you have successfully run a query:
# ### Intentionally make a typo in the database url. What kind of error message do you see?
# Name Error

# In[ ]:


# get_db_url_typo = f'mysql+pymysql://{user}:{bassword}@{host}/employees'
    
# query = 'show tables'

# pd.read_sql(query, get_db_url_typo)


# ### Intentionally make an error in your SQL query. What does the error message look like?
# 
# ProgrammingError

# In[ ]:


# get_db_url = f'mysql+pymysql://{user}:{password}@{host}/employees'
    
# query_typo = 'show table'

# pd.read_sql(query_typo, url_employees)


# ### 4. Read the employees and titles tables into two separate dataframes

# In[22]:


query = 'select * from employees'
employees = pd.read_sql(query, get_db_url)

employees.head()


# In[23]:


query = 'select * from titles'
titles = pd.read_sql(query, get_db_url)

titles.head()


# ### 5. Visualize the number of employees with each title.

# In[24]:


employee_number_under_title = titles.groupby('title').title.count()
employee_number_under_title


# In[25]:


employee_number_under_title.plot(kind = 'barh')
plt.title("Number of employees under each title")
plt.xlabel("Number of employees")


# ### 6. Join the employees and titles dataframes together.

# In[26]:


em_join_ti = pd.merge(employees, titles, left_on = 'emp_no', right_on = 'emp_no', how = 'inner')
em_join_ti.head()


# ### 7. Visualize how frequently employees change titles.

# In[27]:


em_change_ti = em_join_ti.groupby('emp_no').title.count()
em_change_ti


# In[28]:


em_change_ti.value_counts(normalize = True)


# In[29]:


em_change_ti.value_counts(normalize = True).plot.bar()

plt.title("How frequently employees change titles")
plt.xticks(rotation=0)
plt.ylabel("Percentage of Employees")
plt.xlabel("Number of Titles Empolyees Owned")


# ### 8. For each title, find the hire date of the employee that was hired most recently with that title.

# In[30]:


em_join_ti.groupby('title').hire_date.max()


# ### 9. Write the code necessary to create a cross tabulation of the number of titles by department. (Hint: this will involve a combination of SQL and python/pandas code)

# In[31]:


query = """select dept_name, title from departments join dept_emp using(dept_no) join titles using(emp_no)"""

dep_title = pd.read_sql(query, get_db_url)
dep_title.head()


# In[32]:


pd.crosstab(dep_title.dept_name, dep_title.title)


# ### 4. Use your get_db_url function to help you explore the data from the chipotle database. Use the data to answer the following questions

# In[33]:


query = 'show tables'

url_chipotle = f'mysql+pymysql://{user}:{password}@{host}/chipotle'
    
pd.read_sql(query, url_chipotle)


# In[34]:


query = 'select * from orders'
orders = pd.read_sql(query, url_chipotle)

orders.head()


# ### 4-1. What is the total price for each order?

# In[35]:


orders['item_price'] = orders.item_price.apply(lambda i: float(i[1:-1]))
orders.head()


# In[36]:


orders.groupby('order_id').item_price.sum()


# ### 4-2. What are the most popular 3 items?

# In[37]:


orders.groupby('item_name').item_name.count().nlargest(n=3,keep='all')


# ### 4-3. Which item has produced the most revenue?

# In[38]:


orders['item_total_price'] = orders.quantity * orders.item_price
orders.head()


# In[39]:


orders.groupby('item_name').item_total_price.sum().nlargest(n=1,keep='all')


# In[ ]:




