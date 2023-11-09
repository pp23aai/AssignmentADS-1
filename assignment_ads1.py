# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 20:18:27 2023

@author: Prudhvi vardhan
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# read data from path using pandas 
df = pd.read_csv("C:\\Users\\user\\Downloads\\suicides_data.csv")

# gives first 5 rows and columns of data
df.head()

# gives last 5 rows and columns of data
df.tail()

# gives overview of the data
df.info()

# give statistical overview 
df.describe()

# graph1 :Line chart 

def generate_suicide_timeline(df):
    """
     this function shows the total world suicides of all time ,by region
    """
    
    # mapping each country and dividing in to regions
    # country_region = {'USA': 'Americas', 'France': 'Europe', ...}
    
    country_region = {
    'USA': 'america',
    'Canada': 'america',
    'Brazil': 'america',
    'France': 'europe',
    'Germany': 'europe',
    'Italy': 'europe',
    'China': 'asia',
    'Japan': 'asia',
    'India': 'asia',
 }


    df['region'] = df['country'].map(country_region)
    
    # Now, we group the data by year and region
    yearwise_region = df.groupby(['year', 'region'])['suicides/100k pop'].sum().unstack().reset_index()
    
    # Here , we draw lines for different regions
    plt.figure(figsize=(12, 8))
    for region in  yearwise_region.columns[1:]:
        plt.plot(yearwise_region['year'], yearwise_region[region], marker='*', label=(region))
    
    # adding labelling to data
    plt.title(" Total world wide suicides per 100k Population by region ", fontsize=20)  
    plt.xlabel('Year', fontsize=16)
    plt.ylabel('No. Suicides per 100k Pop', fontsize=16)
    plt.legend(title='Region', loc='upper right')
    plt.grid(True)
    plt.xticks(rotation=60)
    plt.tight_layout()
    plt.show()
    
# calling the function
generate_suicide_timeline(df)


# graph2 : bar chart

def chart_suicide_demographics(data, analysis_year, palette=None):
    """
    Displays a bar chart for suicide demographics based on age for a specified year within the dataset.
    
    Parameters:
    - data: DataFrame containing the suicide statistics.
    - analysis_year: The year for which the statistics are to be analyzed.
    - palette: A list of colors for the bars. If None, default colors will be used.
    
    This function filters the dataset for the given year, calculates the sum of suicides by age group,
    sorts the age groups into a standard order, and then plots a bar chart.
    """
    
    if palette is None:
        palette = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
    
    # Narrow down the dataset to the chosen year
    data_for_year = data[data['year'] == analysis_year]
    
    # Collate the total number of suicides per age bracket
    suicide_tally_by_age = (
        data_for_year.groupby('age', as_index=False)['suicides_no']
        .sum()
        .sort_values(by='suicides_no', ascending=False)
    )
    
    # Define the order of age categories assuming a certain set of age groups
    ordered_ages = ['5-14 years', '15-24 years', '25-34 years', '35-54 years', '55-74 years', '75+ years']
    suicide_tally_by_age['age'] = pd.Categorical(suicide_tally_by_age['age'], categories=ordered_ages, ordered=True)
    
    # Charting
    plt.figure(figsize=(12, 7))
    bars = plt.bar(suicide_tally_by_age['age'], suicide_tally_by_age['suicides_no'], color=palette)
    
    # Customize the chart appearance
    plt.title(f'Suicide Demographics in {analysis_year}', fontsize=18)
    plt.xlabel('Age Category', fontsize=16)
    plt.ylabel('Count of Suicides', fontsize=16)
    plt.xticks(rotation=45)
    plt.yticks(fontsize=13)
    
    # Add a legend if multiple colors are used
    if len(set(palette)) > 1:
        plt.legend(bars, ordered_ages)
    
    # Enhance layout for better presentation
    plt.tight_layout()
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.gca().set_axisbelow(True)
    
    # Show the resulting bar chart
    plt.show()

# Running the function with the dataset for the year 2015
chart_suicide_demographics(df, 2015)



# graph 3: Pie Chart 

def generate_suicide_statistics_chart(dataframe, target_year, chart_colors=None):
    """
    Generates a pie chart displaying the distribution of suicide numbers by gender for a specified year.
    
    Parameters:
    - dataframe: pandas DataFrame containing the suicide data.
    - target_year: Integer representing the year to filter the data by.
    - chart_colors: Optional list of colors for the chart. Default colors are used if not provided.
    
    The function filters the data for the given year, calculates the sum of suicides by gender,
    and then plots a pie chart with the aggregated data.
    """
    
    # Ensure chart colors are provided, or set default colors
    if not chart_colors:
        chart_colors = ['blue', 'red']
    
    # Filter the data for the specified year
    yearly_data = dataframe[dataframe['year'] == target_year]
    
    # Aggregate suicide numbers by gender
    suicide_stats_by_gender = yearly_data.groupby('sex')['suicides_no'].sum().reset_index()
    
    # Plot configuration
    plt.figure(figsize=(10, 6))
    plt.pie(
        suicide_stats_by_gender['suicides_no'],
        labels=suicide_stats_by_gender['sex'],
        colors=chart_colors,
        autopct='%1.1f%%',
        startangle=90
    )
    
    # Set the title of the plot
    plt.title(f'Distribution of Suicides by Gender in {target_year}', fontsize=16)
    
    # Ensuring the pie chart is a circle
    plt.axis('equal')
    
    # Display the plot
    plt.show()

# We'll test this function with the year 1987 and custom colors
generate_suicide_statistics_chart(df , 1987, chart_colors=['lightblue', 'lightcoral'])


 
