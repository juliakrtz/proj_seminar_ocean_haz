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
    seabed varchar
); 

CREATE TABLE coral_reefs (
    id serial  PRIMARY KEY,
    acres integer,
    severity varchar,
    st_area integer, 
    st_perimeter integer
); 

CREATE TABLE shark_attacks (
    id serial PRIMARY KEY, 
    date_attack timestamp, 
    time_attack timestamp,
    island varchar,
    location_attack varchar,
    location_attack_2 varchar,
    dist_from_shore varchar, 
    activity varchar,
    water_clarity integer, 
    ocean_depth integer,
    shark_type varchar
); 

CREATE TABLE hazardous_areas (
    id serial PRIMARY KEY,
    pixel_depth integer, 
    hazardous_y_n varchar
);
