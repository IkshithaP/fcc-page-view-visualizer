import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
url="https://raw.githubusercontent.com/freeCodeCamp/boilerplate-page-view-time-series-visualizer/refs/heads/main/fcc-forum-pageviews.csv"
df=pd.read_csv(url,index_col="date",parse_dates=True)
#filtering the dataset
lower_bound = df['value'].quantile(0.025)
upper_bound = df['value'].quantile(0.975)

# Filter the DataFrame to remove outliers
df_cleaned = df[(df['value'] >= lower_bound) & (df['value'] <= upper_bound)]

# Display the cleaned DataFrame
print(df_cleaned.head())
#drawing line plot
def draw_line_plot():
   
   # Set up the figure and axis
    plt.figure(figsize=(12, 6))
    
    # Plot the data
    plt.plot(df.index, df['value'], color='red', linewidth=1)
    
    # Add title and labels
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019", fontsize=16)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Page Views", fontsize=12)
    
    # Format the x-axis ticks
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    
    # Tight layout for better appearance
    plt.tight_layout()
    
    # Save the plot or display it
    plt.savefig("line_plot.png")  # Save as a file (optional)
    plt.show()  # Show the plot

# Call the function
draw_line_plot()

#drawing bar plot
def draw_bar_plot():
    
    
    # Prepare the data for the bar plot
    df['year'] = df.index.year
    df['month'] = df.index.month
    df_bar = df.groupby(['year', 'month'])['value'].mean().unstack()

    # Set up the figure and axis
    fig, ax = plt.subplots(figsize=(12, 6))

    # Plot the bar chart
    df_bar.plot(kind='bar', ax=ax, width=0.8, cmap='tab10')

    # Customize the chart
    ax.set_title("Average Daily Page Views per Month", fontsize=16)
    ax.set_xlabel("Years", fontsize=12)
    ax.set_ylabel("Average Page Views", fontsize=12)
    ax.legend(title="Months", labels=[
        "January", "February", "March", "April", "May", "June", 
        "July", "August", "September", "October", "November", "December"
    ], fontsize=10)

    # Adjust layout for better appearance
    plt.tight_layout()

    # Save the figure and display
    plt.savefig("bar_plot.png")  # Save to file (optional)
    plt.show()

# Call the function
draw_bar_plot()


#drawing box plot
def draw_box_plot():
    
    # Prepare data for box plots
    df['year'] = df.index.year
    df['month'] = df.index.month_name()

    # Sort months for correct order in plots
    df['month'] = pd.Categorical(df['month'], categories=[
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"], ordered=True)

    # Set up the matplotlib figure
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))

    # Year-wise Box Plot (Trend)
    sns.boxplot(ax=axes[0], x="year", y="value", data=df)
    axes[0].set_title("Year-wise Box Plot (Trend)", fontsize=14)
    axes[0].set_xlabel("Year", fontsize=12)
    axes[0].set_ylabel("Page Views", fontsize=12)

    # Month-wise Box Plot (Seasonality)
    sns.boxplot(ax=axes[1], x="month", y="value", data=df)
    axes[1].set_title("Month-wise Box Plot (Seasonality)", fontsize=14)
    axes[1].set_xlabel("Month", fontsize=12)
    axes[1].set_ylabel("Page Views", fontsize=12)

    # Adjust layout and save the figure
    plt.tight_layout()
    plt.savefig("box_plot.png")
    plt.show()

# Call the function
draw_box_plot()
