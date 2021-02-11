"""This module contains the COPY commands to load the raw data from the S3
external stage into staging data tables.
"""


COPY_WEATHER_DATA_FROM_S3 = """
//print the files found in the weather s3 bucket
list @UDACITY_WEATHER_S3_STAGE;

//copy the temperature data from the file into the table
COPY INTO NY_TEMPERATURE
  FROM @udacity_weather_s3_stage/USW00094728-temperature-degreeF.csv
  FILE_FORMAT = (format_name = "UDACITYPROJECT"."STAGING".WEATHER_CSV_FORMAT)
  FORCE = TRUE;

//copy the precipitation data from the file into the table
COPY INTO NY_PRECIPITATION
  FROM @udacity_weather_s3_stage/USW00094728-NY_CITY_CENTRAL_PARK-precipitation-inch.csv
  FILE_FORMAT = (format_name = "UDACITYPROJECT"."STAGING".WEATHER_CSV_FORMAT)
  FORCE = TRUE;

SELECT * FROM NY_TEMPERATURE ORDER BY DATE LIMIT 4;
"""

COPY_YELP_DATA_FROM_S3 = """
//copy the YELP COVID data from the file into the table
COPY INTO YELP_COVID_FEATURES
  FROM @udacity_yelp_s3_stage/covid_19_dataset_2020_06_10/yelp_academic_dataset_covid_features.json
  FILE_FORMAT = (format_name = "UDACITYPROJECT"."STAGING".YELP_JSON_FORMAT)
  FORCE = TRUE;


// copy YELP business data from file into table
COPY INTO YELP_BUSINESS
  FROM @udacity_yelp_s3_stage/yelp_dataset/yelp_academic_dataset_business.json
  FILE_FORMAT = (format_name = "UDACITYPROJECT"."STAGING".YELP_JSON_FORMAT)
  FORCE = TRUE;
  

// copy YELP checkin data from file into table
COPY INTO YELP_CHECKIN
  FROM @udacity_yelp_s3_stage/yelp_dataset/yelp_academic_dataset_checkin.json
  FILE_FORMAT = (format_name = "UDACITYPROJECT"."STAGING".YELP_JSON_FORMAT)
  FORCE = TRUE;
  
// copy YELP tip data from file into table
COPY INTO YELP_TIP
  FROM @udacity_yelp_s3_stage/yelp_dataset/yelp_academic_dataset_tip.json
  FILE_FORMAT = (format_name = "UDACITYPROJECT"."STAGING".YELP_JSON_FORMAT)
  FORCE = TRUE;
  
// copy YELP user data from file into table
COPY INTO YELP_USERS
  FROM @udacity_yelp_s3_stage/yelp_dataset/yelp_academic_dataset_user.json
  FILE_FORMAT = (format_name = "UDACITYPROJECT"."STAGING".YELP_JSON_FORMAT)
  FORCE = TRUE;
  
// copy YELP reviews data from file into table
COPY INTO YELP_REVIEWS
  FROM @udacity_yelp_s3_stage/yelp_dataset/yelp_academic_dataset_review.json
  FILE_FORMAT = (format_name = "UDACITYPROJECT"."STAGING".YELP_JSON_FORMAT)
  FORCE = TRUE;
  
// STAGE CONTENTS
list @UDACITY_YELP_S3_STAGE;

// CHECK TABLE
select * from YELP_USERS LIMIT 2;
"""
