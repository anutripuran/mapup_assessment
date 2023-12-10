#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
from datetime import time


# In[4]:


def calculate_distance_matrix(dataset_path):
    df = pd.read_csv(r'C:\Users\Hp\Desktop\programs\Datasets\dataset-3.csv')
    distance_matrix = pd.pivot_table(df, values='distance', index='id_start', columns='id_end', aggfunc='sum', fill_value=0)
    distance_matrix = distance_matrix + distance_matrix.T
    distance_matrix.values[[range(len(distance_matrix))]*2] = 0

    return distance_matrix
result_matrix = calculate_distance_matrix('dataset-3.csv')
print(result_matrix) 


# In[5]:


def unroll_distance_matrix(distance_matrix):
    indices = distance_matrix.index
    unrolled_data = []
    for id_start in indices:
        for id_end in indices:
            
            if id_start != id_end:
               
                distance_value = distance_matrix.loc[id_start, id_end]
                unrolled_data.append({'id_start': id_start, 'id_end': id_end, 'distance': distance_value})
    unrolled_df = pd.DataFrame(unrolled_data)

    return unrolled_df
unrolled_distance_df = unroll_distance_matrix(result_matrix)
print(unrolled_distance_df)


# In[7]:


def find_ids_within_ten_percentage_threshold(df, reference_value):
    reference_df = df[df['id_start'] == reference_value]
    average_distance = reference_df['distance'].mean()
    lower_threshold = average_distance - 0.1 * average_distance
    upper_threshold = average_distance + 0.1 * average_distance
    filtered_df = df[(df['distance'] >= lower_threshold) & (df['distance'] <= upper_threshold)]
    result_ids = sorted(filtered_df['id_start'].unique())

    return result_ids
reference_value = 123
result_ids = find_ids_within_ten_percentage_threshold(unrolled_distance_df, reference_value)
print(result_ids)


# In[17]:


def calculate_toll_rate(df):
    rate_coefficients = {'moto': 0.8, 'car': 1.2, 'rv': 1.5, 'bus': 2.2, 'truck': 3.6}
    for vehicle_type, rate in rate_coefficients.items():
        df[vehicle_type] = df['distance'] * rate

    return df

result_with_toll_rate = calculate_toll_rate(unrolled_distance_df)
print(result_with_toll_rate)


# In[16]:


def calculate_time_based_toll_rates(df):
    df['id_start'] = pd.to_datetime(df['id_start'])
    df['id_end'] = pd.to_datetime(df['id_end'])

    time_ranges = [
        (time(0, 0, 0), time(10, 0, 0), 0.8),
        (time(10, 0, 0), time(18, 0, 0), 1.2),
        (time(18, 0, 0), time(23, 59, 59), 0.8)
    ]

    for start_time, end_time, discount_factor in time_ranges:
        mask = (df['id_start'].dt.time >= start_time) & (df['id_end'].dt.time <= end_time)
        df.loc[mask, ['moto', 'car', 'rv', 'bus', 'truck']] *= discount_factor
    weekend_mask = df['id_start'].isin(['Saturday', 'Sunday'])
    df.loc[weekend_mask, ['moto', 'car', 'rv', 'bus', 'truck']] *= 0.7

    return df
result_with_time_based_toll_rates = calculate_time_based_toll_rates(result_with_toll_rate)
print(result_with_time_based_toll_rates)


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





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




