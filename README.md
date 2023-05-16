## Extract dust value from CAMS regional air quality **netCDF4** files. 

Simple Python script and Windows .exe (compiled for x64 Windows 10/11) to extract data for certain points. The data is extracted in the same directory as the script in seperate .csv files for each station containing hourly dust data. 

# Requirements

## Windows: 
* Windows 10/11 x64
  
  ## Linux:
  * python & pip
  * tk 
  * netCDF4
  * pandas
  * geopy
  * numpy

Usage: 

# Windows: 
* Make sure you're running *Windows 10/11 x64* (not tested under x32)
* Double click the .exe file 
* Select the .nc file and the station file 
* **The station file needs to be a .csv file in the format station_code;lat;lon ex. AASTAT1;44.44;88.88**
* The resulting files should be in the same directory in which the .exe is run 

# Linux
* Make sure you have all the requirements installed
* Run the script with `python extrnetcdf_gui.py`
* Select the .nc file and the station file 
* **The station file needs to be a .csv file in the format station_code;lat;lon ex. AASTAT1;44.44;88.88**
* The resulting files should be in the same directory in which the python script is ran 