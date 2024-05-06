import streamlit as st
import plotly.express as px
import pandas as pd
import altair as alt
import plotly.graph_objects as go
# Load Excel file

def make_gauge(percent, input_text, input_color):
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = percent,
        title = {'text': input_text},
        gauge = {
            'axis': {'range': [None, 100]},
            'bar': {'color': input_color},
            
            }))

    return fig
st.set_page_config(
    page_title="dashboard for Biodiversity",
    page_icon="🌎",
    layout="wide",
    initial_sidebar_state="expanded"
)
col1, col2, col3= st.columns((1,1,3))
alt.themes.enable("dark")
excel_file_path = "4Lenses copy.xlsx"
df = pd.read_excel(excel_file_path)


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
</style>
""",
    unsafe_allow_html=True,
)
# st.write(df)


st.title("Main Page")
st.write("""
My first app
Hello *world!*
""")




with st.sidebar:
    st.title('🌎 Biodiversity Dashboard')
    year_list = list(df.year.unique())[::-1]
    year_list=year_list[1::]
    print(year_list,"year list")
    selected_year = st.selectbox('Select a year', year_list)
    
    df_selected_year = df[df.year == selected_year ]
    
# add all later
forest_area_percent = float(df_selected_year['Forest area %'].iloc[0])
bio_diversity_score = float(df_selected_year['Biodiversity score'].iloc[0])
forest_area_percent = float(df_selected_year['Forest area %'].iloc[0])
print(forest_area_percent)

input_text = "Forest Area"
input_color = "green"

gauge_chart = make_gauge(forest_area_percent, input_text, input_color)
gauge_chart2 = make_gauge(bio_diversity_score, "Bio score", input_color)
# with col1:
#     st.plotly_chart(gauge_chart, use_container_width=True)

# with col2:
#     st.plotly_chart(gauge_chart, use_container_width=True)

with col3:
    if selected_year != 2001.0:
    
 
        lastyear_percent = float(df[df.year == selected_year-1]['Forest area %'].iloc[0])
       

    st.metric(label="Biodiversity score", value=round(bio_diversity_score), delta=round(bio_diversity_score)-round(lastyear_percent))

if selected_year != 2020.0:
    # df_after = df[df.year == selected_year+1 ]
    
    next_year_percent = float(df[df.year == selected_year+1]['Forest area %'].iloc[0])
    st.subheader(f"Forest area percentage ({selected_year+1}): {next_year_percent}")



# Tree cover for country over time? 8/10
# add radar chart for the given country and the loses

# Displaying forest area percentage for previous year


line_chart = px.line(df, x='year', y='Forest area %', title='line Chart of Wheat Yield by Year')

# st.write(line_chart)


st.plotly_chart(line_chart)
# with interactive: