"""This module contains the SQL queries to create the ODS tables holding the
weather data.
This data is in 3NF, as required by the ODS
"""

WEATHER_ODS_SQL_QUERIES = """
CREATE OR REPLACE SEQUENCE date_id_seq;
CREATE TABLE "UDACITYPROJECT"."ODS"."WEATHER_DATES" (
  "DATE_ID" INTEGER DEFAULT date_id_seq.nextval PRIMARY KEY, 
  "DATE" DATE NOT NULL
) 
COMMENT = 'This will be the table to hold the weather dates';

CREATE OR REPLACE TABLE "UDACITYPROJECT"."ODS"."PRECIPITATION" (
  "DATE_ID" INTEGER PRIMARY KEY FOREIGN KEY REFERENCES "UDACITYPROJECT"."ODS"."WEATHER_DATES"("DATE_ID"), 
  "PRECIPITATION" FLOAT,
  "PRECIPITATION_NORMAL" FLOAT NOT NULL
) 
COMMENT = 'This will be the table to hold the weather precipitation data';

CREATE TABLE "UDACITYPROJECT"."ODS"."TEMPERATURE" (
  "DATE_ID" INTEGER PRIMARY KEY FOREIGN KEY REFERENCES "UDACITYPROJECT"."ODS"."WEATHER_DATES"("DATE_ID"), 
  "MIN" FLOAT,
  "MAX" FLOAT,
  "NORMAL_MIN" FLOAT NOT NULL,
  "NORMAL_MAX" FLOAT NOT NULL
) 
COMMENT = 'This will be the table to hold the weather temperature data';
"""
