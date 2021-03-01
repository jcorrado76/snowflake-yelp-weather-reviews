"""The purpose of this module is to contain the SQL statements for loading the
YELP data into the ODS in 3NF
"""


INSERT_BUSINESS_CATEGORIES = """
INSERT INTO "UDACITYPROJECT"."ODS"."YELP_BUSINESS_CATEGORIES" (
  BUSINESS_ID,
  CATEGORY
)
SELECT
  json_rows:business_id,
  TRIM(VALUE)
FROM "UDACITYPROJECT"."STAGING"."YELP_BUSINESS" as  business,
     LATERAL FLATTEN(SPLIT(business.json_rows:categories, ','));
"""

INSERT_YELP_BUSINESSES = """
INSERT INTO "UDACITYPROJECT"."ODS"."YELP_BUSINESSES" (
  ID,
  NAME,
  ADDRESS,
  STATE,
  CITY,
  IS_OPEN,
  LATITUDE,
  LONGITUDE,
  ZIP_CODE,
  REVIEW_COUNT,
  STARS
)
SELECT
  json_rows:business_id id,
  json_rows:name name,
  json_rows:adress address,
  json_rows:state state,
  json_rows:city city,
  TRIM(json_rows:is_open)::BOOLEAN is_open,
  json_rows:latitude latitude,
  json_rows:longtidue longitude,
  json_rows:postal_code zip_code,
  json_rows:review_count review_count,
  json_rows:stars stars
FROM "UDACITYPROJECT"."STAGING"."YELP_BUSINESS";
"""

INSERT_YELP_ELITE_MEMBERSHIPS = """
INSERT INTO "UDACITYPROJECT"."ODS"."YELP_USER_ELITE_MEMBERSHIP" (
  user_id,
  elite_year
)
SELECT
  json_rows:user_id,
  CASE
    WHEN VALUE = '' THEN NULL
    ELSE TRIM(VALUE)::INT
  END AS elite_year_membership
FROM "UDACITYPROJECT"."STAGING"."YELP_USERS" as  user,
     LATERAL FLATTEN(SPLIT(user.json_rows:elite, ','));
"""

INSERT_YELP_USER_FRIENDS = """
INSERT INTO "UDACITYPROJECT"."ODS"."YELP_USER_FRIENDS" (
  user_id,
  friend_id
)
SELECT json_rows:user_id, TRIM(VALUE)
FROM "UDACITYPROJECT"."STAGING"."YELP_USERS" AS user,
     LATERAL FLATTEN(SPLIT(user.json_rows:friends, ','));
"""

INSERT_YELP_TIPS = """
INSERT INTO "UDACITYPROJECT"."ODS"."YELP_TIPS" (
  USER_ID,
  BUSINESS_ID,
  TEXT,
  TIMESTAMP,
  COMPLIMENT_COUNT
)
SELECT
  json_rows:user_id,
  json_rows:business_id,
  json_rows:text,
  json_rows:date::TIMESTAMP,
  json_rows:compliment_count
FROM "UDACITYPROJECT"."STAGING"."YELP_TIP";
"""


INSERT_YELP_CHECKINS = """
INSERT INTO "UDACITYPROJECT"."ODS"."YELP_CHECKINS"(
  business_id,
  timestamp
)
SELECT
  json_rows:business_id,
  TRIM(VALUE)::TIMESTAMP AS TIMESTAMP
FROM
  "UDACITYPROJECT"."STAGING"."YELP_CHECKIN" AS checkins,
     LATERAL FLATTEN(SPLIT(checkins.json_rows:date, ','));
"""

INSERT_YELP_REVIEWS = """
INSERT INTO "UDACITYPROJECT"."ODS"."YELP_REVIEWS"(
  review_id,
  user_id,
  business_id,
  stars,
  useful,
  funny,
  cool,
  review,
  timestamp
)
SELECT
  json_rows:review_id,
  json_rows:user_id,
  json_rows:business_id,
  json_rows:stars,
  json_rows:useful,
  json_rows:funny,
  json_rows:cool,
  json_rows:text AS REVIEW,
  json_rows:date::TIMESTAMP
FROM "UDACITYPROJECT"."STAGING"."YELP_REVIEWS";
"""
YELP_ETL_QUERIES = [
        INSERT_BUSINESS_CATEGORIES,
        INSERT_YELP_BUSINESSES,
        INSERT_YELP_ELITE_MEMBERSHIPS,
        INSERT_YELP_USER_FRIENDS,
        INSERT_YELP_TIPS,
        INSERT_YELP_CHECKINS,
]
