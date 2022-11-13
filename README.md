# SqlAlchemy_Challenge
Surf’s Up

This challenge is to perform a climate analysis using the data collected from 2010 to 2017 in Honolulu, Hawaii. This is done in 2 steps:
1)  **Analyze and Explore Climate Data** - Do a basic climate analysis and data exploration of the climate database using SQLAlchemy ORM queries, Pandas and Matplotlib.
2)  **Design Climate App** - After completing the initial analysis, design a Flask API based on the queries that were just developed.  

##  1) Analyze and Explore Climate Data
This step involves analysing Precipitation and Weather Stations data. 

For this, the connection between Python and SQLite Database is established by performing the following steps:
1)  Use the SQLAlchemy **create_engine()** function to connect to the SQLite database.
2)  Use the SQLAlchemy **automap_base()** function to reflect the tables into classes, and then save references to the classes named Station and Measurement.
3)  Link Python to the database by creating a **SQLAlchemy session**.

The SQLite db used for this analysis can be found in **SqlAlchemy_Challenge\SurfsUp\Resources\hawaii.sqlite**
The Jupyter notebook used can be found in **SqlAlchemy_Challenge\SurfsUp\climate.ipynb**

### 1.1) Exploratory Precipitation Analysis
1)  Find the most recent date in the dataset.
2)  Using this date, query the dataase to get the previous 12 months of precipitation data.
3)  Load the query results into a Pandas DataFrame, with date as the index.
4)  Plot the results by using the DataFrame **plot** method.
![image](https://user-images.githubusercontent.com/111614210/201544190-eafbad0b-edd8-4bb4-b656-05d1c0ab8b6b.png)
5)  Use Pandas to print the summary statistics for the precipitation data.

![image](https://user-images.githubusercontent.com/111614210/201544234-e81dc321-5819-4fc9-8410-27e6621eee64.png)

### 1.2) Exploratory Station Analysis
1)  Identify the total number of stations by querying the dataset.
2)  Identify the most active station by querying the dataset. 
3)  Use a query that calculates the lowest, highest, and average temperatures for the most-active station.
![image](https://user-images.githubusercontent.com/111614210/201544312-3099e642-7db3-406f-8f78-3bcb1f5e9071.png)
4)  Design a query to get the previous 12 months of temperature observation (TOBS) data for most-active station.
5)  Plot the results as a histogram with bins=12.
![image](https://user-images.githubusercontent.com/111614210/201544350-6287c1d0-29e8-4ebe-a436-b7a04301741b.png)
6)  Close the session.

## 2) Design Climate App
1)  Use Flask to create the following routes:

1.1)    **/** 
-   This is the homepage. List all the available routes here.
![image](https://user-images.githubusercontent.com/111614210/201545794-8262a6c4-77f6-43dd-a7f8-410e24dffafe.png)

1.2)    **/api/v1.0/precipitation**
-   Convert the query results from the precipitation analysis, to retrieve only the last 12 months of data, to a dictionary using date as the key and prcp as the value.  
-   Return the JSON representation of your dictionary.

![image](https://user-images.githubusercontent.com/111614210/201545839-9f0616dc-55ba-47d2-9004-bc605f11679c.png)

1.3)    **/api/v1.0/stations**
-   Return a JSON list of stations from the dataset.

![image](https://user-images.githubusercontent.com/111614210/201545896-4d4647b1-8b96-43a7-a9e7-cec07c8a730c.png)

1.4)    **/api/v1.0/tobs**
-   Query the dates and temperature observations of the most-active station for the previous year of data.
-   Return a JSON list of temperature observations for the previous year.

![image](https://user-images.githubusercontent.com/111614210/201546139-2163e20d-bc9f-428f-ba04-fe2f887e2cb8.png)

1.5)    **/api/v1.0/start** and **/api/v1.0/start/end**
-   Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
-   For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
-   For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.
-   Return an error message if the start date is greater than the last available date in the dataset or if the end date is less than the oldest date in the dataset.
  
![image](https://user-images.githubusercontent.com/111614210/201546029-74eab65a-d199-4f28-8734-be215bf08738.png)![image](https://user-images.githubusercontent.com/111614210/201546075-d5344125-6771-4a75-9bce-f28aa5004e85.png)

The Python script used can be found in **SqlAlchemy_Challenge\SurfsUp\app.py**

## 3) Bonus 1: Trip Temperature Analysis 1
This analysis is performed to answer the following question: Hawaii is reputed to enjoy mild weather all year round. Is there a meaningful difference between the temperatures in, for example, June and December?

1)  The hypotheses used to answer the question above are as follows:
**Null Hypothesis**: Hawaii is reputed to enjoy mild weather all year round. The temperatures in June and December similar.
**Alternate Hypothesis**: The temperatures in June and December are different.
2)  Calculate the average temperature in June and December at all stations across all available years in the dataset.
3)  Run t-test. An unpaired t-test should be used here, as the size of the June and December tobs data are different.
4)  The unpaired t-test performed on the June and December collections gives the following results:
-   The p-value (3.9025129038616655e-191) is less than 0.05, so the null hypothesis can be rejected.
-   This means that the alternate hypothesis stands true.
-   This is also confirmed by the mean June and December temperatures calculated above. The December average temperature is around 4F less than that of June.



The Jupyter notebook used can be found in **SqlAlchemy_Challenge\SurfsUp\temp_analysis_bonus_1.ipynb**

## 4) Bonus 2: Trip Temperature Analysis 2


The Jupyter notebook used can be found in **SqlAlchemy_Challenge\SurfsUp\temp_analysis_bonus_2.ipynb**

