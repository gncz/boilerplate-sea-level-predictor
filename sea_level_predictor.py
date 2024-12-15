import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv( filepath_or_buffer= "epa-sea-level.csv")
    
    pd.set_option('display.precision', 16)
    
    '''fig, ax = plt.subplots()
    ax.plot(df["Year"], df["CSIRO Adjusted Sea Level"], marker='o', linestyle='None')
    '''
    # Create scatter plot
    
    plt.scatter(data = df, 
            x = "Year", 
            y= "CSIRO Adjusted Sea Level", 
            color="blue"
            )

    # Create first line of best fit
    slope, intercept, r, p, se = linregress(df["Year"], df.iloc[:,1])
    
    df_2050 = pd.DataFrame(columns = ["Year", "Pred", "Pred2"])
    
    df_2050["Year"] = pd.DataFrame(range(1880,2051)).astype(float)
    df_2050["Pred"] = intercept + slope * df_2050["Year"]     
    
    plt.plot( df_2050["Year"], intercept + slope * df_2050["Year"] , color = "green")
       
    # Create second line of best fit
    
    df_2000 = df[ df["Year"]>=2000 ]
    slope2, intercept2, r2, p2, se2 = linregress(df_2000["Year"], df_2000.iloc[:,1])
    df_2050["Pred2"] = intercept2 + slope2 * df_2050["Year"]
    
    plt.plot( range(2000,2051), intercept2 + slope2 * range(2000,2051), color = "red")
    
    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
