#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Use the following code for the questions below:

import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
a


# 1. How many negative numbers are there?

# In[2]:


a[a < 0].shape


# In[3]:


(a < 0).sum()


# In[5]:


a[a < 0].size


# 2. How many positive numbers are there?

# In[6]:


a[a > 0].size


# 3. How many even positive numbers are there?

# In[7]:


a[(a%2==0)&(a>0)].size


# 4. If you were to add 3 to each data point, how many positive numbers would there be?

# In[17]:


a1 = a + 3
a1[a > 3].size


# 5. If you squared each number, what would the new mean and standard deviation be?

# In[9]:


a2 = a**2
print(a2)

new_mean_of_a2 = a2.mean()
print(new_mean_of_a2)

std_of_a2 = a2.std()
print(std_of_a2)


# 6. A common statistical operation on a dataset is centering. This means to adjust the data such that the center of the data is at 0. This is done by subtracting the mean from each data point. Center the data set.

# In[10]:


mean_of_a = a.mean()
print(f"The mean of array a is {mean_of_a}\n")
centered_a = a - mean_of_a
print(f"Array a after being centered: {centered_a}")


# 7. Calculate the z-score for each data point.

# In[11]:


# Calculate the mean of array a: 

mean_of_a = a.mean()
print(f"The mean of array a is: {mean_of_a}\n")

# Calculate the standard deviation of array a:

std_of_a = a.std()
print(f"The standard deviation of array a is: {std_of_a}\n")

# Calculate z-score:

z_score_of_a = (a - mean_of_a)/std_of_a
z_score_of_a = np.round(z_score_of_a, decimals = 2)
print(f"The z score of each data point in array a is:\n{z_score_of_a}")


# In[12]:


# Life w/o numpy to life with numpy

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following


# In[13]:


# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list

sum_of_a = sum(a)
sum_of_a


# In[14]:


# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list

min_of_a = min(a)
min_of_a


# In[15]:


# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list

max_of_a = max(a)
max_of_a


# In[16]:


# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list

mean_of_a = sum(a)/len(a)
mean_of_a


# In[17]:


# Exercise 5 - Make a variable named product_of_a 
# to hold the product of multiplying all the numbers in the above list together

product_of_a = 1

for i in a:
    product_of_a = product_of_a*i

product_of_a


# In[18]:


# Exercise 6 - Make a variable named squares_of_a. 
# It should hold each number in a squared like [1, 4, 9, 16, 25...]

square_of_a = [n**2 for n in a]
square_of_a


# In[19]:


# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers

odds_in_a = [n for n in a if n%2 == 1]
odds_in_a


# In[20]:


# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.

evens_in_a = [n for n in a if n%2 == 0]
evens_in_a


# In[21]:


# What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
# Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, 
# and list of squares for this list of two lists.


# In[22]:


# Exercise 1 - refactor the following to use numpy. 
# Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**

b = [
    [3, 4, 5],
    [6, 7, 8]
]

sum_of_b = 0
for row in b:
    sum_of_b += sum(row)

sum_of_b


# In[23]:


b = np.array(b)
print(type(b))

sum_of_b = b.sum()
sum_of_b


# In[24]:


# Exercise 2 - refactor the following to use numpy. 

b = [
    [3, 4, 5],
    [6, 7, 8]
]

print(type(b))

min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  
min_of_b


# In[25]:


b = np.array(b)
print(type(b))

min_of_b = b.min()
min_of_b


# In[26]:


# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.

b = [
    [3, 4, 5],
    [6, 7, 8]
]

print(type(b))

max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])
max_of_b


# In[27]:


b = np.array(b)
print(type(b))

max_of_b = b.max()
max_of_b


# In[28]:


# Exercise 4 - refactor the following using numpy to find the mean of b

b = [
    [3, 4, 5],
    [6, 7, 8]
]

print(type(b))

mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))
mean_of_b


# In[29]:


b = np.array(b)
print(type(b))

mean_of_b = b.mean()
mean_of_b


# In[30]:


# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.

b = [
    [3, 4, 5],
    [6, 7, 8]
]

