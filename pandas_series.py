#!/usr/bin/env python
# coding: utf-8

# 1. Use pandas to create a Series from the following data:
# 
# ["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


# a. Name the variable that holds the series fruits.

fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])
print(fruits)
print(type(fruits))


# In[3]:


# b. Run .describe() on the series to see what describe returns for a series of strings.

fruits.describe()


# In[4]:


# c. Run the code necessary to produce only the unique fruit names.

unique_fruit = fruits.unique()
print(unique_fruit)
print(type(unique_fruit))
print(unique_fruit.size)


# In[5]:


# d. Determine how many times each value occurs in the series.

fruit_count = fruits.value_counts()
    
# A new series is returned and the element is the count (int) and the labels are the fruit names.

print(fruit_count)
print(type(fruit_count)) 


# In[6]:


# e. Determine the most frequently occurring fruit name from the series.

max_count = fruit_count.max()
fruit_count[fruit_count == max_count]


# In[7]:


# f. Determine the least frequently occurring fruit name from the series.

min_count = fruit_count.min()
fruit_count[fruit_count == min_count]


# In[8]:


# g. Write the code to get the longest string from the fruits series.

longest_length = fruits.str.len().max()
fruits[fruits.str.len() == longest_length]


# In[10]:


# h. Find the fruit(s) with 5 or more letters in the name.

# remove the space

fruits.str.replace(" ",'')

# Find out the length with 5 or more

fruits.str.replace(" ",'').str.len() >= 5

# subset

fruits[fruits.str.replace(" ",'').str.len() >= 5]


# In[11]:


# i. Capitalize all the fruit strings in the series.

cap_fruit = fruits.str.capitalize()
cap_fruit


# In[12]:


# j. Count the letter "a" in all the fruits (use string vectorization)

count_a = fruits.str.count("a")
count_a.sum()


# In[16]:


# l.Use the .apply method and a lambda function 
# to find the fruit(s) containing two or more "o" letters in the name.

fruits.apply(lambda fruit: fruit if fruit.count('o') >= 2 else "")


# In[14]:


def two_or_more_o(fruit):
    if fruit.count("o") >= 2:
        return fruit

fruits.apply(two_or_more_o)


# In[17]:


# m. Write the code to get only the fruits containing "berry" in the name

fruits.apply(lambda fruit: fruit if "berry" in fruit else "")


# In[18]:


# n. Write the code to get only the fruits containing "apple" in the name

fruits.apply(lambda fruit: fruit if "apple" in fruit else "")


# In[19]:


# o. Which fruit has the highest amount of vowels?

# define a fuction that count vowels

def count_vowel(word):
    word = word.lower()
    count = 0
    for letter in word:
        if letter in "aeiou":
            count += 1
    return count

# find out the highest amount of vowels

max_vowels = fruits.apply(count_vowel).max()
print(max_vowels)

# subset

fruits[max_vowels]


# 2. Use pandas to create a Series from the following data:
# 
# ['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']

# In[20]:


data = pd.Series(['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23'])
data


# In[21]:


# What is the data type of the series?

print(type(data))
type(data[0])


# In[22]:


# Use series operations to convert the series to a numeric data type.

# remove the $ sign

data_num = data.str.replace("$","")

# remove the ","

data_num = data_num.str.replace(",","")

# convert to float

data_num = data_num.apply(lambda i: float(i))
data_num


# In[23]:


# What is the maximum value? The minimum?

max = data_num.max()
print(max)

min = data_num.min()
print(min)


# In[24]:


# Bin the data into 4 equally sized intervals and show how many values fall into each bin.

data_bin_4 = pd.cut(data_num, 4)

print(data_bin_4)

data_bin_4.value_counts()


# In[30]:


data_num.plot.hist()
plt.title("Deposite Distribution")
plt.xlabel("Deposite")
plt.ylabel("Frequnce")
plt.xticks(rotation = 45)


# In[25]:


# Plot a histogram of the data. Be sure to include a title and axis labels.

plt.figure(figsize = (8, 5))

data_bin_4.value_counts().plot.bar()
plt.title("Deposite Distribution")
plt.xlabel("Deposite range")
plt.ylabel("Frequnce")
plt.xticks(rotation = 10)


# 3. Use pandas to create a Series from the following exam scores:
# 
# [60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78]

# In[26]:


scores = pd.Series([60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78])
scores


# In[27]:


# What is the minimum exam score? The max, mean, median?

scores.describe()


# In[28]:


# Plot a histogram of the scores.

scores.plot.hist()


# In[31]:


# Convert each of the numbers above into a letter grade. For example, 86 should be a 'B' and 95 should be an 'A'.

scores.apply(lambda score: "A" if score >= 88 else ("B" if score >= 80 else ("C" if score >= 67 else ("D" if score >= 60 else "F"))))


# In[32]:


# Write the code necessary to implement a curve. I.e. that grade closest to 100 should be converted to a 100, 
# and that many points should be given to every other score as well.

curve_points = (100 - scores).min()
curved_scores = scores + curve_points
curved_scores

scores.plot.hist(alpha = 0.5)
curved_scores.plot.hist(alpha = 0.5)


# Use pandas to create a Series from the following string:
# 
# 'hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'

# In[33]:


original_text = pd.Series('hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy')
original_text


# In[34]:


text = pd.Series([char for char in original_text[0]])
text.describe()


# In[35]:


# What is the most frequently occuring letter? Least frequently occuring?

# the describe already return the most frequently occuring letter.

char_count = text.value_counts()
min_count = char_count.min()

char_count[char_count == min_count]


# In[36]:


# How many vowels are in the list?

text.apply(count_vowel).sum()


# In[37]:


# How many consonants are in the list?

text.size - text.apply(count_vowel).sum()


# In[38]:


# Create a series that has all of the same letters, but uppercased

original_text.str.upper()


# In[39]:


# Create a bar plot of the frequencies of the 6 most frequently occuring letters.

six_most = text.value_counts().head(n=6)
six_most.plot.bar()
plt.xticks(rotation = 0)
plt.title("Top 6 most frequently occuring letters")
plt.xlabel("letters")
plt.ylabel("frequency")


# 5. Complete the exercises from https://gist.github.com/ryanorsinger/f7d7c1dd6a328730c04f3dc5c5c69f3a, but use pandas Series for the data structure instead of lists and use Series subsetting/indexing and vectorization options instead of loops and lists.

# In[40]:


fruits = pd.Series(['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange'])

numbers = pd.Series([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9])


# In[41]:


# Exercise 1 - rewrite the above example code using list comprehension syntax. 
# Make a variable named uppercased_fruits to hold the output of the list comprehension. 
# Output should be ['MANGO', 'KIWI', etc...]

uppercased_fruits = fruits.str.upper()
list(uppercased_fruits)


# In[42]:


# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax 
# to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]

capitalized_fruits = fruits.str.capitalize()
list(capitalized_fruits)


# In[43]:


# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. 
# Hint: You'll need a way to check if something is a vowel.

fruits_with_more_than_two_vowels = fruits[fruits.apply(count_vowel) > 2]
list(fruits_with_more_than_two_vowels)


# In[44]:


# Exercise 4 - make a variable named fruits_with_only_two_vowels. 
# The result should be ['mango', 'kiwi', 'strawberry']

fruits_with_only_two_vowels = fruits[fruits.apply(count_vowel) == 2]
list(fruits_with_only_two_vowels)


# In[45]:


# Exercise 5 - make a list that contains each fruit with more than 5 characters

list(fruits[fruits.str.len() > 5])


# In[46]:


# Exercise 6 - make a list that contains each fruit with exactly 5 characters

list(fruits[fruits.str.len() == 5])


# In[47]:


# Exercise 7 - Make a list that contains fruits that have less than 5 characters

list(fruits[fruits.str.len() < 5])


# In[48]:


# Exercise 8 - Make a list containing the number of characters in each fruit. 
# Output would be [5, 4, 10, etc... ]

fruits.str.len()
list(fruits.str.len())


# In[49]:


# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits 
# that contain the letter "a"


fruits_with_letter_a = fruits.apply(lambda fruit: fruit if "a" in fruit else "")
fruits_with_letter_a
list(fruits_with_letter_a)


# In[50]:


# 10 - Make a variable named even_numbers that holds only the even numbers 

even_numbers = numbers[numbers % 2 == 0]
even_numbers
list(even_numbers)


# In[51]:


# 11 - Make a variable named odd_numbers that holds only the odd numbers

odd_numbers = numbers[numbers % 2 == 1]
odd_numbers
list(odd_numbers)


# In[52]:


#  12 - Make a variable named positive_numbers that holds only the positive numbers

positive_numbers = numbers[numbers > 0]
positive_numbers
list(positive_numbers)


# In[53]:


# 13 - Make a variable named negative_numbers that holds only the negative numbers

negative_numbers = numbers[numbers < 0]
negative_numbers
list(negative_numbers)


# In[54]:


# 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals

numbers[(numbers >= 10) | (numbers <= -10)]
list(numbers[(numbers >= 10) | (numbers <= -10)])


# In[55]:


# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared.
# Output is [4, 9, 16, etc...]

numbers_squared = numbers**2
numbers_squared
print(list(numbers_squared))


# In[56]:


# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers 
# that are both odd and negative.

odd_negative_numbers = numbers[(numbers < 0) & (numbers % 2 == 1)]
odd_negative_numbers
list(odd_negative_numbers)


# In[57]:


# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five. 

numbers_plus_5 = numbers + 5
numbers_plus_5
list(numbers_plus_5)


# In[58]:


# BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list. 
# *Hint* you may want to make or find a helper function that determines if a given number is prime or not.

def check_prime(x):
    if x > 1:
        for i in range (2, x):
            if (x % i) == 0:
                return False
                break
        else:
            return True
    else:
        return True
    
mask = numbers.apply(check_prime)
numbers[mask]
list(numbers[mask])


# In[ ]:




