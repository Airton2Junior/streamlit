import streamlit as st
import pandas as pd

st.write("#Aqui temos Widgets:")

st.write("##Sliders:")
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

st.write("##Input:")
st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name

st.write("##Checkbox:")
agree = st.checkbox('I agree')  # 👈 this is a widget

# Use the value of the widget
if agree:
    st.write('Great!')
else:    
    st.write('Not great!')

st.write("##Selectbox:")
option = st.selectbox(
    'Which number do you like best?',
     [1, 2, 3]) # 👈 this is a widget

'You selected:', option

st.write("##Multiselect:")
options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red']) # 👈 this is a widget

'You selected:', options

st.write("##File Uploader:")
uploaded_file = st.file_uploader("Choose a CSV file")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data)
    
st.write("##Color Picker:")
color = st.color_picker('Pick A Color', '#00f900') # 👈 this is a widget
st.write('The current color is', color)

st.write("##Date Input:")
import datetime
d = st.date_input(
    "When's your birthday",
    datetime.date(2019, 7, 6)) # 👈 this is a widget
st.write('Your birthday is:', d)

st.write("##Time Input:")
t = st.time_input('Set an alarm for', datetime.time(8, 45)) # 👈 this is a widget
st.write('Alarm is set for:', t)

st.write("##Number Input:")
number = st.number_input('Insert a number') # 👈 this is a widget
st.write('The current number is ', number)

st.write("##Text Area:")
txt = st.text_area('Text to analyze', '''
    It was the best of times, it was the worst of times, it was
    the age of wisdom, it was the age of foolishness, it was the
    epoch of belief, it was the epoch of incredulity, it was the
    season of Light, it was the season of Darkness, it was the
    spring of hope, it was the winter of despair, (...)
    ''') # 👈 this is a widget
st.write('Sentiment:', txt)

st.write("##Progress Bar:")
import time
my_bar = st.progress(0) # 👈 this is a widget
for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1)
    
st.write("##Spinner:")
with st.spinner('Wait for it...'):
    time.sleep(5)
st.success('Done!')

st.write("##Balloon:")
st.balloons()

st.write("##Error:")
st.error('This is an error')

st.write("##Warning:")
st.warning('This is a warning')

st.write("##Info:")
st.info('This is a purely informational message')

st.write("##Success:")
st.success('This is a success message!')

st.write("##Exception:")
e = RuntimeError('This is an exception of type RuntimeError')
st.exception(e)

st.write("##Code:")
st.code("print('Hello, World!')")

st.write("##JSON:")
st.json({
    "name": "John Doe",
    "age": 29,
    "city": "New York"
})

st.write("##Markdown:")
st.markdown("## Hello, World!")
st.markdown("### Hello, World!")
st.markdown("#### Hello, World!")
st.markdown("##### Hello, World!")
st.markdown("###### Hello, World!")
st.markdown("Hello, World!")

st.write("##Latex:")
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

st.write("##Title:")
st.title("Hello, World!")

st.write("##Header:")
st.header("Hello, World!")

st.write("##Subheader:")
st.subheader("Hello, World!")

st.write("##Write:")
st.write("Hello, World!")

st.write("##Sidebar:")
st.sidebar.write("Hello, World!")
st.sidebar.write("##Title:")
st.sidebar.title("Hello, World!")
st.sidebar.write("##Header:")
st.sidebar.header("Hello, World!")
st.sidebar.write("##Subheader:")
st.sidebar.subheader("Hello, World!")
st.sidebar.write("##Write:")
st.sidebar.write("Hello, World!")

st.write("##Columns:")
col1, col2 = st.columns(2)
col1.write("Hello, World!")
col2.write("Hello, World!")
col1, col2, col3 = st.columns([1, 2, 1])
col1.write("Hello, World!")
col2.write("Hello, World!")
col3.write("Hello, World!")

st.write("##Expander:")
with st.expander("Hello, World!"):
    st.write("Hello, World!")