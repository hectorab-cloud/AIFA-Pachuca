import dash
from dash import html
import geopandas as gpd
import folium
from dash import dcc, html
import folium
from branca.element import Figure
import os 
print(os.listdir())

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Dashboard con Mapa"),
    html.Iframe(id="map", srcDoc=open("E:\\Laborales\\SEGOB\\AIFA-Pachuca\\Productos\\Dashboard\\mapa_le.html", "r").read(), width="100%", height="500px")
])

if __name__ == '__main__':
    app.run(debug=True)