print(type(b))

product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number
        
product_of_b


# In[31]:


b = np.array(b)
print(type(b))

product_of_b = b.prod()
product_of_b


# In[32]:


# Exercise 6 - refactor the following to use numpy to find the list of squares 

b = [
    [3, 4, 5],
    [6, 7, 8]
]

print(type(b))

squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)
        
squares_of_b


# In[33]:


b = np.array(b)
print(type(b))

squares_of_b = b**2
print(squares_of_b)

# convert array back to list
squares_of_b = squares_of_b.tolist()
squares_of_b


# In[34]:


# Exercise 7 - refactor using numpy to determine the odds_in_b

b = [
    [3, 4, 5],
    [6, 7, 8]
]

print(type(b))

odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)
            
odds_in_b


# In[35]:


b = np.array(b)
print(type(b))

odds_in_b = b[b%2 == 1]
odds_in_b


# In[36]:


# Exercise 8 - refactor the following to use numpy to filter only the even numbers

b = [
    [3, 4, 5],
    [6, 7, 8]
]

print(type(b))

evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)
            
evens_in_b


# In[37]:


b = np.array(b)
print(type(b))

evens_in_b = b[b%2 == 0]
evens_in_b


# In[38]:


# Exercise 9 - print out the shape of the array b.

b = np.array(b)
print(b)

b.shape


# In[39]:


# Exercise 10 - transpose the array b.

b.transpose()


# In[40]:


# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)

b.flatten()


# In[41]:


# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)

b.reshape(6,1)


# In[42]:


## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# HINT, you'll first need to make sure that 
# the "c" variable is a numpy array prior to using numpy array methods.


# In[43]:


# Convert c from a list to array

c = np.array(c)
c


# In[44]:


# Exercise 1 - Find the min, max, sum, and product of c.

c.min()


# In[45]:


c.max()


# In[46]:


c.sum()


# In[47]:


c.prod()


# In[48]:


# Exercise 2 - Determine the standard deviation of c.

c.std()


# In[49]:


flat_c = c.flatten()
flat_c.std()


# In[ ]:


# Exercise 3 - Determine the variance of c.


# In[50]:


c.var()


# In[51]:


flat_c = c.flatten()
flat_c.var()


# In[52]:


# Exercise 4 - Print out the shape of the array c

c.shape


# In[53]:


# Exercise 5 - Transpose c and print out transposed result.

c.transpose()


# In[56]:


# Exercise 6 - Get the dot product of the array c with c. 

multiplication = c * c
multiplication.sum()


# In[57]:


# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261

trans_c = c.transpose()
multiplication = c * trans_c
multiplication.sum()


# In[58]:


# Exercise 8 - Write the code necessary to determine the product of c times c transposed. 
# Answer should be 131681894400.

product = c * trans_c
product.prod()


# In[3]:


## Setup 4

d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

d = np.array(d)
d


# In[5]:


# Exercise 1 - Find the sine of all the numbers in d

sin_of_d = np.sin(d)
np.round(sin_of_d, decimals = 2)


# In[7]:


# Exercise 2 - Find the cosine of all the numbers in d

cos_of_d = np.cos(d)
np.round(cos_of_d, decimals = 2)


# In[8]:


# Exercise 3 - Find the tangent of all the numbers in d

tan_of_d = np.tan(d)
np.round(tan_of_d, decimals = 2)


# In[9]:


# Exercise 4 - Find all the negative numbers in d

d[d < 0]


# In[10]:


# Exercise 5 - Find all the positive numbers in d

d[d > 0]


# In[11]:


# Exercise 6 - Return an array of only the unique numbers in d.

np.unique(d)


# In[12]:


# Exercise 7 - Determine how many unique numbers there are in d.

np.unique(d).size


# In[13]:


# Exercise 8 - Print out the shape of d.

d.shape


# In[15]:


# Exercise 9 - Transpose and then print out the shape of d.

trans_d = d.transpose()
trans_d.shape


# In[16]:


# Exercise 10 - Reshape d into an array of 9 x 2

d.reshape(9,2)


# In[ ]:




