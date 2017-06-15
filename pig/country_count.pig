-- NUMBER OF COUNTRIES
-- The indicators csv is as (CountryName, CountryCode, IndicatorName, IndicatorCode, Year, Value)

raw_indicators = LOAD 'sut/Indicatorsh.csv' USING PigStorage(',') AS (CountryName, CountryCode, IndicatorName, IndicatorCode, Year, Value);

countries = FOREACH raw_indicators GENERATE CountryCode;
countries = DISTINCT countries;
countries_groupAll = GROUP countries ALL;
countries_count = FOREACH countries_groupAll GENERATE COUNT(countries);

DUMP countries_count;