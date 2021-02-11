# Introduction
***
The purpose of this project is to perform the ETL steps that would be required, and some basic analysis to understand if the weather in a given area has an affect on local yelp reviews.

For this project, I've used the YELP review data set and weather data for New York City.

I will be loading this data into Snowflake and performing the proper ETL required to analyze this data in a downstream system.

# SQL Queries
***
The SQL queries for this project are organized into three folders:
* copy - copy data from external stage to staging tables
* create - create ODS tables
* insert - insert data into ODS

This way, SQL statements of a similar nature are placed close together.
Note that I didn't add the SQL query statements for creating the staging tables, as I had created those in the web browser.
They were straightforward, and don't have any specific information about the files, besides their file formats.
