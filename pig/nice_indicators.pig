-- 
-- The indicators csv is as (CountryName, CountryCode, IndicatorName, IndicatorCode, Year, Value)
REGISTER piggybank.jar;
raw_indicators = LOAD 'sut/Indicatorsh.csv' USING org.apache.pig.piggybank.storage.CSVLoader() AS (CountryName, CountryCode, IndicatorName, IndicatorCode, Year, Value);

grouped_indicators = GROUP raw_indicators BY IndicatorName;

grouped_indicators_count = FOREACH grouped_indicators GENERATE group, COUNT($1) as N;

grouped_indicators_filtered = FILTER grouped_indicators_count BY (N >= 13000);

dump grouped_indicators_filtered;

