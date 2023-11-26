# Bike-Sharing Rental Trend Analysis

## **Introduction**
> Bike sharing systems are new generation of traditional bike rentals where whole process from membership, rental and return back has become automatic. Through these systems, user is able to easily rent a bike from a particular position and return back at another position. Currently, there are about over 500 bike-sharing programs around the world which is composed of over 500 thousands bicycles. Today, there exists great interest in these systems due to their important role in traffic, environmental and health issues.

> Bike-sharing rental process is highly correlated to the environmental and seasonal settings. For instance, weather conditions, precipitation, day of week, season, hour of the day, etc. can affect the rental behaviors. The core data set is related to the two-year historical log corresponding to years 2011 and 2012 from Capital Bikeshare system, Washington D.C., USA which is publicly available in [Capital Bikeshare](https://capitalbikeshare.com/system-data). We aggregated the data on two hourly and daily basis and then extracted and added the corresponding weather and seasonal information. Weather information are extracted from [Freemeteo](https://www.freemeteo.com).
 
 
## **Problem Statement**
*   How is the trend of bike users in recent years?
*   How is the trend of casual users and registered users during different months and hours?
*   What is the highest of bike users during different seasons and weathers?
*   Does temperature and humidity affect bike users behaviour?

 
## Goals and Objective
*   Identify the underlying causes of trends or systemic patterns over time.
*   Measuring the strength of the linear relationship between two variables.


## Dataset Information
This dataset has 17379 rows dan 17 columns

## Dashboard:

### Run Streamlit
Install all the required libraries and run the following command:
```bash
pip install streamlit
pip install -r requirements.txt
```
### Run Dashboard
```bash
streamlit run dashboard.py
```

or you can visit directly on this [link](https://capitalbikeshare-time-series-dashboard.streamlit.app/)

## Result
![image](https://raw.githubusercontent.com/novrizalrnd/bike_sharing/main/img/dashboard.png)
