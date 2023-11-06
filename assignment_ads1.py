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

 
def plot_suicides_by_age_group(df, year):
    """Plots a bar chart of the total suicides by age group for a given year.

    Args:
        df: A Pandas DataFrame containing the suicide data.
        year: The year to plot.
    """

    # Filter the data to the specified year
    df_changed = df[df['year'] == year]

    # Group the data by age group and sum the suicides for all countries
    worldsuicides_by_ages = (
        df_changed
        .groupby('age')
        .agg(suicides_no=('suicides_no', 'sum'))
        .reset_index()
    )

    # Sort the age groups in ascending order
    worldsuicides_by_ages = worldsuicides_by_ages.sort_values('age')

    # Create a bar chart of the total suicides by age group
    plt.figure(figsize=(10, 6))
    plt.bar('age', 'suicides_no', data=worldsuicides_by_ages, color='cyan')

    # Add a title, x-axis label, and y-axis label to the chart
    plt.title(f'Total Global Suicides by Age Group, {year}', fontsize=14)
    plt.xlabel('Age Group', fontsize=12)
    plt.ylabel('Total Suicides', fontsize=12)

    # Add grid to the chart
    plt.grid()

    # Turn the labels on the x-axis so that they are easier to see
    plt.xticks(rotation=45)

    # Make the chart look better
    plt.tight_layout()

    # Displaying the chart
    plt.show()

# calling the function
plot_suicides_by_age_group(df, 2015)


# graph 3: Pie Chart 

def plot_suicides_by_sex(df, year):
    """
    Makes a pie chart that shows the percentage of people who died by suicide by gender in a given year.

    Args:
        df: A Pandas DataFrame containing the suicide data.
        year: The year to plot.
    """

    # Filter the data to the specified year.
    df_filtered = df[df['year'] == year]

    # Group the data by sex and sum the suicides for all countries.
    global_suicides_by_sex = (
        df_filtered
        .groupby('sex')
        .agg(suicides_no=('suicides_no', 'sum'))
        .reset_index()
    )

    # Create the pie chart.
    plt.figure(figsize=(8, 8))
    plt.pie(
        global_suicides_by_sex['suicides_no'],
        labels=global_suicides_by_sex['sex'],
        colors=['cyan', 'magenta'],
        autopct='%1.1f%%',
        startangle=140,
    )
    plt.title(f'% of Global Suicides by Gender, {year}', fontsize=14)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()

# calling the function
# here we can see give any year
#plot_suicides_by_sex(df,1995)
plot_suicides_by_sex(df,2015)



 
