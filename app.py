#  PROYECTO CONSOLIDACION STREAMLIT: FUNCION app.py

# Importaciones
import streamlit as st
import streamlit.components.v1 as stc
from eda_app import run_eda_app
from ml_app import run_ml_app

# st.set_page_config(
# 	page_title='Consolidation project: Streamlit',
# 	layout='wide',
# 	initial_sidebar_state='auto'
# )

# Función main()
def main():

	st.markdown(
		"""
		<div style='background-color: #3872FB; padding: 10px; border-radius: 5px;'>
		<h1 style='color: white; text-align: center'>App for the early detection of Diabetes Mellitus</h1>
		<h2 style='color: white; text-align: center'>DM</h2>
		</div>
		<div style='height: 20px;'></div>
		""",
		unsafe_allow_html=True
	)
	menu = st.sidebar.selectbox('Menu ', ['Home', 'EDA', 'ML', 'Info'], )

	if menu == 'Home':
		st.subheader('Home')
		st.markdown('### App for the early detection of Diabetes Mellitus')
		st.markdown('dataset contains signals and symptoms that might indicate diabetes mellitus')
		st.markdown('### Data source')
		st.markdown(
			"""
			<div style='background-color: #D3D3D3; padding: 10px; border-radius: 5px;'>
				<ul>
					<li style='color: black'><a href="https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dataset" target="_blank">Link</a></li>
				</ul>
			</div>
			<div style='height: 20px;'></div>
			""",
			unsafe_allow_html=True
		)
		st.markdown('### App content')
		st.markdown(
			"""
			<div style='background-color: #D3D3D3; padding: 10px; border-radius: 5px;'>
				<ul>
					<li style='color: black'>EDA section: Exploratory data analysis</li>
					<li style='color: black'>ML section: Diabetes prediction based on ML (Machine Learning)</li>
				</ul>
			</div>
			<div style='height: 20px;'></div>
			""",
			unsafe_allow_html=True
		)
	elif menu == 'EDA':
		run_eda_app()
	elif menu == 'ML':
		run_ml_app()
	else:
		st.subheader('Info')
		st.markdown('Consolidation project using Streamlit library')
		st.markdown('MBIT - Master in Data Engineering, Cloud & Big Data')
		st.markdown('* * *')
		st.markdown('###  A bit of info about diabetes mellitus')
		stc.iframe("https://www.diabetes.co.uk/", width=900, height=500, scrolling=True)

if __name__ == '__main__':
	main()