#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[13]:


df=pd.read_csv(r'C:\Users\Hp\Desktop\programs\Datasets\dataset-1.csv')


# In[14]:


df


# In[19]:


def generate_car_matrix(dataframe):
    
    matrix = dataframe.pivot(index='id_1', columns='id_2', values='car').fillna(0)
    
   
    matrix.values[[range(len(matrix))]*2] = 0
    
    return matrix

result_matrix = generate_car_matrix(df)

print(result_matrix)


# In[20]:


def get_type_count(dataframe):
   
    dataframe['car_type'] = pd.cut(dataframe['car'],
                                   bins=[-float('inf'), 15, 25, float('inf')],
                                   labels=['low', 'medium', 'high'],
                                   include_lowest=True)
    
    
    type_counts = dataframe['car_type'].value_counts().to_dict()
    
    
    sorted_type_counts = dict(sorted(type_counts.items()))
    
    return sorted_type_counts
result_counts = get_type_count(df)

print(result_counts)


# In[21]:


def get_bus_indexes(dataframe):
    
    bus_mean = dataframe['bus'].mean()
    
    bus_indexes = dataframe[dataframe['bus'] > 2 * bus_mean].index.tolist()
    
    bus_indexes.sort()
    
    return bus_indexes

result_indexes = get_bus_indexes(df)

print(result_indexes)


# In[22]:


def filter_routes(dataframe):
    route_means = dataframe.groupby('route')['truck'].mean()
    
    selected_routes = route_means[route_means > 7].index.tolist()
    
    selected_routes.sort()
    
    return selected_routes

result_routes = filter_routes(df)
print(result_routes)


# In[23]:


def multiply_matrix(input_matrix):
    modified_matrix = input_matrix.copy()
    modified_matrix = modified_matrix.applymap(lambda x: x * 0.75 if x > 20 else x * 1.25)
    modified_matrix = modified_matrix.round(1)

    return modified_matrix
modified_result_matrix = multiply_matrix(result_matrix)
print(modified_result_matrix)


# In[ ]:





# # Time Check

# In[27]:


import pandas as pd
from datetime import datetime,timedelta


# In[25]:


df=pd.read_csv(r'C:\Users\Hp\Desktop\programs\Datasets\dataset-2.csv')


# In[26]:


df


# In[ ]:


def check_time_completeness:
    
    df['timestamp'] = pd.to_datetime(df['startDay'] + ' ' + df['startTime'])
    df['end_timestamp'] = pd.to_datetime(df['endDay'] + ' ' + df['endTime'])
    completeness_results = {}

    for key, group in df.groupby(['id', 'id_2']):
        
        group = group.sort_values(by='timestamp')
        start_time = group['timestamp'].iloc[0]
        end_time = group['end_timestamp'].iloc[-1]

        if (end_time - start_time == timedelta(days=7)) and (start_time.time() == datetime.min.time()) and (end_time.time() == datetime.max.time()):
            completeness_results[key] = "Complete"
        else:
            completeness_results[key] = "Incomplete"

    return completeness_results
result = check_time_completeness('dataset-2.csv')

print(result)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




