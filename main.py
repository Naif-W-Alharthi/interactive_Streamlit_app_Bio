import streamlit as st
import plotly.express as px
import pandas as pd
import altair as alt
import plotly.graph_objects as go
import numpy as np
# Load Excel file

def make_gauge(percent, input_text, input_color, width=200, height=150):
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = percent,
        title = {'text': input_text},
        gauge = {
            'axis': {'range': [None, 100]},
            'bar': {'color': input_color},
        }
    ))

    # Set the width and height of the figure
    fig.update_layout(width=width, height=height)

    return fig
st.set_page_config(
    page_title="dashboard for Biodiversity",
    page_icon="🌎",
    layout="wide",
    initial_sidebar_state="expanded"
)
col1, col3= st.columns((1,1))
alt.themes.enable("dark")
excel_file_path = "4Lenses copy.xlsx"
df = pd.read_excel(excel_file_path)

excel_file_path = "2_Clean wheat-yields.csv"
df_wheat = pd.read_csv(excel_file_path)
excel_file_path = "2_Clean Tree Cover Loss.csv"
df_tree = pd.read_csv(excel_file_path)
excel_file_path = "2_Clean global-living-planet-index.csv"
df_living = pd.read_csv(excel_file_path)
excel_file_path = "2_Clean deforestation-co2-trade-by-product.csv"
df_defor = pd.read_csv(excel_file_path)

st.markdown(
    """
<style>
[data-testid="stMetricValue"] {
    font-size: 50px !important;
}

[data-testid="stMetricDelta"] {
    font-size: 30px !important;
}

[data-testid="stMarkdownContainer"] {
    font-size: 500px !important;
}

 .stMetric { text-align: center; display: flex; align-items: center; justify-content: center; }
</style>
""",
    unsafe_allow_html=True,
)




with st.sidebar:
    st.title('🌎 Biodiversity Dashboard')
    year_list = list(df.year.unique())[::-1]
    year_list=year_list[1::]
    selected_year = st.selectbox('Select a year', year_list)
    df_selected_year = df[df.year == selected_year ]
    df_living_list= list(df_living.Country.unique())
    selected_country = st.selectbox('Select a country', df_living_list)
    df_selected_country = df_living[df_living.Country == selected_country ]
    df_defor_list = list(df_defor.Country.unique())
    selected_country_defor = st.selectbox('Select a country for radar', df_defor_list)
    df_defor_selected = df_defor[df_defor.Country == selected_country_defor]
    

forest_area_percent = float(df_selected_year['Forest area %'].iloc[0])
bio_diversity_score = float(df_selected_year['Biodiversity score'].iloc[0])
Agri = float(df_selected_year['Agricultral land %'].iloc[0])
wheat_yeild = float(df_selected_year['wheat yeild'].iloc[0])


input_text = "Forest Area"
input_color = "green"
gauge_width = 300
gauge_height = 300

gauge_chart = make_gauge(forest_area_percent, input_text, "orange", width=gauge_width, height=gauge_height)
gauge_chart2 = make_gauge(bio_diversity_score, "Bio score", input_color, width=gauge_width, height=gauge_height)
gauge_chart3 = make_gauge(Agri, "Agriculture", "blue", width=gauge_width, height=gauge_height)
gauge_chart4 = make_gauge(wheat_yeild, "Wheat yield", "yellow", width=gauge_width, height=gauge_height)

with col1:
   line_chart = px.line(df_selected_country, x='Year', y='Living Planet Index', title='line Chart of Living plannet index for '+selected_country)
   st.plotly_chart(line_chart)
   st.write(gauge_chart)
   st.write(gauge_chart2)

    

with col3:
    if selected_year != 2001.0:
        lastyear_percent = float(df[df.year == selected_year-1]['Forest area %'].iloc[0])
    else:
        lastyear_percent = bio_diversity_score
    st.metric(label="Global Biodiversity score", value=round(bio_diversity_score), delta=round(bio_diversity_score)-round(lastyear_percent))
    df_pivot = df_defor_selected.pivot_table(index='Country', columns='Products', values='CO2 (in Tonnes)').reset_index()
    df_melted = pd.melt(df_pivot, id_vars=["Country"], var_name="Products", value_name="CO2 (in Tonnes)")
    df_melted['Sqrt_CO2'] = df_melted['CO2 (in Tonnes)'] ** 0.5
    fig = px.line_polar(df_melted, r='Sqrt_CO2', theta='Products', line_close=True)
    st.plotly_chart(fig)
    st.write(gauge_chart3)
    st.write(gauge_chart4)

