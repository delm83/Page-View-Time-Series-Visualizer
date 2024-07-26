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
print(df)

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots()
    plt.plot(df.index, df['value'])
    ax.xaxis.set_major_locator(plt.MaxNLocator(8))
    plt.title('Daily freeCodeCamp Forum Page Views')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.tight_layout()
    
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    #return fig

def draw_bar_plot():
    pass
    # Copy and modify data for monthly bar plot
    #df_bar = None

    # Draw bar plot





    # Save image and return fig (don't change this part)
    #fig.savefig('bar_plot.png')
    #return fig

def draw_box_plot():
    pass
    # Prepare data for box plots (this part is done!)
    #df_box = df.copy()
    #df_box.reset_index(inplace=True)
    #df_box['year'] = [d.year for d in df_box.date]
    #df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
   



    # Save image and return fig (don't change this part)
    #fig.savefig('box_plot.png')
    #return fig
