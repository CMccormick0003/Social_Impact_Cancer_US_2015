create table state_rates(
	index                          INT,
	target_deathrate               float,
	popest2015                     float,
	geography                      varchar,
	avg_cancer_incd_rate           float,
	mortality_rate                 float,
	county                         varchar,
	county_full                    varchar,
	countyfips                     float,
	state_id                       varchar,
	lat                            float,
	lng                            float,
	state_cancer_incidence_rate    float,
	state_mortality_rate           float,
	state_target_deathrate         float
	)
	
	select * from state_rates;