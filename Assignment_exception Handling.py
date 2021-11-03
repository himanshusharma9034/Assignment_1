#!/usr/bin/env python
# coding: utf-8

# # Q1.Write a function to compute 5/0 and use try/except to catch the exceptions.
# 

# In[4]:


try:
    5/0
except Exception as e:
    print(e)


# # Q2. Implement a Python program to generate all sentences where subject is in

# In[ ]:


# ["Americans", "Indians"] and verb is in ["Play", "watch"] and the object is in
# ["Baseball","cricket"].
# Hint: Subject,Verb and Object should be declared in the program as shown below.
# subjects=["Americans ","Indians"]
# verbs=["play","watch"]
# objects=["Baseball","Cricket"]
# Output should come as below:
# Americans play Baseball.
# Americans play Cricket.
# Americans watch Baseball.
# Americans watch Cricket.
# Indians play Baseball.
# Indians play Cricket.
# Indians watch Baseball.
# Indians watch Cricket.


# In[37]:


def lstcon_genreator (subject = ["Americans", "Indians"],verb = ["Play", "watch"],object_ =  ["Baseball","cricket"]):
    try:
        for i in subject:
            for j in verb:
                d1 = i + " " + j
                for k in object_:
                    e1 = d1 + " " + k
                    print (e1)
    except:
        print("::::::>>>>>> CODING :::::::>>>>>>")
    finally:
        print(":::::::>>>>> OUTPUT :::::::>>>>>>")


# In[38]:


lstcon_genreator()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




