import os
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import datetime as dt
slash = '/'
path = os.getcwd()
class Montana():
    def input_dropdown_micro(macro_period):
        micro_periods = {'alltime':['tax year','year','quarter','month','week','day','weekday'],
                         'tax year':['quarter','month','week','day','weekday'],
                         'year':['quarter','month','week','day','weekday'],
                         'quarter':['month','week','day','weekday','date'],
                         'month':['week','day','weekday','date'],
                         'week':['day','weekday','date'],
                        }
        options=[]
        for i in micro_periods[macro_period]:
            options.append({'label':i,'value':i})
        return options

    def input_dropdown_column_set(df,column):
        a = pd.Series(df[column].unique().astype(str)).to_list()
        options = []
        for i in a:
            options.append({'label':i,'value':i})
        return options
    
    def filter_time_period(df,main_dropdown_value,sub_dropdown_1):
        data = df.copy()
        if main_dropdown_value != 'alltime':
            data = data[data[main_dropdown_value] == sub_dropdown_1]
        else:
            data = data
        return data