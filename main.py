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
alt.themes.enable("dark")
excel_file_path = "4Lenses copy.xlsx"
df = pd.read_excel(excel_file_path)



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
    # df_selected_year= df_selected_year[:-1]
    
forest_area_percent = float(df_selected_year['Forest area %'].iloc[0])

print(forest_area_percent)

input_text = "Forest Area"
input_color = "green"
gauge_chart = make_gauge(forest_area_percent, input_text, input_color)
st.plotly_chart(gauge_chart, use_container_width=True)
# line_chart = px.line(df, x='year', y='Forest area %', title='line Chart of Wheat Yield by Year')

# st.write(line_chart)


# st.plotly_chart(line_chart)
# with interactive: