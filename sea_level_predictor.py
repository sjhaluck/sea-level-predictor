import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig = plt.figure(figsize = (12,8))
    plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
    x = range(1880,2050)
    plt.plot(x,intercept + slope*x)

    # Create second line of best fit
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df[df['Year']>=2000]['Year'],df[df['Year']>=2000]['CSIRO Adjusted Sea Level'])
    x2 = range(2000,2050)
    plt.plot(x2, intercept2 + slope2*x2)
    
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()