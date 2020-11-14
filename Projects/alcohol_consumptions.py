"""
Created on Mon Jun 11 12:01:34 2018
read external website: 'http://bit.ly/drinksbycountry'
for Python 3.5
"""

import pandas as pd
import matplotlib.pyplot as plt
import os
FILENAME = 'http://bit.ly/drinksbycountry'

drink = pd.read_csv(FILENAME)
drink.drop('continent', axis=1, inplace=True)
drink.rename(columns={'country': 'Country'}, inplace=True)

GDP = pd.read_csv('world_bank.csv', header=4, encoding='utf-8')

# Use dictionary to replace specific values found in column 'Country Name'
country_D = {"Korea, Rep.": "South Korea",
             "Iran, Islamic Rep.": "Iran",
             "Hong Kong SAR, China": "Hong Kong"}
GDP['Country Name'] = GDP['Country Name'].replace(country_D)

GDP.rename(columns={'Country Name': 'Country'}, inplace=True)

df = pd.merge(drink, GDP, how='inner', left_on='Country',
              right_on='Country')

directory = os.getcwd()

fig = plt.figure()
plt.subplot(221)
plt.scatter(df['2015'], df.spirit_servings)
