#  PROYECTO CONSOLIDACION STREAMLIT: FUNCION app.py

# Importaciones
import streamlit as st
import streamlit.components.v1 as stc
from eda_app import run_eda_app
from ml_app import run_ml_app

st.set_page_config(
	page_title='Consolidation project: Streamlit',
	layout='wide',
	initial_sidebar_state='auto'
)

# Función main()
def main():

	st.title('App for the early detection of Diabetes Mellitus')
	menu = st.sidebar.selectbox('Menu ', ['Home', 'EDA', 'ML', 'Info'], )

	if menu == 'Home':
		st.subheader('Home')
		st.markdown('### App for the early detection of Diabetes Mellitus')
		st.markdown('dataset ...')
		st.markdown('### Data source')
		st.markdown('link ...')
		st.markdown('### App content')
		st.markdown('EDA section')
		st.markdown('ML section')
	elif menu == 'EDA':
		run_eda_app()
	elif menu == 'ML':
		run_ml_app()
	else:
		st.markdown('Info ...')

if __name__ == '__main__':
	main()