from sqlalchemy import create_engine
import pandas as pd
import psycopg2
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import plotly.express as px
import altair as alt
import requests
import folium
from config import username, password, hostname, port, db

from flask_cors import CORS
from flask import Flask, render_template, redirect, request, url_for, jsonify

app = Flask(__name__)
CORS(app)

# Set up database connection
engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{hostname}:{port}/{db}')


@app.route("/")
def home():
   return render_template("home.html")

import psycopg2

conn = psycopg2.connect(dbname="project3",user="postgres",password="DataRocks123!",host="localhost",port="5432")
cur = conn.cursor()



@app.route("/chart1")
def povertydeath():
  #url= 'http://127.0.0.1:5000/api/v1.0/cancer'
  #r = requests.get(url)
  #json = r.json()
  cur.execute("SELECT povertypercent,mortality_rate FROM cancer")
  rows = cur.fetchall()
  df = pd.DataFrame(rows, columns=['povertypercent','mortality_rate'])
  #df = df1[['povertypercent','mortality_rate']]
  df = df.dropna()
  df.sort_values(by="povertypercent", ascending = True, inplace=True)
  values = df.mortality_rate.tolist()
  labels= df.povertypercent.tolist()
  return render_template("mortalitypoverty.html", labels=labels, values=values)



# Define route for map
@app.route('/chart2')
def cancerimapus():
    # Retrieve data from the database
    cur.execute("SELECT * FROM cancer_per_state where state_id not in ('KS','MN')")
    rows = cur.fetchall()
    df = pd.DataFrame(rows, columns=['index', 'state_id', 'state_cancer_incidence_rate','state_mortality_rate', 'state_target_deathrate'])
    df2=df[['state_id', 'state_cancer_incidence_rate']]
    print(df2)

    # Create the Leaflet map
    us_map = folium.Map(location=[39.50, -98.35], zoom_start=4)
    folium.Choropleth(
        geo_data='https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/us-states.json',
        name='choropleth',
        data=df2,
        columns=['state_id','state_cancer_incidence_rate'],
        key_on='feature.id',
        fill_color='YlOrRd',
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name='Cancer Incidence Rate'
    ).add_to(us_map)
    #return us_map.to_json()
    return us_map._repr_html_()


@app.route("/chart4")
def cancer_population():
  cur.execute("SELECT incidencerate, popest2015 FROM cancer")
  rows = cur.fetchall()
  df = pd.DataFrame(rows, columns=['incidencerate','popest2015'])
  df = df.dropna()
  df.sort_values(by="popest2015", ascending = True, inplace=True)
  values = df.incidencerate.tolist()
  labels= df.popest2015.tolist()
  print (values)
  print (labels)
  return render_template("cancerrate_pop.html", labels=labels, values=values)


# Define route for scatterplot
@app.route("/chart6")
def cancerstaterates():
  cur.execute("SELECT state_id, state_cancer_incidence_rate,    state_mortality_rate,   state_target_deathrate from  cancer_per_state where state_id not in ('KS','MN')")
  rows = cur.fetchall()
  df = pd.DataFrame(rows, columns=['state_id','state_cancer_incidence_rate','state_mortality_rate','state_target_deathrate'])
#   df = df.dropna()
#   df.sort_values(by="popest2015", ascending = True, inplace=True)
  state_cancer_incidence_rates = df.state_cancer_incidence_rate.tolist()
  state_mortality_rates = df.state_mortality_rate.tolist()
  state_target_deathrates =  df.state_target_deathrate.tolist()

  labels= df.state_id.tolist()
  values={
    "state_cancer_incidence_rates":state_cancer_incidence_rates,
    "state_mortality_rates":state_mortality_rates,
    "state_target_deathrates":state_target_deathrates
    }
#   print (values)
  print (labels)
  return render_template("cancer_scatterplot.html", labels=labels,values=values)



@app.route("/chart5")
def cancerdeath():
    conn = engine.connect()
    query = "SELECT * FROM cancer"
    cancer = pd.read_sql(query, conn)
    #return cancer.to_json(orient="records")
    items_to_drop = ["index","target_deathrate", "medianage", "medianagemale", "medianagefemale","pctnohs18_24", "pcths18_24", "pctwhite", "pctblack", "pctasian", "pctotherrace", "race_undef", "pctmarriedhouseholds","birthrate", "countyfips", "lat", "lng", "mortality_rate", "pcths25_over", "incidencerate"]
    deathratecorrelation = cancer.corr()["target_deathrate"].drop(index = items_to_drop)
    #deathratecorrelation
    fig = px.line_polar(deathratecorrelation, r='target_deathrate', theta=deathratecorrelation.index, line_close=True)
    fig.update_traces(fill='toself')
    #return fig.show()
    return render_template('social_death_radar.html', plot=fig.to_html())


#keep at the end of the file
if __name__ == '__main__':
    app.run(debug=True)


#Upcoming charts - coding in progress

# Define route for A choropleth map - Leaflet - Chart 3
#@app.route('/chart3')
#def tergetdeathmap():
#    # Retrieve data from the database
#    cur.execute("SELECT * FROM cancer_per_state")
#    rows = cur.fetchall()
#    df = pd.DataFrame(rows, columns=['index', 'state_id', 'state_target_deathrate'])
#    df2=df[['state_id', 'state_target_deathrate']]
#    print(df2)
#
#    # Create the Leaflet map
#    us_map = folium.Map(location=[39.50, -98.35], zoom_start=4)
#    folium.Choropleth(
#        geo_data='https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/us-states.json',
#        name='choropleth',
#        data=df2,
#        columns=['state_id','state_target_deathrate'],
#        key_on='feature.id',
#        fill_color='PuRd',
#        fill_opacity=0.7,
#        line_opacity=0.2,
#        legend_name='Target Death Rate for Cancer - US (2015)'
#    ).add_to(us_map)
#    #return us_map.to_json()
#    return us_map._repr_html_()


# Define route for A choropleth map - PLotly Express - Chart 3

#import plotly.express as px
#import pandas as pd
#from flask import Flask, render_template
#
#app = Flask(__name__)
#
# Define route for chart
#@app.route('/chart3')
#def targetdeathmap():
#    # Retrieve data from the database
#    cur.execute("SELECT * FROM cancer")
#    rows = cur.fetchall()
#    df = pd.DataFrame(rows, columns=['state_id','county', 'target_deathrate'])
#
#    # Create the choropleth map using plotly express
#    fig = px.choropleth(df, locations='state_id', color='target_deathrate', locationmode='USA-states', scope='usa')
#
#    # Render the figure as HTML and pass it to the template for display
#    return render_template('targetdeathrateus.html', plot=fig.to_html())
#
#fig = px.choropleth(cancer, locations = "state_id", color = "target_deathrate", locationmode = "USA-states", scope = "usa")
#fig.show()



# Define route for A choropleth map - PLotly Express - Chart 7
#
#from urllib.request import urlopen
#import json
#import requests
#import pandas as pd
#with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
#counties = json.load(response)
#url= 'http://127.0.0.1:5000/api/v1.0/cancer'
#r = requests.get(url)
#json = r.json()
#df = pd.DataFrame(json)
#df = df[df['mortality_rate'].notna()]
#df = df[df['countyfips'].notna()]
#import plotly.express as px
#fig = px.choropleth(df, geojson = counties, locations='countyfips', color='mortality_rate',
#color_continuous_scale="blues",
#range_color=(48, 513),
#scope="usa",
#)
#fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


