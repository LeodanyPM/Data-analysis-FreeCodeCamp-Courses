import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=['date'], index_col='date')

# Clean data
df = df[(df['value']>= df['value'].quantile(0.025)) & (df['value']<= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, _ = plt.subplots(figsize=(14,8))
    plt.plot(df.index, df['value'])
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df2 = df.resample('ME').mean().reset_index()
    df2['Years'] = df2['date'].dt.year
    df2['Months'] = df2['date'].dt.month
    df2['Months'] = df2['Months'].replace({1: 'January', 2: 'February', 3: 'March', 4: 'April',
                                      5: 'May', 6:'June', 7:'July', 8: 'August',
                                      9: 'September', 10: 'October', 11:'November', 
                                      12: 'December'})
    df_bar = df2.pivot_table(index='Years',
                           columns= 'Months',
                           values='value')
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 
                   'July', 'August', 'September', 'October', 'November', 'December']
    df_bar = df_bar[month_names]               
    # Draw bar plot
    fig, ax = plt.subplots(figsize=(14, 8))
    df_bar.plot(kind='bar', width=0.8,ax=ax, figsize=(14, 8))
    ax.set_xlabel('Years', fontsize=12)
    ax.set_ylabel('Average Page Views', fontsize=12)
    ax.legend(title='Months', title_fontsize=12)




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
    months = ['Jan','Feb', 'Mar', 'Apr','May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    sns.boxplot(data=df_box, x='year',hue='year', y='value', ax=ax1)
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')
    sns.boxplot(data=df_box, x='month', y='value',hue='month', ax=ax2, order=months)
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')
    plt.tight_layout()
    plt.show()



    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
