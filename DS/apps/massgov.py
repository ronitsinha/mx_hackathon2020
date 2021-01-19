
import requests
import pprint
import webbrowser
import streamlit as st
from bs4 import BeautifulSoup

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



#URL = 'https://www.mass.gov/info-details/covid-19-response-reporting#covid-19-interactive-data-dashboard-'
# URL = 'https://www.mass.gov/info-details/archive-of-covid-19-cases-in-massachusetts#january-2021-'
# page = requests.get(URL)

# # pprint.pprint(page.content)

# soup = BeautifulSoup(page.content, 'html.parser')

# site = soup.find('div', class_ = 'main-content main-content--two')
# # print(site)
# # print(type(site))

# data_link = site.find('a')['href']
# print(data_link)
# full_link = 'https://www.mass.gov' + data_link
# print(full_link)

# xlsx_name = data_link.replace('/doc/', '').replace('/download', '')
# # print(xlsx_name)

# months = [('january', 1), ('february', 2), ('march', 3), ('april', 4)]
# for tup in months:
# 	index = xlsx_name.find(tup[0])
# 	if index > -1:
# 		# print('worked')
# 		xlsx_name = xlsx_name.replace(tup[0], str(tup[1]))

# print(xlsx_name)


# chrome_path = '/Applications/Google Chrome.app %s'
# print(chrome_path)

# webbrowser.open_new(full_link)

def display_home(df):
	data_overview = df.parse(sheet_name='Data Documentation')
	return data_overview


def get_data():
	file_dir = '/Users/rachel.hu/Downloads/covid-19-dashboard_1-17-2021.xlsx'

	excel = pd.ExcelFile(file_dir)
	print(excel.sheet_names)
	return excel
# print(type(excel.sheet_names))

# count = 0
# for sheet in excel.sheet_names:
# 	name = 'covid_data_{}'.format(count)
# 	name = excel.parse(sheet)
# 	print("\n\n\n\nNAME\n\n\n", s, "\n\n\n\n")
# 	count+=1




def display_county_city(df):
	county_daily_data = df.parse(sheet_name='County_Daily')
	st.header('County Daily')
	st.dataframe(county_daily_data)

	county_weekly_data = df.parse(sheet_name='County_Weekly')
	st.header('County Weekly')
	st.dataframe(county_weekly_data)

	town_weekly_data = df.parse(sheet_name='Weekly_City_Town')
	st.header('City Weekly')
	st.dataframe(town_weekly_data)

def app():
	get_data()
	display_county_city(get_data())


# covid_data = pd.read_excel(file_dir)
# print(covid_data)

# print(covid_data.head(10))