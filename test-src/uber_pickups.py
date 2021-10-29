import streamlit as st
import numpy as np
import pandas as pd

st.title('Uber pickups in NYC')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

# Downloads some data, puts it in Pandas dataframe, 
# and converts the date column from text to datetime
@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows = nrows)
    lowercase = lambda x : str(x).lower()
    data.rename(lowercase, axis='columns', inplace = True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# Text element to inform user data is loading
data_load_state = st.text('Loading data...')

# Load 10000 rows of data into dataframe
data = load_data(10000)

# Notify user that data has successfully loaded
data_load_state.text('Data loaded! (using st.cache)')

# Raw data section
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

# Histogram section
st.subheader('Number of pickups by hour')
hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0, 24)
)[0]

st.bar_chart(hist_values)

# Plot data on map
if st.checkbox('Show map of all pickups'):
    st.subheader('Map of all pickups')
    st.map(data)

# Filter data and map
hour_to_filter = st.slider('Select hour to filter', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)

