# Technical assessment
 
## Prerequisites on mac os:
1. run docker command if docker is not installed then install docker using the link - https://docs.docker.com/docker-for-mac/install/

2. install Tableau  -- https://public.tableau.com/en-us/s/download

3. docker run command with volume mount: toolsets included in the docker image are  jupyter notebook, scala, python, R, spark. 
```
sudo docker run -it --rm -v /Users/host:/home/jovyan  -d -p 8888:8888 jupyter/all-spark-notebook
```
4. Firewall port should be open for BOM API connections

5. Clone repository 
```
git clone https://github.com/nsvram/cba_tech_assessment.git
```

## Steps in building Toy model to predict weather

Step 1: Data collection from API:
* By running the weather_api_data_read.ipynb script, it will download weather history for the period between 2017-01-01 and 2017-12-31. 
* It can be changed by alter the function call at the last line.
* The weather history data is joined with weather station master (../data/all_station_master.csv) to get the latitude and longitude.
* The results of the file will be saved in ../data/aus_weather_extract.csv

Note: Web API used: http://www.bom.gov.au/climate/dwo/201801/text/IDCJDW2000.201801.csv 
 
Step 2: Geo Spatial calculations and analysis 
* run the notebook predict_weather.ipynb
* Geo Spatial calculations and build toy model to predict weather as PSV file
* Read the history data loaded as part of step 1 and predict weather by weather station level.
* Find the closest weather station from all Australian airports.
* Export the predicted data in with IATA code in the expected format.

Step 3: Data validation
* Run the scala validation scala_data_validation.ipynb
* Read the final predicted .psv file
* Check the results are exported properly to meet the expectations
 
Step 4: Visualization
* Quick visualization using pandas and plotly to check the predicted model is making sense.
* Build report on tableau to check Actuals Vs Predicted
 
## Tools and Technologies
* docker
* scala 
* spark
* python
* pandas
* R 

## Acknowledgments
* jupyter/all-spark-notebook - is used
