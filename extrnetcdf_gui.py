import tkinter as tk
from tkinter import filedialog
import netCDF4
import pandas as pd
from geopy.distance import geodesic
import numpy as np

# Open the NetCDF file
nc_filename = filedialog.askopenfilename(title='Select NetCDF file', filetypes=[('NetCDF Files', '*.nc')])
nc_file = netCDF4.Dataset(nc_filename)
# Access the subgroup containing the variables if necessary
# data_group = nc_file.groups['data_group']

# Get the relevant variables from the NetCDF file
lats = nc_file.variables['latitude'][:]
lons = nc_file.variables['longitude'][:]
dust = nc_file.variables['dust'][:]  # Assuming the variable name is 'dust'

# Read the station data from the CSV file
stations_file = filedialog.askopenfilename(title='Select stations file', filetypes=[('CSV Files', '*.csv')])
station_data = pd.read_csv(stations_file, delimiter=';')
# Iterate over the stations
for index, station in station_data.iterrows():
    station_lat = station['lat']
    station_lon = station['lon']

    # Calculate the distances between the station and all grid points
    distances = [geodesic((station_lat, station_lon), (lat, lon)).kilometers for lat, lon in zip(lats, lons)]

    # Find the index of the closest grid point
    closest_index = distances.index(min(distances))

    # Extract the dust values for each hour at the closest grid point
    hourly_values = dust[:, 0, closest_index // lons.size, closest_index % lons.size]

    # Create a DataFrame for the station data
    station_df = pd.DataFrame({'hour': np.arange(744), 'dust_value': hourly_values.tolist()})

    # Get the station name for the file name
    # Remove the asterisk since it's not an allowed Windows symbol
    #station_name = station['station_code']
    station_name = station['station_code'].replace('*', '')

    # Save the station data to a separate CSV file
    file_name = f'{station_name}.csv'
    station_df.to_csv(file_name, index=False)

# Close the NetCDF file
nc_file.close()
