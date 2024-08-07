# Import the dependencies.
from flask import Flask, jsonify
import pandas as pd
import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, desc


#################################################
# Database Setup
#################################################

# Create engine
engine = create_engine("sqlite:///../Surfs_Up/Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

# Homepage route
@app.route('/')
def Welcome():
    return(
        f"Welcome to the Hawaiian Climate Analysis API Homepage!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start/2016-8-23<br/>"
        f"/api/v1.0/start/2016-8-23/end/2017-8-23"
    )
    

# Precipitation Route
@app.route('/api/v1.0/precipitation')
def precipitation():
    # Calculate the date from one year ago
    prior_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    # Query the database
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prior_year).\
        order_by(Measurement.date).all()
    # Create a dictionary from the results
    precip = {date: prcp for date, prcp in precipitation}
    # Return JSON response
    return jsonify(precip)

# Stations Route
@app.route('/api/v1.0/stations')
def stations():
    # Start Session
    session = Session(engine)
    # Define columns to select
    sel = [Station.station, Station.name, Station.longitude, Station.latitude, Station.elevation]
    # Execute the query
    results = session.query(*sel).all()
    # Close the session
    session.close

    # Create the list of the stations with the desired order
    stations = []
    for station, name, lon, lat, elevation in results:
        station_dict = {}
        # Station number
        station_dict['Station'] = station
        # Station name      
        station_dict['Name'] = name 
        # Station Latitude            
        station_dict['Lat'] = lat               
        # Station Longitude
        station_dict['Lon'] = lon              
        # Station elevation
        station_dict['Elevation'] = elevation   
        stations.append(station_dict)

    # Return the JSON response
    return jsonify(stations)

# Tobs Route
@app.route('/api/v1.0/tobs')
def tobs():

    # Start Session
    session = Session(engine)
    # Query the temperature data
    temp_results = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.date > '2016-08-23').\
        order_by(Measurement.date).all()
    # Create a list of temperature records
    temperatures = []
    for date, tobs in temp_results:
        results = {}
        results['Temperature'] = tobs
        results['Date'] = date
        temperatures.append(results)
    # Return JSON response
    return jsonify(temperatures)

# Start Route
@app.route('/api/v1.0/start/<start>')
def start(start):

    # Parse the start date
    start_date = dt.datetime.strptime(start, "%Y-%m-%d").date()

     # Query the min, average, and max temperature for start date on
    start = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    stats = [func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)]
        
    stats_result = session.query(*stats).\
        filter(Measurement.date >= start_date).all()

     # Format the result as a dictionary
    temp_stats = {
    "Start Date": start,
    "Low Temperature": stats_result[0][0],
    "High Temperature": stats_result[0][1],
    "Average Temperature": stats_result[0][2]
    }
    
    # Return JSON response
    return jsonify(temp_stats)

@app.route('/api/v1.0/start/<start>/end/<end>')
def date_range(start, end):
    start = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    end_eq = session.query(Measurement.date).order_by(desc(Measurement.date)).first()
    end_str = end_eq[0]
    end = dt.datetime.strptime(end_str, '%Y-%m-%d').date()
    temp_stats = [func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)]
    start_end_results = session.query(*temp_stats).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()



    # Create a list
    temperatures  = {
    "Start Date": start,
    "End Date": end,
    "Low Temperature": start_end_results[0][0],
    "High Temperature": start_end_results[0][1],
    "Average Temperature": start_end_results[0][2]
    }
    


    # Return JSON response
    return jsonify(temperatures)

# Close session
session.close()


# Define main behavior
if __name__ == "__main__":
    app.run(debug=True)