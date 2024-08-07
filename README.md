# Surfs Up
![hawaii_intro_pic.jpeg](https://github.com/Taireagan/Surfs_Up/blob/main/Images/hawaii_intro_pic.jpeg)

## Background
After many months of hard work, you've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii. To make the most of your trip, you have decided to conduct a comprehensive climate analysis of the area. Understanding the local weather patterns will help you pack appropriately, plan your activities, and make the most of your time in this beautiful location.

Honolulu, the capital city of Hawaii, is known for its tropical climate, stunning beaches, and vibrant cultural scene. However, like any tropical destination, its weather can be unpredictable, with varying precipitation levels and temperature fluctuations throughout the year. By analyzing historical climate data, you aim to gain insights into typical weather patterns, potential rainfall, temperature ranges, and other meteorological factors that may affect your travel experience.

---
## Table of Contents

[Data Sources](#data-sources)

[Objective of Analysis](#objective-of-analysis)

[Analysis and Visualizations](#analysis-and-visualizations)

[Climate App](#climate-app)

[Summary](#summary)

---

## Data Sources
- Data: [hawaii_measurements.csv](https://github.com/Taireagan/Surfs_Up/tree/main/Resources#:~:text=4%20hours%20ago-,hawaii_measurements.csv,-Finalized%20assignments%20and)
- Data: [hawaii_stations.csv](https://github.com/Taireagan/Surfs_Up/tree/main/Resources#:~:text=4%20hours%20ago-,hawaii_stations.csv,-Finalized%20assignments%20and)

---

## Objective of Analysis
We will use Python and SQLAlchemy to do a basic climate analysis and data exploration of your climate database. Specifically, we'll use SQLAlchemy ORM queries, Pandas, and Matplotlib. The primary objective of this analysis is to provide a detailed understanding of Honolulu's climate, focusing on two key aspects:

### 1. Precipitation:
For the precipitation analysis, we start by identifying the most recent date in the dataset. Using this date as a reference point, we will retrieve the precipitation data for the preceding 12 months, focusing on the "date" and "prcp" values. The query results will be loaded into a Pandas DataFrame, with columns explicitly named for clarity. The DataFrame will be sorted by "date" to ensure chronological order. Finally, we will visualize the precipitation data using the DataFrame's plotting capabilities.

### 2. Station:
In the station analysis we will do a basic climate analysis and data exploration for each station ID. First, we calculate the total number of stations present in the dataset. Next, we identify the most-active stations by listing them alongside their observation counts in descending order. We then determine which station ID has the highest number of observations. Using this most-active station ID, we design a query to calculate the lowest, highest, and average temperatures recorded at that station. Additionally, we query the previous 12 months of temperature observation (TOBS) data for the most-active station. The results are visualized as a histogram with 12 bins, providing a clear view of temperature distributions over the past year.


---
## Analysis and Visualizations

### Precipitation Analysis
To conduct a comprehensive analysis of the precipitation data, the following steps are undertaken:
- **Identify the Most Recent Date:** Begin by determining the most recent date available in the dataset.
- **Retrieve Precipitation Data:** Using this date as a reference, extract the precipitation data for the previous 12 months.
- **Filter Relevant Data:** Focus on selecting only the "date" and "prcp" (precipitation) columns from the dataset.
- **Create a Pandas DataFrame:** Load the extracted data into a Pandas DataFrame, ensuring that column names are explicitly defined for clarity and accuracy.
- **Sort the Data:** Arrange the DataFrame entries in chronological order based on the "date" column to facilitate accurate analysis.
- **Visualize the Data:** Utilize the Pandas DataFrame plotting method to generate a visual representation of the precipitation data, as illustrated in the accompanying image.
![bargraph_precipation.png](https://github.com/Taireagan/Surfs_Up/blob/main/Images/bargraph_precipation.png)

- **Print Summary Statistics:** Use Pandas to print the summary statistics for the precipitation data.
- ![statistics_precipation.png](https://github.com/Taireagan/Surfs_Up/blob/main/Images/statistics_precipation.png)


## Station Analysis
The station analysis involves a series of queries to extract meaningful insights from the dataset. The following steps outline the approach taken:
- **Calculate The Total Number of Stations:** Design a query to compute the total number of stations present in the dataset, providing an overview of the data's scope.
  
  ![number_of_stations.png](https://github.com/Taireagan/Surfs_Up/blob/main/Images/number_of_stations.png)

- **Identify Most-Active Stations:** Design a query to identify the most-active stations, defined as those with the highest number of observations. This involves listing stations along with their observation counts in descending order.
  
![most_active_station.png](https://github.com/Taireagan/Surfs_Up/blob/main/Images/most_active_station.png)

- **Temperature Analysis for the Most-Active Station:** Design a query to calculate the lowest, highest, and average temperatures for the most-active station identified in the previous step.
  
![temp_on_active_station.png](https://github.com/Taireagan/Surfs_Up/blob/main/Images/temp_on_active_station.png)

-  **Retrieve Temperature Observation Data:** Design a query to extract temperature observation (TOBS) data for the most-active station over the previous 12 months. This involves:
        -  Filtering data to focus on the station with the greatest number of observations.
        -  Querying the last 12 months of TOBS data for that specific station.
  
![temp_observation.png](https://github.com/Taireagan/Surfs_Up/blob/main/Images/temp_observation.png)

-  **Data Visualization:** Plot the retrieved TOBS data as a histogram with 12 bins, effectively visualizing the distribution of temperature observations over the past year.
  
![histogram_station.png](https://github.com/Taireagan/Surfs_Up/blob/main/Images/histogram_station.png)

---

## Climate App
In this project, we will develop a Flask API to serve the results of the previously designed queries. This API will provide a structured way to access the data and insights from the dataset, facilitating data retrieval and analysis through well-defined endpoints. The following outlines the process for creating the API routes using Flask:

- **API Overview:** The Flask API will expose several endpoints, each corresponding to a specific query and analysis result. These endpoints will allow users to interact with the data seamlessly, retrieving information about station statistics, temperature observations, and precipitation data.

  ![home_page.png](https://github.com/Taireagan/Surfs_Up/blob/main/Images/home_page.png)

### Route Design:
Using Flask, we will design the following API routes:

- **Precipitation Route:** 

![precipitation_route.png](https://github.com/Taireagan/Surfs_Up/blob/main/Images/precipitation_route.png)

- **Stations Route**

![stations_route.png](https://github.com/Taireagan/Surfs_Up/blob/main/Images/stations_route.png)

- **Tobs Route**

![tobs_route.png](https://github.com/Taireagan/Surfs_Up/blob/main/Images/tobs_route.png)

- **Temperatures from Start Date Route**

![start_temps.png](https://github.com/Taireagan/Surfs_Up/blob/main/Images/start_temps.png)

- **Temperatures from 2016 - 2017 Route**

![start_end_temps.png](https://github.com/Taireagan/Surfs_Up/blob/main/Images/start_end_temps.png)

---
## Summary 
This analysis provides a comprehensive overview of the climate patterns in Hawaii, focusing on key factors such as temperature, precipitation, and station activity. By utilizing historical climate data, the study examines temperature trends, precipitation variability, and the distribution of weather observations across various stations on the islands. The findings reveal seasonal variations in rainfall and temperature, identify the most active weather stations, and highlight the overall climatic characteristics of the region. This analysis serves as a valuable resource for understanding Hawaii's unique climate and can aid in planning activities.