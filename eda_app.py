# PROYECTO DE CONSOLIDACION STREAMLIT: FUNCION eda_app.py

# Importaciones: streamlit, pandas, matplotlib, seaborn
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Función principal que emplearemos en la APP
def run_eda_app():

	st.title('Exploratory Data Analysis')
	
	submenu = st.sidebar.selectbox('Submenu', ['Descriptive', 'Visual'])
	df = pd.read_csv('data/diabetes_data_upload.csv')
	df_clean = pd.read_csv('data/diabetes_data_upload_clean.csv')
	df_freq_dist_age = pd.read_csv('data/freqdist_of_age_data.csv')
	gender_distribution = df['Gender'].value_counts()
	class_distribution = df['class'].value_counts()

	if submenu == 'Descriptive':
		# original data
		st.subheader('Descriptive analysis')
		st.dataframe(df)

		# data types
		with st.expander('Data types'):
			st.dataframe(df.dtypes)
		
		# descriptive summary
		with st.expander('Descriptive summary'):
			st.dataframe(df_clean.describe())

		# gender distribution
		with st.expander('Gender distribution'):
			st.dataframe(gender_distribution)

		# Class distribution
		with st.expander('Class distribution'):
			st.dataframe(class_distribution)

	elif submenu == 'Visual':
		# original data
		st.subheader('Visual analysis')
		two_thirds, one_third = st.columns([2,1])
		with two_thirds:
			with st.expander('Graphs of gender distribution'):
				fig, ax = plt.subplots()
				sns.countplot(
					data=df, 
					x='Gender',
					orient='v',
					palette='Set2',
					ax=ax)
				st.pyplot(fig)
			with st.expander('Graphs of class distribution'):
				fig, ax = plt.subplots()
				sns.countplot(
					data=df, 
					x='class',
					orient='v',
					palette='Set2',
					ax=ax)
				st.pyplot(fig)
		with one_third:
			with st.expander('Gender distribution'):
				st.dataframe(gender_distribution)
			with st.expander('Class distribution'):
				st.dataframe(class_distribution)
		with st.expander('Frequency distribution plot per age'):
			fig, ax = plt.subplots()
			sns.barplot(
				data=df_freq_dist_age, 
				x='Age', 
				y='count',
				hue='Age',
				palette='Set2', 
				ax=ax)
			plt.xticks(rotation=45)
			st.pyplot(fig)
		with st.expander('Outlier detection plot'):
			fig, ax = plt.subplots()
			sns.boxplot(
				data=df, 
				x='Gender', 
				y='Age',
				hue='Gender', 
				palette='Set2',
				ax=ax)
			st.pyplot(fig)
		with st.expander('Correlation matrix'):
			fig, ax = plt.subplots()
			sns.heatmap(
				df_clean.corr(), 
				annot=True, 
				fmt='.2f', 
				annot_kws={"size": 6}, 
				cbar_kws={"shrink": 1, 'aspect': 30, 'pad': 0.02, 'label': 'Correlation coefficient'},
				ax=ax)
			ax.tick_params(axis='both', which='major', labelsize=6)
			st.pyplot(fig)



# Fin de la FUNCION







