# SqlAlchemy_Challenge
Surf’s Up

This challenge is to perform a climate analysis using the data collected from 2010 to 2017 in Honolulu, Hawaii. This is done in 2 steps:
1)  **Analyze and Explore Climate Data** - Do a basic climate analysis and data exploration of the climate database using SQLAlchemy ORM queries, Pandas and Matplotlib.
2)  **Design Climate App** - After completing the initial analysis, design a Flask API based on the queries that were just developed.  

##  Analyze and Explore Climate Data
This step involves analysing Precipitation and Weather Stations data. 

For this, the connection between Python and SQLite Database is established by performing the following steps:
1)  Use the SQLAlchemy **create_engine()** function to connect to the SQLite database.
2)  Use the SQLAlchemy **automap_base()** function to reflect the tables into classes, and then save references to the classes named Station and Measurement.
3)  Link Python to the database by creating a **SQLAlchemy session**.

### Exploratory Precipitation Analysis
1)  Find the most recent date in the dataset.
2)  Using this date, query the dataase to get the previous 12 months of precipitation data.
3)  Load the query results into a Pandas DataFrame, with date as the index.
4)  Plot the results by using the DataFrame **plot** method.
5)  Use Pandas to print the summary statistics for the precipitation data.

### Exploratory Station Analysis
1)  Identify the total number of stations by querying the dataset.
2)  Identify the most active station by querying the dataset. 
3)  Use a query that calculates the lowest, highest, and average temperatures for most-active station.
4)  Design a query to get the previous 12 months of temperature observation (TOBS) data for most-active station.
5)  Plot the results as a histogram with bins=12.