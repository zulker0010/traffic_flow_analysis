import seaborn as sns
from clean_data import df
import numpy as np
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