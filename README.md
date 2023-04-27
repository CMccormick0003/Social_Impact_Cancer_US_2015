# Social_Impact_Cancer_US_2015
We were intersted in exploring the impact of different social and econmic factors on cancer and healthin different regions of the United States.  Social characteristics include a person's age, gender, race, marital status, level of education completed, zip code they live in, size of the town they live in, and the average age of people in the town. Economic characteristics include median income, employment status, poverty rate in their community, and type of health insurance coverage. We sought to understand the incidence of cancer regionally and nationally and how different social and economic factors impacted people's health and rate of  death.
# The data source we selected to evaluate is from 2015 and is a composite of data from the American Community Survey, clinicaltrials.gov, and cancer.gov.
This repository is for a database used to house data in SQL, powered by Python Flask API, including html and javascript.  This project included web scraping of data collected from the internet, data cleaning with Python in a Jupyter notebook, use of SQL and postgres to load data to vscode to create an api, development of a webpage with visuals based on the data loaded from SQL.  One of the visuals includes an interactive component for the viewer.


Per the CDC, in 2015, a total of 1,633,390 new cancer cases were reported in the United States: 816,937 in men and 816,453 in women. The overall incidence rate was 437.7 per 100,000 persons.  (United States Cancer Statistics: Highlights from 2015 Incidence, https://www.cdc.gov/cancer/uscs/about/data-briefs/no3-USCS-highlights-2015-incidence.htm#:~:text=CDC%E2%80%99s%20National%20Program%20of%20Cancer%20Registries%20and%20the,men%20had%20higher%20cancer%20incidence%20rates%20than%20, accessed on 12Apr2023  These statistics are just a few of the official federal cancer statistics for the whole United States population that are compiled every year by the National Program of Cancer Registries of the CDC and the National Cancer Institute’s (NCI’s) Surveillance, Epidemiology, and End Results Program.  Although more recent data were available as fact sheets or on dashboards, comprehensive datasets were not available to analyze.  Thus, we chose to use 2015 data.


The source data was obtained from Kaggle at the following link on 12Apr2023.
https://www.kaggle.com/datasets/thedevastator/uncovering-trends-in-health-outcomes-and-socioec
License: https://creativecommons.org/licenses/by/4.0/
The source data was 2 csv files: av-household-size.csv and cancer-reg.csv.

**avg-household-size.csv**
This csv includes 4 columns and 3220 data rows.
|      Column name         |                                   Description                                    |
|--------------------------|--------------------------------------------------------------------------------- |
| statefips                |    State identification number. (Integer)                                        |
| countyfips               |    County identification number. (Integer)                                       |
| avghouseholdsize         |    Average size of households in the county. (Float)                             |
| geography                |    Location name. (String)                                                       |



**cancer_reg.csv**
This csv includes 32 columns and 3047 data rows.
|  Column name             |                                    Description                                   | 
|--------------------------|--------------------------------------------------------------------------------- |
|  geography               |    Location name. (String)                                                       | 
|  avganncount             |    Average annual count of cancer cases in the county. (Numeric)                 | 
|  avgdeathsperyear        |    Average number of deaths per year in the county. (Numeric)                    | 
|  target_deathrate        |    Number of deaths per 100k individuals in each county. (Numeric)               | 
|  medincome               |    Median household income for the county. (Numeric)                             | 
|  popest2015              |    Population estimates for 2015. (Numeric)                                      | 
|  povertypercent          |    Percentage of people living in poverty. (Numeric)                             | 
|  studypercap             |    Number of clinical trials per capita in the given county. (Numeric)           | 
|  binnedinc               |    Binned income for each county. (Categorical)                                  | 
|  medianage               |    Median age of the population in the county. (Numeric)                         | 
|  medianagemale           |    Median age of the male population in the county. (Numeric)                    | 
|  medianagefemale         |    Median age of the female population in the county. (Numeric)                  | 
|  percentmarried          |    Percentage of people who are married in the county. (Numeric)                 | 
|  pctnohs18_24            |    Percentage of people aged 18-24 who did not graduate high school. (Numeric)   | 
|  pcths18_24              |    Percentage of people aged 18-24 who graduated high school. (Numeric)          | 
|  pctsomecol18_24         |    Percentage of people aged 18-24 who attended some college. (Numeric)          | 
|  pctbachdeg18_24         |    Percentage of people aged 18-24 who have a bachelor's degree. (Numeric)       | 
|  pcths25_over            |    Percentage of people aged 25 and over who graduated high school. (Numeric)    | 
|  pctbachdeg25_over       |    Percentage of people aged 25 and over who have a bachelor's degree. (Numeric) | 
|  pctemployed16_over      |    Percentage of people aged 16 and over who are employed. (Numeric)             | 
|  pctunemployed16_over    |    Percentage of people aged 16 and over who are unemployed. (Numeric)           | 
|  pctprivatecoverage      |    Percentage of people with private health insurance                            | 
|  pctprivatecoveragealone |    Percentage of people wto eith private health insurance only                       | 
|  pctempprivcoverage      |    Percentage of people with temporary private health insurance                  | 
|  pctpubliccoverage       |    Percentage of people with public health insurance                             | 
|  pctpubliccoveragealone  |    Percentage of people with public health insurance only                        | 
|  pctwhite                |    Percent White                                                                 | 
|  pctblack                |    Percent Black                                                                 | 
|  pctasian                |    Percent Asian                                                                 | 
|  pctotherrace            |    Percent other race (as identified by respondent)                              | 
|  pctmarriedhouseholds    |    Percent of married household per county                                       | 
|  birthrate               |    Percent born per 1000,000                                                     | 

THe data was cleaned in a  variety of ways.Examples are beloe
#Create a new field for medincome to bin the values into categories.  The new field is called "medincome" range.
#Create a new field for race to provide the value to reach 100% for race total % for the county. The new field is called race_undef. 
#Create a new field for medianage to bin the values into categories.  The new field is called medianage_range.
#Create a new field called studypercap_range that summarizes the number of research studies in each county into bins based on the number of studies in the field studypercap.
# Create the pop_range field using pd.cut() to create categories for county population
THen we dropped fields we did not plan to use in the analyses or data visuals and reordered the fields so the newly created fields were located close to their source column.  
This cleaned data was saved as a csv.
We furhter cleaned the data to remove illogical data such as 30 counties where the median age was over 100 years of age.
THe county location field was split into two columns, one for the county name and one for the state id (2 letter abbreviation of the state).
THen we merged the clean csv called cancer_reg_clean with the csv called gps to include geographical information such as latitude and longitude for each county.  This will allow mapping of data.
Rows that included gps data but no health data can be dropped.
Soem data categories did not sum to 100%, so those categories were not plotted at this time. For exampe the unemployed and employed percentages do not equal 100% for each county and there were numerous counties with missing employed percents.  
We created a new dataframe (cancer_per_state) to hold health rates per state and created new columns to house these calculated values: state_cancer_incidence_rate,  state_mortality_rate, state_target_deathrates
After creating the cancer_per_state dataframe, use the .loc accessor to assign the calculated values from clean dataframe of county data to the 50 rows (state names) in the cancer_per_state dataframe
#Now we have 2 csv files to load import into SQL, one based on county data and one based on state data.

#A database was created in postgres SQL.
A table was created in SQL.
Each csv was imported into postgres SQL by using sqlalchemy.

***************************************************************************************************************************
#HTML environment was created for user interaction and to display the visuals
#Flask was used to create the visuals and used to connect to the HTML file.
#A config file was created creating an engine to connect with postgres. 
#An api used to pull the data from its location. when the user clicked for the chart.
***************************************************************************************************************************

#HTML:
THe website explains the purpose of the site and provides some background information.
THe user is invited to engage with the visuals on a dashboard by clicking the title of each one.
THe visuals are arranged by the type of data they display (county, state or country [US]).  

In the future, the HTML coudl be updated:
- images could be loaded ot the site to enhance the user's experience, show and icon for each category, etc
- examples of other categories for visuals could include sections such as economic, social, community, education, and medical
- add a resources section to provide information on how to access research studies or advocacy groups
- add tips on maintaing personal and family health and financial stability related to healthcare

This is a visual of the website:
![website_visual](https://user-images.githubusercontent.com/120672518/234731892-df4f875b-eaba-48e6-8217-df67ada2e78d.png)


#ANALYSIS OF VISUALS:

#COUNTY  -  Mortality Rate vs Poverty % (per county) 
This graph shows the mortality rate per 100,000 on the y-axis as plotted against poverty rates per county on the x-axis.
X: Poverty % (range 3.2% to 47.4%)  Y: Mortality Rate (range 48.5 to 513.6 per 100,000
We hypothesized that there would be an upward relationship between the variables, as poverty increased mortality woudl increase as well.
Althought there appears to be an upward trend for mortality rate as poverty increaes from 0 to 10%, the rest of the graph appears faily linear and has a lot of noise between 10 and 48.5%.  This graphs shows all the counties in the dataset, over 3,000.  If we show data for a more focused region or state or for a spcific poverty level, data may separate on the graph.  This comparison should be analyzed further together with other factors that may be related such as household size or marital status (for docial and economic support) and insurance (access to care) to further investigate the relationship between poverty level and mortality.
![MortalityvPovertyUS_chart1](https://user-images.githubusercontent.com/120672518/234466785-edeb719f-533a-4ff5-8e57-591b47d43f08.png)


#COUNTY  -  Cancer Incidence Rate vs. Population (per county) 
- There is more variability in the countries with lower population.  THe data for counties with higher population (for example, over 90,000 people) was generally tighter with less variability.
- Two counties were outliers.  Cancer incidence rates for 3015 counties in the data were between 201.3 and 718.9. However the cancer incidence rate for two counties was much higher.  These data should be further investigated to see if there is a cluster event of cancer diagnoses for a specific cause (perhaps related to an environmental or other public health issue) or if there was an error in data collection or analysis from the source data from which the Kaggele data set authors obtained these data.
    Union County, Florida - population 15,234, cancer incidence of 1206.9 per 100,000 people, median age 40.3 years.
    Williamsburg City, Virginia population 15,052 and cancer incidence of 1014.2 per 100,000 people, median age 24.6 years.
-Note, the x-axis includes datapoint on the graph shows values up to ~3.3 million, however the last 14 data points in teh dataset are not included in the grphh
![CancerIncidvPopUS_chart4](https://user-images.githubusercontent.com/120672518/234466807-7a33bf4b-d9da-4a03-a215-a1821a613bbb.png)

#STATE  -  Cancer Incidence Per State
THis chloropleth shows the cancer incidence per state.  
THe first map below does not show any colors because two states have outlier data.  Kansas (KS) and Minnesota (MN) have a cancer incidence rate of 7006 and 3110.  Nevada is 1154.  THe rest of the states have data that is closer in size and ranges from 307 to 617 people diagnosed /100,000.  Without futher digging into the data, we can not be certain if NV, KS and MN data are accurate or if there is a data error in rounding.
If we want to still display the same data set on a chloropleth, consider suing a color palate that has more colors as is shown in the bottom graph and not more of the states' data become visualized.
![CancerRateUS_chloropleth_map](https://user-images.githubusercontent.com/120672518/234466962-ce17840d-ce04-48e7-a5b6-63e773b67aef.png)
![CancerRateUS_chloropleth_multicolor](https://user-images.githubusercontent.com/120672518/234467309-34bb788d-11f3-431a-9db7-db1b8908516b.png)


#UNITED STATES - Correlation of Social Factors to Mortality Rate in US
This is a polar graph that shows how much each criteria impacts the field in the middle of the graph.
You can "Zoom In" by using hte zoom button on the top right of the graph.
This rgaph shows that poverty %, unemployment % and public insurance coverage (eg, Medicare or Medicaid) are most highly related to Target Death Rate.  Moving one of these three levers has more impact than the others around the circle.
This model is multivariate and can be refined by choosing other fields in the dataset to see what has more or less impact relative to others.
![SocialImpactPolarZoomChart5](https://user-images.githubusercontent.com/120672518/234737713-952e0329-af5a-4a5d-9518-55d2688ae5e6.png)


#STATE - Health Rates per State (Cancer Incidence, Mortality Rate, & Target Death Rate) *zoom im*
THis graph shows the cancer incidence, mortality rate and target death rate per state as a scatter plot.
THe state abbreviations are not appearing on the graph and that is being updated.
![HealthRatesUSscatterStateChart6](https://user-images.githubusercontent.com/120672518/234736379-caa86736-5c26-472d-a47a-05eecdb4e551.png)



#GRAPHS UNDER CONSTRUCTION
THe visuals had generated during the build and we are working on modifying these graphs.  A prior view of the visual is shown under each heading.

#COUNTY  -  Mortality Rate in US (per county) (under construction)
THis graph shows the death rate per county in the US. 
Data are not available for states in white.
![MortalityRateCountymapChart7x](https://user-images.githubusercontent.com/120672518/234737738-974aad19-8c55-49c7-8e3f-de32cee3473a.png)

#UNITED STATES  -  Target Death Rate in US (under construction)
Target death rate is the rate of deaths set as a goal by the federal government for each region.  It is not the same for all regions as it takes into consideration existing factors in the region and current social and economic data and other health and mortality rates.
![TargetDeathRateUSmapx](https://user-images.githubusercontent.com/120672518/234737758-d1956e78-c32d-47a4-9b8b-fde3172d0436.png)
