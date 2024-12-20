import folium
import pandas as pd
import json

geo_json = 'https://raw.githubusercontent.com/southkorea/seoul-maps/master/kostat/2013/json/seoul_municipalities_geo_simple.json'
file_path = 'C:\pythonDev\lean\data\자치구별+총인구(추계인구)_20241220092033.csv'
datas = pd.read_csv(file_path,usecols=['자치구별(2)','2022'])

seoul_counts = datas[['자치구별(2)','2022']]
seoul_counts.columns = ['name','values']
seoul_counts = seoul_counts.sort_values(by = 'name')

m = folium.Map(
    location = [37.5502,126.982],
    tiles = 'CartoDB positron',  # 타일 변경
    #attr = 'Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under ODbL',
    zoom_start = 11.2
)

folium.Choropleth(
    geo_data = geo_json,
    name = 'choropleth',
    data = seoul_counts,
    columns =['name','values'],
    key_on = 'feature.properties.name',
    hightlight = True,
    fill_color = 'PuRd',
    fill_opacity = 0.5,
    line_opacity =1
).add_to(m)

m.save('m.html')