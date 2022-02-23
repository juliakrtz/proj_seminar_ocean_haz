# Mapping Ocean Hazards in Hawaii

## Introduction

Millions of people around the world enjoy ocean activities in their day-to-day lives. From surfing to swimming, the ocean is the world’s largest open-resource for sports and recreation. However, participating in ocean activities comes with risk and responsibility. For example, from a study which surveyed 1,348 subjects on surfing injuries, 1,237 subjects reported acute surfing injuries, and 477 reported chronic surfing injuries (Nathanson et al., 2002: 156). Contact with the seafloor caused 17 percent of acute surfing injuries, with a higher proportion of these seafloor injuries caused by surfing over coral reef (Nathanson et al., 2002:156). 

The study also found that wave height was a factor in the type of injury sustained; forty-four percent of acute injuries occurred in waves that were shoulder high or smaller, 47 percent were in waves head high to overhead, and 9 percent were in waves double overhead or higher (Nathanson et al., 2002:158). The study concluded that this was due to the fact that most surfers were not at the advanced  level and therefore sustained injuries in smaller waves. 

Additionally, in terms of competitive surfing, the injury rate is 1.51 per 1,000 hours of surfing (Active & Safe). Factors that contribute to this risk include type of wave, wave height, the break of the wave, wind speed, wind direction and the unknown incline and composition of the sea floor, which ranges from a variety of things such as coral reefs, hard sand, and submerged rocks. 

Thus, for surfers and other ocean-goers alike, the nature of the ocean is unpredictable and can be dangerous if a person lacks knowledge about an area. It is for this reason that we chose to create our web application, which displays information on ocean hazards in Hawaii. While the features and weather data included in the web map were originally targeted at surfers, the information that is provided is applicable to anyone who partakes in an ocean-related activities and wants to know more information about the area beforehand. 

## Objective

The objective of this web application is to provide the user with information on ocean hazards from a point they pick on the map. The hope is to help reduce the amount of ocean-related injuries sustained by people who are unfamiliar with a particular spot, or who do not know the weather conditions on a given day and thus step into a more dangerous situation than they intend to. Since the data which was utilized in this application is connected to a database which is regularly updated, this means that the data which the user is able to access will hopefully achieve the objective and reduce ocean-related injuries.

## Data  

Data used:
* Sea bottom type: retrieved from [Hawaii’s GIS official website](https://geoportal.hawaii.gov/);
* Coral reefs: retrieved from [Hawaii’s GIS official website](https://geoportal.hawaii.gov/);
* Shark Attacks: retrieved from [shark attacks incidents list from State of Hawaii's site](https://dlnr.hawaii.gov/sharks/shark-incidents/incidents-list/) and stored locally as csv inside “data\original” folder;
* Hazard Areas/ocean depth: extracted shallow areas from bathymetry data from General Bathymetric Chart of the Oceans - GEBCO, available at their [data download website](https://download.gebco.net/), and stored locally as shapefile inside “data\original” folder;
* Weather data: retrieved from stormglass API (https://stormglass.io/).

## Methods  

The application was built in Python for all the backend functionalities and in JavaScript for the frontend and interaction with the user.
The backend is structured in the pre-process modules and a main.py file.
The pre-process modules get the source data, process it (in the case of shark attacks data) and store it in the database. At this step, the Python library sqlalchemy is used to connect to the database and insert the data into PostGIS. For the shark attacks data, a geographic location was not included in the original dataset, and thus locations for the shark attacks were geocoded using the geocoder library.
In the main file, a flask application was created and queries were made in order to get the data from the database. The queries then run with the inputted coordinates from the html, where it gets all data within a radius of 10,000 meters. Weather data was retrieved from stormglass API, using the inputted coordinates as well. To connect to the database and make the queries, the psycopg2 library was used. 

The frontend is structured in two html files, the “input.html” for the first interaction with the user, where no data is shown, and the “results.html” which is shown after the coordinates are submitted in the form. All the data retrieved from the database is displayed in the map as well as tables in the case of the weather data and shark attacks. To display the spatial data in a map, the JavaScript library Leaflet was used. 

The diagram below shows the project structure.

![alt text](figures/structure.png?raw=true)

## App Functionality: Running It On Your Own 

To run the app locally, the following requirements are necessary:
* Python 3.x;
* Postgres with an empty database named “geotech_ocean_haz”;
* Install packages outlined in requirements.txt file;

After that, clone the repository to your local environment and follow those steps:
1. Run all files located inside the preprocess folder;
2. In the preprocess_sharkattacks.py file, uncomment lines 69 and 74
3. In PostgreSQL, in the shark_attacks table, run the following query in order to insert a column with unique IDs:
“ALTER TABLE sharks_attacks ADD COLUMN objectid SERIAL PRIMARY KEY”;
4. Finally, run the file “main.py” and open the application locally in the browser.

## Output and visualization

The ocean hazard data which is returned from the chosen point includes the bottom type (i.e., sand, coral, rock, or mud), coral reefs in the area, the ocean depth (how many meters below the surface of the ocean the ocean floor is), weather data (wave direction, wave height, wind direction, wind speed), and shark attacks from 1995-2021. The area surrounding the chosen point has an extent of 10,000 meters. 

The interface used for the web map was Leaflet. As mentioned previously, Leaflet is an open-source JavaScript library which is especially good for interactive maps. Using Leaflet enabled the implementation of other tools for the user within the map, such as a layers control panel and a legend. Features within the map are also able to display pop-ups when clicked-on, which informs the user of the type of bottom-type, for example. 

Additionally, the stormglass API information on wave direction, wave height, wind direction, and wind speed is displayed in a table next to the map. This data also corresponds with the point the user selects. Next to the weather table is an image of a compass, so that the user is able to understand the direction which is referenced by the wave and wind direction. 

Since the shark attack data was geocoded according to island, and not beach location because not all beaches are included in the geocoder library, the shark attack data is also included in a table next to the map. The table for shark attacks returns all shark attacks for the island which is closest to the point which was selected. 

## Limitations and next steps
Some limitations and possible issues in the project are:
* Shark attacks data was copied manually from the website and stored locally as csv, so it doesn’t update automatically;
* It was not possible to geocode more specific locations (such as name of the beaches) for the shark attacks data;
* PostgreSQL credentials are not centrally located, so it is necessary to update in almost all files when there is a connection to the database;
* It is necessary to create manually a unique ID for the shark attacks table in PostgreSQL;
* Weather data can be requested maximum 10 times per day;
* In the results page, map controls (legend and layer control) don’t show up when one of the layers are not retrieved from the buffer query;
* Also in the results page, the shark attacks table shows repeated values

Next steps to this project: 
* Create a centrally located DB connection 
* Find an open-source API for the weather data
* Fix the shark attacks data table
* Visually display the buffer so that the user can see where the data stops for their specified point

## Conclusions

We were able to successfully implement ocean-hazard data into a Leaflet map to create a user-friendly application. Although there is still room for improvement, our objective of providing information in the hopes of reducing ocean-related injuries was achieved. 

## Authors

Julia Kraatz
Bachelor’s degree in Anthropology and Geography at California Polytechnic State University, San Luis Obispo
Master’s degree in Geospatial Technologies at NOVA University, WWU Muenster, and UJI 

Paula Kawahara 
Bachelor's degree in Environmental and Sanitary Engineer at Federal University of Santa Catarina, Brazil
Master's degree in Master Degree in Geographic Information Systems and Science at NOVA University

## References 

Active & Safe. (n.a.). Surfing. Active & Safe. https://activesafe.ca/surfing/ 

Nathanson et al. (2002). Surfing Injuries. American  Journal  of Emergency Medicine, 20(3), 155-160. https://pubmed.ncbi.nlm.nih.gov/11992332/ 
