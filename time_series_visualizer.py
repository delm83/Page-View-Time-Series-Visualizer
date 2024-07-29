import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv').set_index('date')

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) 
     & (df['value'] <= df['value'].quantile(0.975))]
# convert index date values to pandas datetime objects so I can extract years and months
df.index = pd.to_datetime(df.index)

def draw_line_plot():
    # Draw line plot with matplotlib plot method
    fig = plt.figure()
    plt.plot(df.index, df['value'])
    #stretched fig horizontally
    fig.set_figwidth(10)
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.tight_layout()
    
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot, extract years and months for grouping
    df_bar = df
    df_bar['year'] = df_bar.index.strftime('%Y')
    # use numeric month values so I can group them
    df_bar['month'] = df_bar.index.strftime('%m')
    # get the average of values grouped by year and month
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().reset_index().set_index('year')
    # Use pivot to change dataframe from long to wide format and then plot bar chart
    # using dataframe plot method instead of matplotlib plot method (can also use .plot(kind='bar'))
    #df_bar = df_bar.pivot(columns='month')
    print(df_bar)
    # Draw bar plot    Using fig = plt because using dataframe plot method instead of matplotlib plot method
    
    #alternative bar chart using seaborn:
    fig = sns.catplot(x='year', y='value', hue='month', legend=False, palette='colorblind', kind='bar', data=df_bar, errorbar=None)
    #Use the bbox_to_anchor parameter for more fine-grained control, including moving the legend outside of the axes
    plt.legend(labels=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], fontsize=8).set_title('Months')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.tight_layout()
   
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(1,2)
    ax1.set_xlabel('Year')
    ax2.set_xlabel('Month')
    ax1.set_ylabel('Page Views')
    ax2.set_ylabel('Page Views')
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    print(type(ax1))
    # setting palette without setting hue is deprecated
    sns.boxplot(x ='year', y ='value', data = df_box, ax=ax1, hue='year', legend=False, palette='Set2')
    sns.boxplot(x ='month', y ='value', order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], data = df_box, ax=ax2, hue='month', legend=False, palette='colorblind')
    fig.set_figwidth(10)
    plt.tight_layout()

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
