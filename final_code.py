# -*- coding: utf-8 -*-
"""
Ailey Shollenberger
DS 2500
Final Project
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

CPI_FILE = "C:/Users/ailey/DS2500/Final/cu.data.0.Current"
PPI_FILE = "C:/Users/ailey/DS2500/Final/pc.data.0.Current"

def avg_values_df(df):
    
    '''
    function: avg_values_df
    parameters: a dataframe
    returns: a dataframe including mean value and percent change per year 
    '''
    
    df = df.copy()
    df['year'] = df['year'].astype(int)
    df.columns = df.columns.str.strip()
    df['value'] = pd.to_numeric(df['value'], errors='coerce')
    df.dropna(subset=['value'], inplace=True)
    
    # find mean value for each year then calculate inflation rate
    values_df = df.groupby('year')['value'].mean().reset_index()
    values_df['Prev Year Value'] = values_df['value'].shift(1)
    values_df['Inflation Rate'] = (values_df['value'] - values_df['Prev Year Value']) / values_df['Prev Year Value'] * 100
  
    return values_df[['year', 'value', 'Inflation Rate']]

def plot_inflation(cpi_rates, ppi_rates, years):
    
    '''
    function: plot_inflation
    paramters: column values from a dataframe
    returns: a line graph showing percent change per year
        
    '''
    
    fig, ax = plt.subplots(figsize=(8,6))
    
    # plot one line for CPI and one line for PPI
    ax.plot(years, cpi_rates, label='CPI', marker = 'o')
    ax.plot(years, ppi_rates, label='PPI', marker = 'o')
    
    ax.set_xlabel('Years')
    ax.set_ylabel('Inflation Rate')
    ax.set_title('Change Over Time of CPI and PPI Values')
    ax.legend()
    plt.grid()
    plt.show()

def combine_df(cpi_df, ppi_df):
    
    '''
    function: combine_df
    parameters: two dataframes
    returns: one dataframe merged from the two given
    '''
    
    # merge dataframes based on years and rename columns
    merged_df = pd.merge(cpi_df, ppi_df, left_on='year', right_on='year')
    merged_df.rename(columns = {'value_x':'CPI Value'}, inplace=True)
    merged_df.rename(columns = {'value_y':'PPI Value'}, inplace=True)
    merged_df.rename(columns = {'Inflation Rate_x':'CPI Inflation Rate'}, inplace=True)
    merged_df.rename(columns = {'Inflation Rate_y':'PPI Inflation Rate'}, inplace=True)

    return merged_df

def plot_matrix(merged_df, title):
    
    '''
    function: plot_matrix
    parameters: a dataframe, a string for graph title
    returns: a heatmap 
    '''
    
    # include value and inflation rate as variables for matrix
    matrix = merged_df[['CPI Value', 'CPI Inflation Rate', 'PPI Value', 'PPI Inflation Rate']].corr()
    sns.heatmap(matrix, cmap="Greens", annot=True)
    plt.title(title)
    
    plt.show() 

def main():
    
    # use CPI data file to create a CPI dataframe including data from 2000-2021
    cpi_df = pd.read_csv(CPI_FILE, sep='\t')
    years_cpi = cpi_df[(cpi_df['year'] >= 1999) & (cpi_df['year'] <= 2021)]
    cpi_inflation = avg_values_df(years_cpi)
    
    # use PPI data file to create a PPI dataframe including data from 2000-2021
    ppi_df = pd.read_csv(PPI_FILE, sep='\t')
    years_ppi = ppi_df[(ppi_df['year'] >= 1999) & (ppi_df['year'] <= 2021)]
    ppi_inflation = avg_values_df(years_ppi)

    # plot a line graph showing percent change per year for CPI and PPI
    inflation_plot = plot_inflation(cpi_inflation['Inflation Rate'], ppi_inflation['Inflation Rate'], cpi_inflation['year'])
    print(inflation_plot)
    
    # plot correlation matrix using CPI and PPI merged dataframe
    merged_df = (combine_df(cpi_inflation, ppi_inflation))
    print(merged_df)
    cpi_matrix = plot_matrix(merged_df, 'Correlation between CPI and PPI (2000-2021)')
    print(cpi_matrix)
    
main()