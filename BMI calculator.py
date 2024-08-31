#!/usr/bin/env python
# coding: utf-8

# In[3]:


name=input("enter your name")

weight=int(input("enter your weight in pounds: "))

height=int(input("enter your height in inches: "))

BMI=(weight * 703)/(height * height)

print(BMI)

if BMI > 0:
    if(BMI < 18.5):
        print(name +", YOU ARE UNDERWEIGHT\n")
    elif(BMI < 24.9):
        print(name +", YOU HAVE NORMAL WEIGHT\n")
    elif(BMI < 29.9):
        print(name +", YOU ARE OVERWEIGHT\n")
    elif(BMI < 34.9):
        print(name +", YOU ARE OBESE\n")
    elif(BMI < 39.9):
        print(name +", YOU ARE SEVERELY OBESE\n")
    else:
        print(name +", YOU ARE MORBIDLY OBESE\n")
else:
    print("enter the valid input")
        


# In[ ]:




