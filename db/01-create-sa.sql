SET search_path TO sa;

/* creating a search path for bathymetry, bottom type, and shark attacks 

*/

CREATE TABLE bathymetry (
    id serial PRIMARY KEY,
    bath_latitude real,
    bath_longitude real, 
    ocean_depth integer

);

CREATE TABLE bottom_type (
    id serial PRIMARY KEY, 
    code integer, 
    seabed "string" /*change this? */ 
); 

CREATE TABLE coral_reefs (
    id serial  PRIMARY KEY,
    acres integer,
    severity "string",
    st_area integer, 
    st_perimeter integer
); 

CREATE TABLE shark_attacks (
    id serial PRIMARY KEY, 
    date_time timestamp, 
    location_attack "string",
    activity "string",
    water_clarity integer, 
    shark "string"
); 

CREATE TABLE hazardous_areas (
    id serial PRIMARY KEY,
    pixel_depth integer, 
    hazardous_y_n "string"
);
