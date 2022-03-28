import streamlit as st
import pandas as pd



st.write("""
### ¡Hola! Bienvenido (a) a  *Nombre de la app*
"Esta app te permitirá conocer algunos síntomas relacionados a alguna enfermedad de transmisión sexual
""")

st.write("Here's our first attemp at using data to create a table:")
st.write(pd.DataFrame({
	'first column': [1, 2, 3, 4],
	'second column': [10, 20, 30, 40]
	}))



df=pd.DataFrame({
	'first column': [1, 2, 3, 4],
	'second column': [10, 20, 30, 40]
	})

option=st.selectbox(
	'Which number do you like best?',
	df ['first column']
	

# https://discuss.streamlit.io/t/discourse-component/8061

discourse_url = "Foro de discusión"
topic_id = 8061

st_discourse(discourse_url, topic_id)
