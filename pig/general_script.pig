-- GENERAL SCRIPT
REGISTER piggybank.jar;
indicators = LOAD 'sut/Indicatorsh.csv' USING org.apache.pig.piggybank.storage.CSVLoader() AS(CountryName, CountryCode, IndicatorName, IndicatorCode, Year, Value);

result = FILTER indicators BY (CountryCode == 'PER') OR (CountryCode == 'PRT') OR (CountryCode == 'USA') OR (CountryCode == 'CHN') OR (CountryCode == 'CHL');
-- result = FILTER result BY (IndicatorCode == '*****CODE*****');

set default_parallel 1;
STORE result INTO 'sut/result/' USING PigStorage(';');
