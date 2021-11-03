#!/usr/bin/env python
# coding: utf-8

# # Q1.1 Write a Python Program(with class concepts) to find the area of the triangle using the below formula. area = (s*(s-a)*(s-b)*(s-c)) ** 0.5 Function to take the length of the sides of triangle from user should be defined in the parent class and function to calculate the area should be defined in subclass.
# 
# 
# 
# 
# 
# 

# In[44]:


class a_tri:
    def __init__(self,a,b,c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
a= int(input("::::>>>>Enter Value for a="))
b= int(input("::::>>>>Enter Value for b="))
c= int(input("::::>>>>Enter Value for c="))

class triangle(a_tri):
    def __init__(self,a,b,c):
        super().__init__(a,b,c)

    def get_area(self):
        s = (a + b + c) / 2
        return (s*(s-a)*(s-b)*(s-c)) ** 0.5        

t = triangle(a,b,c)
print(":::::::>>>>>>>> AREA OF THE TRIANGLE :", t.get_area())


# # Q1.2 Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n.

# In[28]:





# # Q2.1 Write a Python program using function concept that maps list of words into a list of integers representing the lengths of the corresponding words.
# # Hint: If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4]Here 2,3 and 4 are the lengths of the words in the list.

# In[14]:


def map_list(list1 = ["ab","cde","erty"]):
    try:
        new_list = []
        for i in list1:
            len_gth = len(i)
            new_list.append(len_gth)
    except Exception as e:
        print(e)
    finally:
        print(":::::::::>>>>>>>>>>  OUTPUT  <<<<<<<<<<<<:::::::::::")
        print(new_list)


# In[15]:


map_list()


# # Q2.2 Write a Python function which takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.

# In[4]:


def check_vowel(*args):
    while True:
        try:
            string = input(">>>>>>>>>ENTER THE STRING <<<<<<<<")
            try:
                if len(string) > 1:
                    continue
            except:
                print("<><><><>")
        except:
            print("<><><><>")
        else:
            try:
                if (string == 'a' or string == 'A' or string == 'E' or string == 'e' or string == 'I' or string == 'i' or string == 'O' or string == 'o' or string == 'U'or string == 'u'):
                    print(":::TRUE:::VOWEL:::")
                    break
                else:
                    print(":::FALSE:::NOT VOWEL:::")
            except:
                print("Not Vowel")
            finally:
                print(">> OUTPUT <<")


# In[6]:


check_vowel()

