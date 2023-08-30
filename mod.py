import streamlit as st
import numpy as np
import pandas as pd

st.write("bemvinda")

dataframe = np.random.randn(10,20)
st.dataframe(dataframe)

dataframe = pd.DataFrame(
    np.random.radn(10,20),
    columns=("col %d" % i for i in range (20)))

st.dataframe(dataframe.style.highlight_max(axis=0))

dataframe = pd.DataFrame(
    np.random.radn(10,20),
    columns=("col %d" % i for i in range (20)))

st.table(dataframe)

x= st.slider("x")
st.write(x,"numero do quadrado de ", x*x)

st.subheader('Map of all pickups')

st.map(data)

st.subheader('Map of all pickups')
st.map(data)

hour_to_filter = 17
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)

hour_to_filter = st.slider('hour', 0, 23, 17)  # min: 0h, max: 23h, default: 17h



st.title('Uber pickups in NYC')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache_data)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Number of pickups by hour')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# Some number in the range 0-23
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)


df = pd.DataFrame({
    "col1": np.random.randn(1000) / 50 + 37.76,
    "col2": np.random.randn(1000) / 50 + -122.4,
    "col3": np.random.randn(1000) * 100,
    "col4": np.random.rand(1000, 4).tolist(),
})

st.map(df,
    latitude='col1',
    longitude='col2',
    size='col3',
    color='col4')



chart_data = pd.DataFrame({
    'col1' : np.random.randn(20),
    'col2' : np.random.randn(20),
    'col3' : np.random.choice(['A','B','C'],20)
})

st.bar_chart(
    chart_data,
    x='col1',
    y='col2',
    color='col3'
)




if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def click_button():
    st.session_state.clicked = True

st.button('Click me', on_click=click_button)

if st.session_state.clicked:
    # The message and nested widget will remain on the page
    st.write('Button clicked!')
    st.slider('Select a value')



with st.echo():
    st.title("CAT")

    st.markdown("[![Click me](app/static/cat.png)](https://streamlit.io)")