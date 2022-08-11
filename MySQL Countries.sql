-- 1. What query would you run to get all the countries that speak Slovene? Your query should return the 
-- name of the country, language and language percentage. Your query should arrange the result by language percentage in descending order. (1)

select country.Name, countrylanguage.Language, countrylanguage.Percentage from country join countrylanguage on country.Code = countrylanguage.CountryCode
where countrylanguage.Language = "Slovene";

-- 2. What query would you run to display the total number of cities for each country? Your query should return the name 
-- of the country and the total number of cities. Your query should arrange the result by the number of cities in descending order. (3)

select country.name, count(city.name) from country join city on country.Code = city.CountryCode group by country.name order by count(city.name) desc;

-- 3. What query would you run to get all the 
--  cities in Mexico with a population of greater than 500,000? Your query should arrange the result by population in descending order.

select city.name, city.Population from city where city.CountryCode = "MEX" and city.Population > 500000; 

-- 4. What query would you run to get all languages in each country with a percentage greater than 89%? Your query should arrange 
-- the result by percentage in descending order.

select * from countrylanguage where Percentage > "89%" order by Percentage desc;

-- 5. What query would you run to get all the countries with Surface Area below 501 and Population greater than 100,000?
select * from country where SurfaceArea < "501" and Population > "100000";

-- 6. What query would you run to get countries with only Constitutional Monarchy with a capital greater than 200 and a life 
--  expectancy greater than 75 years?
select * from country where Governmentform = "Constitutional Monarchy" and LifeExpectancy > 75;

-- 7. What query would you run to get all the cities of Argentina inside the Buenos Aires district and have the population greater 
-- than 500, 000? The query should return the Country Name, City Name, District and Population
SELECT * FROM city LEFT JOIN country ON country.Code = city.CountryCode WHERE country.Name = 'Argentina' AND District = 'Buenos Aires' AND city.Population > 500000;

-- 8. What query would you run to summarize the number of countries in each region? The query should display the name of the region and 
-- the number of countries. Also, the query should arrange the result by the number of countries in descending order.
SELECT *, COUNT(Code) AS 'Country Number' FROM country GROUP BY Region; 