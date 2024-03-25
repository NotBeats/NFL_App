import streamlit as st
import pandas as pd
import base64

st.title('NFL Team Advanced Passing Stats')

st.markdown("""
Simple webscraping of NFL player stats data.
* **Data Source:** [pro-football-reference.com](https://www.pro-football-reference.com/)
""")

st.sidebar.header('User Input Features')
year_selected = st.sidebar.selectbox('Year', list(reversed(range(1950,2024))))

# https://www.pro-football-reference.com/years/2022/receiving.htm
# webscraping of NFL player stats 
@st.cache
def load_yards_data(year):
    url = "https://www.pro-football-reference.com/years/" + str(year) + "/advanced.htm"
    html = pd.read_html(url, header=1)
    df = html[0]
    raw = df.drop(df[df.Yds == 'Yds'].index) # deletes repeating headers in content
    raw = raw.fillna(0)
    teamstats = raw.drop(['G'], axis=1)
    return teamstats
teamstats = load_yards_data(year_selected)

# team selection
sorted_teams = sorted(teamstats.Tm.unique())
team_selected = st.sidebar.multiselect('Team', sorted_teams, sorted_teams)

# filtering data
df_team_selected = teamstats[(teamstats.Tm.isin(team_selected))]

st.header('Yards Stats of Selected Team(s)')
st.write('Data Dimension: ' + str(df_team_selected.shape[0]) + ' rows and ' + str(df_team_selected.shape[1]) + ' columns')
st.dataframe(df_team_selected)

# download the data as a csv file
def file_download(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="teamstats.csv">Download Yards CSV File</a>'
    return href

st.markdown(file_download(df_team_selected), unsafe_allow_html=True)

@st.cache
def load_acc_data(year):
    url = "https://www.pro-football-reference.com/years/" + str(year) + "/advanced.htm"
    html = pd.read_html(url, header=1)
    df = html[1]
    raw = df.drop(df[df.Yds == 'Yds'].index) # deletes repeating headers in content
    raw = raw.fillna(0)
    teamstats = raw.drop(['G'], axis=1)
    return teamstats
teamstats = load_acc_data(year_selected)

# team selection
sorted_teams = sorted(teamstats.Tm.unique())

# filtering data
df_team_selected = teamstats[(teamstats.Tm.isin(team_selected))]

st.header('Accuracy Stats of Selected Team(s)')
st.dataframe(df_team_selected)

# download the data as a csv file
def file_download(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="teamstats.csv">Download Accuracy CSV File</a>'
    return href

st.markdown(file_download(df_team_selected), unsafe_allow_html=True)

@st.cache
def load_press_data(year):
    url = "https://www.pro-football-reference.com/years/" + str(year) + "/advanced.htm"
    html = pd.read_html(url, header=1)
    df = html[2]
    raw = df.drop(df[df.Yds == 'Yds'].index) # deletes repeating headers in content
    raw = raw.fillna(0)
    teamstats = raw.drop(['G'], axis=1)
    return teamstats
teamstats = load_press_data(year_selected)

# team selection
sorted_teams = sorted(teamstats.Tm.unique())

# filtering data
df_team_selected = teamstats[(teamstats.Tm.isin(team_selected))]

st.header('Pressure Stats of Selected Team(s)')
st.dataframe(df_team_selected)

# download the data as a csv file
def file_download(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="teamstats.csv">Download Pressure CSV File</a>'
    return href

st.markdown(file_download(df_team_selected), unsafe_allow_html=True)

@st.cache
def load_type_data(year):
    url = "https://www.pro-football-reference.com/years/" + str(year) + "/advanced.htm"
    html = pd.read_html(url, header=1)
    df = html[3]
    raw = df.drop(df[df.Yds == 'Yds'].index) # deletes repeating headers in content
    raw = raw.fillna(0)
    teamstats = raw.drop(['G'], axis=1)
    return teamstats
teamstats = load_type_data(year_selected)

# team selection
sorted_teams = sorted(teamstats.Tm.unique())

# filtering data
df_team_selected = teamstats[(teamstats.Tm.isin(team_selected))]

st.header('Play Type Stats of Selected Team(s)')
st.dataframe(df_team_selected)

# download the data as a csv file
def file_download(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="teamstats.csv">Download Play Type CSV File</a>'
    return href

st.markdown(file_download(df_team_selected), unsafe_allow_html=True)