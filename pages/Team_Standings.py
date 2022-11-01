import streamlit as st
import pandas as pd
import base64

st.title('NFL Team Standings')

st.markdown("""
Simple webscraping of NFL player stats data.
* **Data Source:** [pro-football-reference.com](https://www.pro-football-reference.com/)
""")

st.sidebar.header('User Input Features')
year_selected = st.sidebar.selectbox('Year', list(reversed(range(1950,2023))))

# https://www.pro-football-reference.com/years/2022/receiving.htm
# webscraping of NFL player stats 
@st.cache
def load_afc_data(year):
    url = "https://www.pro-football-reference.com/years/" + str(year)
    html = pd.read_html(url, header=0)
    df = html[0]
    raw = df.drop(df[df.W == 'W'].index) # deletes repeating headers in content
    raw = raw.fillna(0)
    teamstats = raw.drop(['SRS'], axis=1)
    return teamstats
teamstats = load_afc_data(year_selected)

st.header('AFC Team Standings')
st.dataframe(teamstats)

# download the data as a csv file
def file_download(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="teamstats.csv">Download AFC CSV File</a>'
    return href

st.markdown(file_download(teamstats), unsafe_allow_html=True)

@st.cache
def load_nfc_data(year):
    url = "https://www.pro-football-reference.com/years/" + str(year)
    html = pd.read_html(url, header=0)
    df = html[1]
    raw = df.drop(df[df.W == 'W'].index) # deletes repeating headers in content
    raw = raw.fillna(0)
    teamstats = raw.drop(['SRS'], axis=1)
    return teamstats
teamstats = load_nfc_data(year_selected)

st.header('NFC Team Standings')
st.dataframe(teamstats)

# download the data as a csv file
def file_download(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="teamstats.csv">Download NFC CSV File</a>'
    return href

st.markdown(file_download(teamstats), unsafe_allow_html=True)