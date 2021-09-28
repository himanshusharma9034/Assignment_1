#!/usr/bin/env python
# coding: utf-8

# # Q1.Create the below pattern using nested for loop in Python.

# In[21]:


input_num = int(input("Enter the integer : "))
a = range(0,input_num)
for i in a:
    print(i*'*')
for j in a[::-1]:
    print(j*'*')


# # Q2. Write a Python program to reverse a word after accepting the input from the user.
# 
# # Input word: ineuron
# # Output: norueni

# In[3]:


input_string = input()
print(input_string[::-1])


# In[ ]:




