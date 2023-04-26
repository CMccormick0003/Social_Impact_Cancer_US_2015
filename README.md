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
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

Loaded in CSV into postgres sql by using sqlalchemy. Created a config file and creating an engine to connect with postgres.
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

Analysis of visuals:
COUNTY  -  Mortality Rate vs Poverty % (per county) 
This graph shows the mortality rate per 100,000 on the y-axis as plotted against poverty rates per county on the x-axis.
X: Poverty % (range 3.2% to 47.4%)  Y: Mortality Rate (range 48.5 to 513.6 per 100,000
We hypothesized that there would be an upward relationship between the variables, as poverty increased mortality woudl increase as well.
Althought there appears to be an upward trend for mortality rate as poverty increaes from 0 to 10%, the rest of the graph appears faily linear and has a lot of noise between 10 and 48.5%.  This graphs shows all the counties in the dataset, over 3,000.  If we show data for a more focused region or state or for a spcific poverty level, data may separate on the graph.  This comparison should be analyzed further together with other factors that may be related such as household size or marital status (for docial and economic support) and insurance (access to care) to further investigate the relationship between poverty level and mortality.
![MortalityvPovertyUS_chart1](https://user-images.githubusercontent.com/120672518/234466785-edeb719f-533a-4ff5-8e57-591b47d43f08.png)


COUNTY  -  Cancer Incidence Rate vs. Population (per county) 
- There is more variability in the countries with lower population.  THe data for counties with higher population (for example, over 90,000 people) was generally tighter with less variability.
- Two counties were outliers.  Cancer incidence rates for 3015 counties in the data were between 201.3 and 718.9. However the cancer incidence rate for two counties was much higher.  These data should be further investigated to see if there is a cluster event of cancer diagnoses for a specific cause (perhaps related to an environmental or other public health issue) or if there was an error in data collection or analysis from the source data from which the Kaggele data set authors obtained these data.
    Union County, Florida - population 15,234, cancer incidence of 1206.9 per 100,000 people, median age 40.3 years.
    Williamsburg City, Virginia population 15,052 and cancer incidence of 1014.2 per 100,000 people, median age 24.6 years.
-Note, the x-axis includes datapoint on the graph shows values up to ~3.3 million, however the last 14 data points in teh dataset are not included in the grphh
![CancerIncidvPopUS_chart4](https://user-images.githubusercontent.com/120672518/234466807-7a33bf4b-d9da-4a03-a215-a1821a613bbb.png)


COUNTY  -  Mortality Rate in US (per county) (under construction)
add description and limitations here
and here and her
![MortalityRateCountymapChart7x](https://user-images.githubusercontent.com/120672518/234466917-42b09b38-7c52-4125-81b9-62b85eeaf5f8.png)


STATE  -  Cancer Incidence Per State
add description and limitations here
and here and here
example lesson of outlier and picking the right colors wide palate for data with extremes
![CancerRateUS_chloropleth_map](https://user-images.githubusercontent.com/120672518/234466962-ce17840d-ce04-48e7-a5b6-63e773b67aef.png)
![CancerRateUS_chloropleth_multicolor](https://user-images.githubusercontent.com/120672518/234467309-34bb788d-11f3-431a-9db7-db1b8908516b.png)



STATE  -  Health Rates per State (Cancer Incidence, Mortality Rate, & Target Death Rate) *zoom im*
add description and limitations here
and here and her
![HealthRatesUSscatterStateChart6](https://user-images.githubusercontent.com/120672518/234467518-4e4886c5-8ebf-4057-a61c-b3711086f5ab.png)


UNITED STATES  -  Target Death Rate in US (under construction)
add description and limitations here
and here and her
![TargetDeathRateUSmapx](https://user-images.githubusercontent.com/120672518/234467616-7be573e3-c179-480f-b22c-7b59cd68c29b.png)

Visuals under construction
COUNTY  -  Mortality Rate in US (per county) (under construction)
UNITED STATES  -  Target Death Rate in US (under construction)
