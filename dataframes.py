#!/usr/bin/env python
# coding: utf-8

# For several of the following exercises, you'll need to load several datasets using the pydataset library. (If you get an error when trying to run the import below, use pip to install the pydataset package.)
# 
# `from pydataset import data`
# 
# When the instructions say to load a dataset, you can pass the name of the dataset as a string to the `data` function to load the dataset. You can also view the documentation for the data set by passing the `show_doc` keyword argument.

# In[1]:


import pandas as pd
import numpy as np
from pydataset import data


# ### Load the dataset and store it in a variable by `data()`

# In[2]:


mpg = data('mpg')
mpg.head()


# ### View the documentation for the dataset

# In[3]:


mpg_doc = data('mpg', show_doc=True)
mpg_doc


# ### 1. Copy the code from the lesson to create a dataframe full of student grades.

# In[4]:


np.random.seed(123)

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# randomly generate scores for each student for each subject
# note that all the values need to have the same length here

math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})

df


# ### 1-1. Create a column named passing_english that indicates whether each student has a passing grade in reading.

# In[5]:


# Find out the data ypte for each column

df.info()


# In[6]:


# Create a mask that indicates whether each student pass the reading exam or not 
# Assuming 60 is the passing grade

df.reading >= 90

# Add the boolean series as a new column without modifing the original data

df_passing_reading = df.assign(passing_reading = df.reading >= 90)

# Output the new table

df_passing_reading


# ### Convert boolean values in passing_english column to pass or fail

# In[7]:


# Create a varible reading_boolean to hold the boolean value for English grades
reading_boolen = df.reading >= 90


# Convert boolean values to Pass or Fail
reading_passing_grade = reading_boolen.apply(lambda i: "Pass" if i == True else "Fail")


# Add the P or F to the new column named passing_english
df_reading_p_or_f = df.assign(passing_reading = reading_passing_grade)


# Output the new table
df_reading_p_or_f


# ### 2. Sort the english grades by the passing_english column. How are duplicates handled?
# - The duplicates are sorted by integer index

# In[8]:


df_reading_p_or_f.sort_values(by = 'passing_reading')


# In[9]:


df_reading_p_or_f.sort_values(by = 'passing_reading', ascending = False)


# ### 3. Sort the english grades first by passing_english and then by student name. All the students that are failing english should be first, and within the students that are failing english they should be ordered alphabetically. The same should be true for the students passing english. (Hint: you can pass a list to the .sort_values method)
# 
# - Both `by` and `ascending` accept list.

# In[10]:


df_reading_p_or_f.sort_values(by = ['passing_reading','name'])


# In[11]:


df_reading_p_or_f.sort_values(by = ['passing_reading','name'], ascending = False)


# In[12]:


df_reading_p_or_f.sort_values(by = ['passing_reading','name'], ascending = [False,True])


# ### 4. Sort the english grades first by passing_english, and then by the actual english grade, similar to how we did in the last step.

# In[13]:


df_reading_p_or_f.sort_values(by = ['passing_reading', 'reading'], ascending = [False, False])


# ### 5. Calculate each students overall grade and add it as a column on the dataframe. The overall grade is the average of the math, english, and reading grades.

# In[14]:


# Calculate overall grade for each student

overall_grade = (df.math + df.english + df.reading)/3
overall_grade = round(overall_grade)
overall_grade

# Add overall grade as a new column named 'overall_grade' without modifying the original table

df.assign(overall_grade = overall_grade)


# ### 2. Load the mpg dataset. Read the documentation for the dataset and use it for the following questions

# ### 2-1. How many rows and columns are there?
# 
# `df.shape[0]` and `df.shape[1]`

# In[15]:


# Number of rows in mpg
mpg.shape[0]


# In[16]:


# Number of columns in mpg
mpg.shape[1]


# In[17]:


# Verified by mpg.info()
mpg.info()


# ### 2-2. What are the data types of each column?
# 
# `df.dtypes` and `df.info()`

# In[18]:


mpg.dtypes


# ### 2-3. Summarize the dataframe with .info and .describe

# In[19]:


mpg.info()


# In[20]:


mpg.describe()


# ### 2-4. Rename the cty column to city.
# 
# `df.rename()`

# In[21]:


mpg.rename(columns = {'cty': 'city'}, inplace = True)
mpg.head()


