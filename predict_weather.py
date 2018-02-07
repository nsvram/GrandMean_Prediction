
# coding: utf-8

# In[1]:


import pandas as pd
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings("ignore")


# In[7]:


def cal_conditions(row):
    #Function to caluculate and predict the day as Rain, Snow, Sunny, etc
    if row['rainfall_mm'] >= 1.5:
        return 'Rain'
    elif row['minimum_temperature'] <= 0 and row['maximum_temperature'] <= 10:
        return 'Snow' 
    elif row['maximum_temperature'] >= 30 and row['minimum_temperature'] <= 25:
        return 'Sunny' 
    else:
        return 'Moderate'

def date_rolling_range(no_of_days,date_to_predict):
    return [(datetime.strptime(date_to_predict, '%Y-%m-%d') - timedelta(days=365) - timedelta(days=no_of_days)).strftime('%Y-%m-%d'), 
            (datetime.strptime(date_to_predict, '%Y-%m-%d') - timedelta(days=365) + timedelta(days=no_of_days)).strftime('%Y-%m-%d')]

def mean_per_date_station(df,date_range, in_station_id):
    filter_range = (df.station_id == in_station_id)&(df.date_formated >= date_range[0]) & (df.date_formated <= date_range[1])
    return df.loc[filter_range].groupby(['station_id']).mean()

def predict_weather(station_id, date_to_predict):
    # Used Grand Mean method to predict weather
    # https://en.wikipedia.org/wiki/Grand_mean
    history_weather = pd.read_csv("/home/jovyan/data/weather_extract.csv", index_col="date")
    df_station_list = history_weather[['station_id','station_name']].groupby(['station_id','station_name']).count()
    history_weather['date_formated']=history_weather.index
    history_weather.date_formated = history_weather.date_formated.apply(lambda x: datetime.strptime(x, '%Y-%m-%d'))
    union_df = pd.concat([mean_per_date_station(history_weather,date_rolling_range(3,date_to_predict),station_id)
                          ,mean_per_date_station(history_weather,date_rolling_range(15,date_to_predict),station_id)
                          ,mean_per_date_station(history_weather,date_rolling_range(30,date_to_predict),station_id)])
    final_prediction = union_df.groupby(union_df.index).mean()
    final_prediction_pred =  final_prediction[['Lat', 'Lon','rainfall_mm','3pm_relative_humidity','3pm_relative_humidity', 'minimum_temperature', 'maximum_temperature']]
    final_prediction_pred["Conditions"] = final_prediction_pred.apply(cal_conditions,axis=1)
    final_prediction_pred["predicted_date"] = date_to_predict
    final_prediction_pred.join(df_station_list)
    df_station_list.to_csv("staion_id.csv")
    with open('/home/jovyan/data/prediction_weather.psv', 'a') as f:
        final_prediction_pred.to_csv(f, header=False, sep='|')


# In[39]:


strat_date = '2018-01-01'
no_of_days = 2
station_id_list = [3003, 9021, 9999, 12038,18192,23090,24048,26021,31011]

date_list = [(datetime.strptime(strat_date, '%Y-%m-%d') + timedelta(days=x)).strftime('%Y-%m-%d')
             for x in range(0, no_of_days)]
for day in date_list:
    for station in station_id_list:
        predict_weather(station, day)
        print (("Predicting Weather for the date - {0} and weather station id - {1}").format(day, station))
    


