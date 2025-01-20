import seaborn as sns
from clean_data import df
import numpy as np
import matplotlib.dates as mpl
import matplotlib.pyplot as plt
import pandas as pd

#pairplot for two variables 
car_to_bike = sns.pairplot(df, vars=["CarCount", "BikeCount"],hue="Total")
car_to_bike

#pairplot for multiple variables
multiple_pairplot = sns.set_style("whitegrid")
sns.pairplot(df, vars=["CarCount","BikeCount", "BusCount", "TruckCount", "Total"],
                                 hue="Traffic Situation", 
                                 diag_kind="kde", 
                                 palette="rocket",
                                 height=3, aspect=1.2,
                                 plot_kws={"alpha":0.6}
            )

#code for 3-D Scatterplot
fig = plt.figure(figsize=(12,10))
ax = fig.add_subplot(projection="3d")
colors = np.random.rand(len(df))
scatter = ax.scatter(df['CarCount'], df['BikeCount'], df['BusCount'],
                     c=colors, cmap='hsv', s=100, alpha=0.7)

fig.colorbar(scatter)
ax.set_title("3-D Scatterplot with major vehicles")
ax.set_xlabel("Cars")
ax.set_ylabel("Bike")
plt.show

df.info
df.describe

#traffic situation on each day of the week
plt.figure(figsize=(10,5))
sns.histplot(data=df, x="Day of the week",
                    hue="Traffic Situation", palette="magma", stat="count", kde=True)

vehicle_table = {'vehicles': ["Cars", "Bikes", "Buses", "Trucks"], 
                          'Number of Vehicles': pd.Series([sum(df["CarCount"]),
                                                    sum(df["BikeCount"]),
                                                    sum(df["BusCount"]),
                                                    sum(df["TruckCount"])],
                                                    index=[0,1,2,3]
                                                    )
                        }

vehicle_df = pd.DataFrame(data=vehicle_table, index=[0,1,2,3])
plt.figure(figsize=(10,5))
sns.histplot(data=vehicle_df, x="vehicles", y="Number of Vehicles", hue="Number of Vehicles")

#kernel density estimation for vehicle distribution
for col in 'xy':
 sns.kdeplot(data=vehicle_df["Number of Vehicles"], shade=True)

#time series table for showing peak traffic hours
frequency_table = pd.crosstab(df['Time'], df['Total'])
frequency_table
df['Time'].value_counts()

df.shape
df['Day of the week'].unique()
df['Day of the week'].value_counts(normalize=True)
df.describe()

#converting  time into hours by extracting the hours
df['Hour'] = pd.to_datetime(df['Time'], format='%I:%M:%S %p').dt.hour

#grouping individual and total vehicle count by the hour
vehicle_columns = ['CarCount', 'BikeCount', 'BusCount', 'TruckCount', 'Total']
hourly_data = df.groupby('Hour')[vehicle_columns].sum()

#function for subplotting each vehicle dist in a single plot
def hourly_vehicle_distribution():
    fig, axes = plt.subplots(nrows = 5, ncols = 1,figsize = (10,18), sharex = True)

#Total vehicle distribution for 24 hours 
    sns.lineplot(x=hourly_data.index, 
             y=hourly_data['Total'], 
             palette = 'red',
             marker = 'o',
             ax = axes[0]
             )

    axes[0].set_title("Total Vehicle Count by the Hour")
    axes[0].set_ylabel("Total Number of Vehicles")

#total car distribution for 24 hours
    sns.lineplot(x=hourly_data.index,
             y=hourly_data['CarCount'],
             color = 'orange',
             marker = 'o',
             ax = axes[1]
             )

    axes[1].set_title("Total Car Count by the Hour")
    axes[1].set_ylabel("Total Number of Cars")

    sns.lineplot(x=hourly_data.index,
             y=hourly_data['BikeCount'],
             color = 'blue',
             marker = 'o',
             ax = axes[2]
             )

    axes[2].set_title("Total BikeCount by the Hour")
    axes[2].set_title("Total Number of Bikes")

    sns.lineplot(x=hourly_data.index,
             y=hourly_data["BusCount"],
             color = 'green',
             marker = 'o',
             ax = axes[3]
             )

    axes[3].set_title("Total BusCount by the Hour")
    axes[3].set_ylabel("Total Number of Buses")

    sns.lineplot(x = hourly_data.index,
             y = hourly_data['TruckCount'],
             color = 'brown',
             marker = 'o',
             ax = axes[4]
             )

    axes[4].set_title('Total TruckCount by the Hour')
    axes[4].set_ylabel('Total Number of Trucks')

hourly_vehicle_distribution()