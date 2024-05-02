import streamlit as st
import plotly.express as px
import pandas as pd

# Load Excel file
excel_file_path = "4Lenses.xlsx"
df = pd.read_excel(excel_file_path)

for col in df.columns: ## Testing for how cols are named
    print(col)

st.write(df)


st.title("Main Page")
st.write("""
My first app
Hello *world!*
""")


bar_chart = px.bar(df, x='Unnamed: 1', y='Unnamed: 2', title='Bar Chart of Wheat Yield by Year')


st.write(bar_chart)


st.plotly_chart(bar_chart)
