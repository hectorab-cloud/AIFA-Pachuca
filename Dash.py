import streamlit as st

import pandas as pd
import numpy as np
import plotly.express as px
import altair as alt
import pydeck as pdk

# Set page title
st.set_page_config(page_title="Multi-Visualization Dashboard", layout="wide")

# Load sample data
@st.cache_data
def load_data():
    df = pd.DataFrame({
        'date': pd.date_range(start='2023-01-01', periods=100),
        'value': np.random.randn(100).cumsum(),
        'category': np.random.choice(['A', 'B', 'C'], 100),
        'lat': np.random.uniform(30, 50, 100),
        'lon': np.random.uniform(-120, -70, 100),
    })
    return df

df = load_data()

st.title("Multi-Visualization Dashboard")

# 1. Line Chart
st.header("1. Line Chart")
st.line_chart(df.set_index('date')['value'])

# 2. Bar Chart
st.header("2. Bar Chart")
chart = alt.Chart(df).mark_bar().encode(
    x='category',
    y='value',
    color='category'
).interactive()
st.altair_chart(chart, use_container_width=True)

# 3. Scatter Plot
st.header("3. Scatter Plot")
fig = px.scatter(df, x='date', y='value', color='category')
st.plotly_chart(fig)

# 4. Heatmap
st.header("4. Heatmap")
pivot = df.pivot(index='date', columns='category', values='value')
fig = px.imshow(pivot)
st.plotly_chart(fig)

# 5. 3D Scatter Plot
st.header("5. 3D Scatter Plot")
fig = px.scatter_3d(df, x='date', y='value', z='category', color='value')
st.plotly_chart(fig)

# 6. Pie Chart
st.header("6. Pie Chart")
fig = px.pie(df, values='value', names='category')
st.plotly_chart(fig)

# 7. Map with Scatter Plot
st.header("7. Map with Scatter Plot")
fig = px.scatter_mapbox(df, lat='lat', lon='lon', color='value', size='value',
                        color_continuous_scale=px.colors.cyclical.IceFire,
                        mapbox_style="carto-positron", zoom=3)
st.plotly_chart(fig)

# 8. 3D Map
st.header("8. 3D Map")
layer = pdk.Layer(
    "HexagonLayer",
    df,
    get_position=['lon', 'lat'],
    auto_highlight=True,
    elevation_scale=50,
    pickable=True,
    elevation_range=[0, 3000],
    extruded=True,
    coverage=1,
)

view_state = pdk.ViewState(
    latitude=df['lat'].mean(),
    longitude=df['lon'].mean(),
    zoom=4,
    pitch=50,
)

r = pdk.Deck(layers=[layer], initial_view_state=view_state)
st.pydeck_chart(r)

