Project Title
Technical assessment
 
Getting Started
 
Setup infrastructure:
Prerequisites on mac os:
docker if not installed then install docker using the link - https://docs.docker.com/docker-for-mac/install/
install Tableau  -- https://public.tableau.com/en-us/s/download
 
docker run command and volume mount:
docker run -it --rm -p 8888:8888 jupyter/all-spark-notebook
docker,Scala,python,R,Spark
-- docker
-- sudo docker run 
-- BOM API connection (Firewall)
 
 
git clone
 
Step 1: Data collection from API:
 
By running the weather_api_data_read.py script, it will download weather history for the period between 2017-01-01 and 2017-12-31. It can be changed by alter the function call at the last line.
The weather history data is joined with weather station master (../data/all_station_master.csv) to get the latitude and longitude.
 
Web API used: http://www.bom.gov.au/climate/dwo/201801/text/IDCJDW2000.201801.csv
The results of the file will be saved in ../data/aus_weather_extract.csv
 
 
Step 2: Geo Spatial
        1. Geo Spatial calculations and build toy model to predict weather as PSV file
        2. Read the history data loaded as part of step 1 and predict weather by weather station level.
        3. Find the closest weather station from all Australian airports.
        4. Export the predicted data in with IATA code in the expected format.
 
 
Step 3: Data validation
        1. Read the final psv file
        2. Check the results are provided properly
 
Step 4: Visualization
        1. Quick visualization using pandas and plotly to check the predicted model is making sense.
        2. Build report on tableau to check Actuals Vs Predicted
 
 
