#!/usr/bin/env python
# coding: utf-8

# In[4]:


E = {0,1,2,3,4}
N = {2,4,5,6,8}
result = E.intersection(N)
print(result)


# In[6]:


E = {0,1,2,3}
N = {4,5,6,8}
result = E.union(N)
print(result)


# In[11]:


E = {0,1,2,3,4,6,8}
N = {1,2,3,4,}
result = E.difference(N)
print(result)


# E = {0,1,2,3,4}
# N = {4,5,6,8}
# result = E.symmetric_difference.N
# print(result)

# In[1]:


E = {0,1,2,3,4,}
N = {5,4,6,8}
result= E.symmetric_difference(N)
print(result)


# In[ ]:




