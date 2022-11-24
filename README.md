# SQL Project - Group 5, Fall 2022
CSCI 403, Section A

Topic: Comparing Teen Birth Rates and Education Datasets in the U.S.

## Cleaning
### Final CSV Files
The cleaned csv files used to load into our Postgres database are in this repo's root as `Birth_CleanCounty.csv` and `Education_NumsCleaned.csv`.

### Cleaning scripts
This `Cleaning` directory holds the scripts used to clean our data as well as the raw csv files.

## Queries
The python scripts for querying our database are available in the `Queries` directory. These rely on pg8000's DB-API implementation to make the queries/requests. 

### Query 1 - Q1_stats.py
```
What is the change in birth rate and education levels in Jefferson County over the past decade?
```

### Query 2 & 3 - Q2_Q3_superlatives.py
```
According to the most recent 2020 Census, which 10 counties have: 
- the highest percentage of people without a high-school education? (Q2)
- the highest birth rates? (Q3)
```

### Query 4 - Q4_percentile.py
```
In 2020, what percentage of counties above the 75th percentile for high birth rates also were in the 75th percentile for low education rates?
```


## Visualizations
Additional visualizations for the data and for queries were created using matplotlib. These can be found in the `visualizaitons` directory.