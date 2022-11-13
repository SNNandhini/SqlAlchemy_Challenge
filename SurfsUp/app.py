import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///./Resources/hawaii.sqlite", connect_args={"check_same_thread": False})

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
#print(Base.classes.keys())

# Save references to the tables
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

# query to find the most active station
most_active_station = session.query(Measurement.station).group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).first()

# Find the most recent date in the data set.
recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()

# Find the oldest date in the dataset
oldest_date = session.query(Measurement.date).order_by(Measurement.date).first()

# Close Session
session.close()

# Convert the string to date, for calculating the date from last year
recent_date_dt = dt.datetime.strptime(recent_date[0], '%Y-%m-%d').date()

# Calculate the date one year from the last date in data set
recent_dt_last_yr = recent_date_dt - dt.timedelta(days=365)

# Convert the date to string, to use in the session query
date_last_yr = recent_dt_last_yr.strftime('%Y-%m-%d')

#################################################
# Set up Flask and landing page
#################################################
app = Flask(__name__)

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>Returns a JSON list of Daily Precipitation in Honolulu, Hawaii between {date_last_yr} and {recent_date_dt}<br/><br/>"
        f"/api/v1.0/stations<br/>Returns a JSON list of stations<br/><br/>"
        f"/api/v1.0/tobs<br/>Returns a JSON list of the dates and temperature observations of the most-active station ({most_active_station[0]}) between {date_last_yr} and {recent_date_dt}<br/><br/>"
        f"/api/v1.0/start_date<br/>Returns a JSON list of minimum, average and maximum temperatures between the specified start date and {recent_date_dt}<br/><br/>"
        f"/api/v1.0/start_date/end_date<br/>Returns a JSON list of minimum, average and maximum temperatures between the specified start and end dates<br/><br/>"
        f"Note:<br/>"
        f"<ol><li>Enter dates in the format 'yyyy-mm-dd'</li><br/>"
        f"<li>Enter dates within the range of {oldest_date[0]} to {recent_date[0]}</li></ol><br/><br/>"
    )

# precipitation route for the last 12 months
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)
 
    # Perform a query to retrieve the date and precipitation scores for the last 12 months
    data_12_months = session.query(Measurement.date,Measurement.prcp).filter(Measurement.date >= date_last_yr)

    # Close Session
    session.close()

    # Convert the query results to a dictionary using date as the key and prcp as the value
    prcp_dict = dict(data_12_months)

    # Return the JSON representation of the dictionary
    return jsonify(prcp_dict)

# stations route
@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Perform a query to retrieve the stations data
    stations = session.query(Station.id, Station.station, Station.name, Station.latitude, Station.longitude, Station.elevation).all()

    # Close Session
    session.close()

    # Convert the query results to dictionary
    station_data = []
    for id, station, name, lat, lng, ele in stations:
        station_dict = {}
        station_dict["id"] = id
        station_dict["station"] = station
        station_dict["name"] = name
        station_dict["latitude"] = lat
        station_dict["longitude"] = lng
        station_dict["elevation"] = ele
        station_data.append(station_dict)

    # Return the JSON representation of the dictionary
    return jsonify(station_data)

# tobs route for the most active station
@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)
   
    # Using the most active station id query the last 12 months of temperature observation data 
    temp_observation = session.query(Measurement.date, Measurement.tobs).filter(Measurement.station == most_active_station[0]).filter(Measurement.date >= date_last_yr).all()

    # Close Session
    session.close()

    # Convert the query results to dictionary
    tobs_dict = dict(temp_observation)
    tobs_dict["station"] = most_active_station[0]

    # Return the JSON representation of the dictionary
    return jsonify(tobs_dict)

# temperature routes
@app.route("/api/v1.0/<start>", defaults={'end': None})
@app.route("/api/v1.0/<start>/<end>")
def temperature(start, end):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Return "Invalid Input Dates" if the user entered start and end dates are not within the range found in the dataset (2010-01-01 to 2017-08-23).
    # Otherwise, perform the queries to calculate the min, max and avg temperatures based on the start and end dates provided by the user.
    if start > recent_date[0] or (end !=None and end < oldest_date[0]):
        return ("Invalid Input Dates")
    else:
        if end:
            temp_calc = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                filter(Measurement.date >= start).filter(Measurement.date <= end).all()
        else:
            temp_calc = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                filter(Measurement.date >= start).all()

        # Close Session
        session.close()

    # Convert the query results to dictionary
    temp_data = []
    for min, avg, max in temp_calc:
        temp_dict = {}
        temp_dict["Minimum Temperature"] = min
        temp_dict["Maximum Temperature"] = max
        temp_dict["Average Temperature"] = avg
        
    temp_dict["Start Date"] = start
    if end:
        temp_dict["End Date"] = end
    else:
        temp_dict["End Date"] = recent_date[0]
    temp_data.append(temp_dict)

    # Return the JSON representation of the dictionary
    return jsonify(temp_data)


if __name__ == "__main__":
    app.run(debug=True)