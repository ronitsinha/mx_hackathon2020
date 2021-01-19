import requests
import pprint
import webbrowser
import streamlit as st

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.graphics.mosaicplot import mosaic
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, roc_auc_score, plot_roc_curve, confusion_matrix, plot_confusion_matrix


# URL = 'https://data.cdc.gov/api/views/vbim-akqf/rows.csv?accessType=DOWNLOAD'
# webbrowser.open_new(URL)

# sleep(60)



@st.cache
def get_data():
	# file_dir = '/Users/rachel.hu/Downloads/COVID-19_Case_Surveillance_Public_Use_Data.csv'
	file_dir = '/Users/rachel.hu/Downloads/temp.csv'
	return pd.read_csv(file_dir)

def clean_missing(df):
	print('\n\n\n\n\nClean Missing\n')
	missing_data = pd.DataFrame(columns=df.columns)
	for row in range(20):
		item = df.iloc[[row]]
		print(item)
		# st.write(type(item['h']))
		if (str(item['icu_yn']) == 'Missing'):
			missing_data.append(item)
			cdc_data.drop(row)
			row -= 1
		# if ((item['sex'] == 'Missing') and (item['race_ethnicity_combined'] == 'Missing') and (item['hosp_yn'] == 'Missing') and (item['icu_yn'] == 'Missing') and (item['death_yn'] == 'Missing') and (item['medcond_yn'] == 'Missing')):
	# 	st.write(item['age_group'])
	# st.write(df.shape)
	print(missing_data)
	print(df.head(20))

def display_head_thousand(df):
	# cdc_data = get_data()
	st.header("CDC data")
	st.dataframe(df.head(1000))

def display_columns(df):
	st.header('Data Points')
	st.write(df.columns)

def display_age_group(df):
	st.header('Age Groups')
	st.write(df['age_group'].value_counts())

	# method 1: NO
	# fig = plt.figure()
	# sns.catplot(x = 'age_group', kind = 'count', data = df, height = 2.5, aspect = .8)
	# st.pyplot(fig)


	# method 2: NO
	# df['age_group'].values_counts().plot(kind='bar')
	# st.pyplot()

	# method 3
	st.bar_chart(df['age_group'].value_counts())

def display_race_ethnicity(df):
	st.header('Race & Ethnicity')
	st.write(df['race_ethnicity_combined'].value_counts())
	st.bar_chart(df['race_ethnicity_combined'].value_counts())

def display_sex(df):
	st.header('Sex')
	st.write(df['sex'].value_counts())
	st.bar_chart(df['sex'].value_counts())

# def display_first_ten(df):
# 	st.header("First Ten")
# 	st.write(df.head(10))

def display_home(df):
	# cdc_data = get_data()
	st.header("CDC data")
	return df.head(1000)

def app():
	cdc_data = get_data()
	clean_missing(cdc_data)
	display_head_thousand(cdc_data)
	display_columns(cdc_data)
	display_age_group(cdc_data)
	display_sex(cdc_data)
	display_race_ethnicity(cdc_data)
	# display_first_ten(cdc_data)


# file_dir = '/Users/rachel.hu/Downloads/COVID-19_Case_Surveillance_Public_Use_Data.csv'
# cdc_data = pd.read_csv(file_dir, index_col=0)
# print(cdc_data.info())