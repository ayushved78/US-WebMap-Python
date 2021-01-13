import folium
import pandas

df = pandas.read_csv("Volcanoes.txt")
lt = list(df["LAT"])
ln = list(df["LON"])
elev = list(df["ELEV"])
df
def color_prod(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

html = """<h4>Volcano information:</h4>
Height: %s m
"""

map = folium.Map(location=[20.5937, 78.9629], zoom_start=5, tiles="Stamen Terrain")
fg= folium.FeatureGroup(name="My_Map")

#method 1
# fg.add_child(folium.Marker(location=[23.033386167245535, 79.39027699069713],popup="Marker here",icon=folium.Icon(color='red')))
#method 2
# for cor in [[30.3165, 78.0322],[28.5355,77.3910],[11.9416,79.8083],[31.1048,77.1734]]:

#method 3
for lat,lon,el in zip(lt,ln,elev):
    fg.add_child(folium.CircleMarker(location=[lat,lon],popup=el,fill_color=color_prod(el),color='grey',fill_opacity=0.7,radius=6))
    iframe = folium.IFrame(html=html % str(el), width=200, height=100)
    #fg.add_child(folium.Marker(location=[lat,lon],popup=el,icon=folium.Icon(color='green')))
map.add_child(fg)


map.save("Maps.html")