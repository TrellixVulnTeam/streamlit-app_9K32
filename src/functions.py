import streamlit as st
import pandas as pd
import numpy as np
import time

df = pd.DataFrame(
    np.random.randn(10, 3), 
    columns=(['a', 'b', 'c'])
)


st.dataframe(df.style.highlight_max(axis=1))

st.line_chart(df)

# Map
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns = ['lat', 'lon']
)

st.map(map_data)

x = st.slider('x') # this is a widget

st.write(x, ' squared is', x * x)

#Save state of the widget onto a variable
st.text_input("Your name", key="name")

st.session_state.name

# Checkbox
if st.checkbox("Show dataframe"):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c']
    )
    
    chart_data


# selectbox for options
option = st.selectbox(
    'Which number do you like best?', 
    df['a']
)

'You selected ', option


# sidebar
# selectbox on the sidebar
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)


# columns to place widgets side-by-side
left_column, right_column = st.columns(2)

left_column.button('Press me!')

with right_column:
    chosen = st.radio(
        'Sorting hat',
        ('Gryffindor', 'Ravenclaw', 'Hufflepuff', 'Slytherin')
    )
    
    st.write(f"You are in {chosen} house!")

st.spinner('Test')


# Progress bar
# must import time
'Starting a long computation'

# placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    # Update the progress bar with each iteration
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)
    
'... and now we\'re done'


# Caching
# Mark a function with @st.cache