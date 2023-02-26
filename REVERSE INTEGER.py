#!/usr/bin/env python
# coding: utf-8

# In[5]:


# 7. Reverse Integer
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321



x=1534236469
if x>0:
    str_x=str(x)
    reverse_str_x=str_x[::-1]
    reverse_int_x=int(reverse_str_x)
    print(reverse_int_x)
elif x<0:
    str_x=str(x)
    non_negative_str_x=str_x[1:]
    reverse_non_negative_str_x=non_negative_str_x[::-1]
    reverse_int_x=int(reverse_non_negative_str_x)
    reverse_negative_x=reverse_int_x*(-1)
    print(reverse_negative_x)
else:
    print(x)


# In[ ]:





# In[ ]:




