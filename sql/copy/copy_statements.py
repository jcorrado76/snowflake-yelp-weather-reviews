"""This module contains the COPY commands to load the raw data from the S3
external stage into staging data tables.

// weather stage contents
list @UDACITY_WEATHER_S3_STAGE;
// yelp stage contents
list @UDACITY_YELP_S3_STAGE;
"""

LOAD_TEMPERATURE = """
COPY INTO NY_TEMPERATURE
  FROM @udacity_weather_s3_stage/USW00094728-temperature-degreeF.csv
  FILE_FORMAT = (format_name = "UDACITYPROJECT"."STAGING".WEATHER_CSV_FORMAT)
  FORCE = TRUE;
"""

LOAD_PRECIPITATION = """
COPY INTO NY_PRECIPITATION
  FROM @udacity_weather_s3_stage/USW00094728-NY_CITY_CENTRAL_PARK-precipitation-inch.csv
  FILE_FORMAT = (format_name = "UDACITYPROJECT"."STAGING".WEATHER_CSV_FORMAT)
  FORCE = TRUE;
"""

LOAD_COVID_FEATURES = """
COPY INTO YELP_COVID_FEATURES
  FROM @udacity_yelp_s3_stage/covid_19_dataset_2020_06_10/yelp_academic_dataset_covid_features.json
  FILE_FORMAT = (format_name = "UDACITYPROJECT"."STAGING".YELP_JSON_FORMAT)
  FORCE = TRUE;
"""

LOAD_BUSINESS = """
COPY INTO YELP_BUSINESS
  FROM @udacity_yelp_s3_stage/yelp_dataset/yelp_academic_dataset_business.json
  FILE_FORMAT = (format_name = "UDACITYPROJECT"."STAGING".YELP_JSON_FORMAT)
  FORCE = TRUE;
"""

LOAD_CHECKIN = """
COPY INTO YELP_CHECKIN
  FROM @udacity_yelp_s3_stage/yelp_dataset/yelp_academic_dataset_checkin.json
  FILE_FORMAT = (format_name = "UDACITYPROJECT"."STAGING".YELP_JSON_FORMAT)
  FORCE = TRUE;
"""

LOAD_TIP = """
COPY INTO YELP_TIP
  FROM @udacity_yelp_s3_stage/yelp_dataset/yelp_academic_dataset_tip.json
  FILE_FORMAT = (format_name = "UDACITYPROJECT"."STAGING".YELP_JSON_FORMAT)
  FORCE = TRUE;
"""

LOAD_USERS = """
COPY INTO YELP_USERS
  FROM @udacity_yelp_s3_stage/yelp_dataset/yelp_academic_dataset_user.json
  FILE_FORMAT = (format_name = "UDACITYPROJECT"."STAGING".YELP_JSON_FORMAT)
  FORCE = TRUE;
"""

LOAD_REVIEWS = """
COPY INTO YELP_REVIEWS
  FROM @udacity_yelp_s3_stage/yelp_dataset/yelp_academic_dataset_review.json
  FILE_FORMAT = (format_name = "UDACITYPROJECT"."STAGING".YELP_JSON_FORMAT)
  FORCE = TRUE;
"""


COPY_WEATHER_DATA_FROM_S3 = [
        LOAD_TEMPERATURE,
        LOAD_PRECIPITATION
]

COPY_YELP_DATA_FROM_S3 = [
        LOAD_COVID_FEATURES,
        LOAD_BUSINESS,
        LOAD_CHECKIN,
        LOAD_TIP,
        LOAD_USERS,
        LOAD_REVIEWS
]
