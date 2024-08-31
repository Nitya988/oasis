#!/usr/bin/env python
# coding: utf-8

# In[22]:


import requests

api_key='16822dd48e76835c7c99e5eca8218f24'

user_input=input("enter city:")

weather_data=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

#print(weather_data.status_code)

#print(weather_data.json())

weather = weather_data.json()['weather'][0]['main']
temp = weather_data.json()['main']['temp']

if weather_data.json()['cod']== '404':
    print("no city find")
else:    
    
    print(f"The weather in {user_input} is:{weather}")

    print(f"The temperature in {user_input} is:{temp}deg F")




# In[ ]:





# In[ ]:




