-- NUMBER OF YEARS IN THE DATA
-- The indicators csv is as (CountryName, CountryCode, IndicatorName, IndicatorCode, Year, Value)
REGISTER piggybank.jar;
raw_indicators = LOAD 'sut/Indicatorsh.csv' USING org.apache.pig.piggybank.storage.CSVLoader() AS (CountryName, CountryCode, IndicatorName, IndicatorCode, Year, Value);

years = FOREACH raw_indicators GENERATE Year;
years = DISTINCT years;
years_groupAll = GROUP years ALL;
years_count = FOREACH years_groupAll GENERATE COUNT(years);

DUMP years_count;