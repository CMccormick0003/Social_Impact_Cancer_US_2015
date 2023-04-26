# Social_Impact_Cancer_US_2015
Social characteristics include a person's age, gender, race, marital status, level of education completed, zip code they live in, size of the town they live in, and the average age of people in the town. Economic characteristics include median income, employment status, poverty rate in their community, and type of health insurance coverage. CDC’s National Program of Cancer Registries and the National Cancer Institute’s (NCI’s) Surveillance, Epidemiology, and End Results Program annually produce U.S. Cancer Statistics data, which are the official federal cancer statistics. U.S. Cancer Statistics provides cancer information on the entire U.S. population.  In 2015, a total of 1,633,390 new cancer cases were reported in the United States: 816,937 in men and 816,453 in women. The overall incidence rate was 437.7 per 100,000 persons.  We were intersted in exploring the impact of different social and econmic factors on cancer and healthin different regions of the United States.  The 2019 dataset was not fully available to us, so we have used the 2015 data set for our analysis.

This repository is for a database used to house data in SQL, powered by Python Flask API, including html and javascript.  This project included web scraping of data collected from the internet, data cleaning with Python in a Jupyter notebook, use of SQL and postgres to load data to vscode to create an api, development of a webpage with visuals based on the data loaded from SQL.  One of the visuals includes an interactive component for the viewer.

The source data was obtained from Kaggle at the following link on 12Apr2023.
https://www.kaggle.com/datasets/thedevastator/uncovering-trends-in-health-outcomes-and-socioec
License: https://creativecommons.org/licenses/by/4.0/
The source data was 2 csv files: av-household-size.csv and cancer-reg.csv.

**avg-household-size.csv**
This csv includes 4 columns and 3220 data rows.
Column name	Description
statefips	State identification number. (Integer)
countyfips	County identification number. (Integer)
avghouseholdsize	Average size of households in the county. (Float)
geography	Location name. (String)

**cancer_reg.csv**
This csv includes 32 columns and 3047 data rows.
Column name	Description
geography	Location name. (String)
avganncount	Average annual count of cancer cases in the county. (Numeric)
avgdeathsperyear	Average number of deaths per year in the county. (Numeric)
target_deathrate	Number of deaths per 100k individuals in each county. (Numeric)
medincome	Median household income for the county. (Numeric)
popest2015	Population estimates for 2015. (Numeric)
povertypercent	Percentage of people living in poverty. (Numeric)
studypercap	Number of clinical trials per capita in the given county. (Numeric)
binnedinc	Binned income for each county. (Categorical)
medianage	Median age of the population in the county. (Numeric)
medianagemale	Median age of the male population in the county. (Numeric)
medianagefemale	Median age of the female population in the county. (Numeric)
percentmarried	Percentage of people who are married in the county. (Numeric)
pctnohs18_24	Percentage of people aged 18-24 who did not graduate high school. (Numeric)
pcths18_24	Percentage of people aged 18-24 who graduated high school. (Numeric)
pctsomecol18_24	Percentage of people aged 18-24 who attended some college. (Numeric)
pctbachdeg18_24	Percentage of people aged 18-24 who have a bachelor's degree. (Numeric)
pcths25_over	Percentage of people aged 25 and over who graduated high school. (Numeric)
pctbachdeg25_over	Percentage of people aged 25 and over who have a bachelor's degree. (Numeric)
pctemployed16_over	Percentage of people aged 16 and over who are employed. (Numeric)
pctunemployed16_over	Percentage of people aged 16 and over who are unemployed. (Numeric)
pctprivatecoverage	Percentage of people with private health insurance
pctprivatecoveragealone	Percentage of people with private health insurance only
pctempprivcoverage	Percentage of people with temporary private health insurance
pctpubliccoverage	Percentage of people with public health insurance
pctpubliccoveragealone	Percentage of people with public health insurance only
pctwhite	percent White
pctblack	percent Black
pctasian	percent Asian
pctotherrace	percent other race (not White,Black or Asian)
pctmarriedhouseholds	percent of married household per county
birthrate	percent born per 1000,000

xxxxxxxxxx some thigns we cleaned adn dropped and new columns we created by grouping data

Loaded in CSV into postgres sql by using sqlalchemy. Created a config file and creating an engine to connect with postgres.

differnet visualizations, work in progress

copy stuff from the ppt