# ### 2-5. Rename the hwy column to highway.

# In[22]:


mpg.rename(columns = {'hwy':'highway'}, inplace = True)
mpg.head()


# ### 2-6. Do any cars have better city mileage than highway mileage?

# In[23]:


# Create a mask that return True if city mileage is better than highway mileage

mask = mpg.city > mpg.highway

# subset the mpg talbe by mask

mpg[mask]


# ### 2-7. Create a column named mileage_difference this column should contain the difference between highway and city mileage for each car.

# In[24]:


# Create a series that return the different between highway and city mileage

mileage_diff = mpg.highway - mpg.city

# Modifiy the original mpg by adding the mileage different as the new column

mpg['mileage_difference'] = mileage_diff

# Output the new table

mpg.head()


# ### 2-8. Which car (or cars) has the highest mileage difference?
# 
# - Chaining the methods: `sort_values()` and `nlargest()`

# In[25]:


mpg.sort_values(by = 'mileage_difference').nlargest(1,'mileage_difference', keep='all')


# ### 2-9. Which compact class car has the lowest highway mileage? The best?

# In[26]:


# mpg.class runs into an error so name has been changed before continue
mpg.rename(columns = {'class':'car_size'}, inplace = True)

# Dobuble check it is working
mpg.car_size.head()


# In[27]:


# Create a mask that return true if the car size is compact
mask = (mpg.car_size == 'compact')

# Subset mpg into a table only has rows of cars with compact size and then chain the methods to output the result
mpg[mask].sort_values(by='highway').head(1)


# In[28]:


mpg[mask].sort_values(by='highway').tail(1)


# ### 2-10. Create a column named average_mileage that is the mean of the city and highway mileage.

# In[29]:


# Create a average_mileage varibale to hold the mean of the city and highway mileage.

average_mileage = (mpg.city + mpg.highway)/2

# Modify the mpg by adding a new column named average_mileage

mpg['average_mileage'] = average_mileage

mpg.head()


# ### 2-11. Which dodge car has the best average mileage? The worst?

# In[30]:


# Create a mask which return True is the manufacturer is dodge

mask = mpg.manufacturer == 'dodge'

# Subset the mpg to a new table only has dodge

mpg[mask].sort_values(by = 'average_mileage').tail(1)


# In[31]:


mpg[mask].sort_values(by = 'average_mileage').head(1)


# ### 3. Load the Mammals dataset. Read the documentation for it, and use the data to answer these questions:

# In[32]:


mammals = data('Mammals')
mammals.head()


# In[33]:


mammals_doc = data('Mammals', show_doc = True)
mammals_doc


# ### 3-1. How many rows and columns are there?

# In[34]:


mammals.shape[0]


# In[35]:


mammals.shape[1]


# ### 3-2. What are the data types?

# In[36]:


mammals.dtypes


# ### 3-3. Summarize the dataframe with .info and .describe

# In[37]:


mammals.info()


# In[38]:


mammals.describe()


# ### 3-4. What is the the weight of the fastest animal?

# In[39]:


mammals.sort_values(by = 'speed').tail(1).weight


# ### 3-5. What is the overal percentage of specials?

# In[40]:


specials_ratio = mammals.specials.sum()/mammals.specials.count()
specials_ratio


# In[41]:


percentage = "{:%}".format(specials_ratio)
percentage


# ### 3-6. How many animals are hoppers that are above the median speed? What percentage is this?

# In[42]:


# Find out the median speed of all mammals
median_speed = mammals.speed.median()
median_speed


# In[43]:


# Create a variable hoppers that hold a table of only hoppers
hoppers = mammals[mammals.hoppers]
hoppers


# In[44]:


# Create a variable fast_hoppers which hold a table of hoppers that are above the median speed
fast_hoppers = hoppers[hoppers.speed > median_speed]
fast_hoppers


# In[45]:


# Count how many fast hoppers out there
fast_hoppers_count = fast_hoppers.hoppers.size
fast_hoppers_count


# In[46]:


# Calculate the percent
fast_hoppers_ratio = fast_hoppers_count/mammals.hoppers.size
fast_hoppers_ratio


# In[47]:


percentage = "{:%}".format(fast_hoppers_ratio)
percentage


# In[ ]:




