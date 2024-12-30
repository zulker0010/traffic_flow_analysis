import seaborn as sns
from clean_data import df
import numpy as np
import matplotlib.pyplot as plt

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

#histogram of vehicles
fig,axes = plt.subplots(nrows=3, ncols=2, figsize={(20,20)})
colors = ['##491D8B', '#6929C4', '#8A3FFC', 
          '#A56EFF', '#7D3AC1', '#AF4BCE',]

for index, column in enumerate(df.columns):
    if index<6:
        ax = axes.flatten()[index]
        ax.hist(df[column], colors = colors[index], bins=20, edgecolor = "black", alpha = 0.7, label = column)
        ax.legend(loc="best", fontsize = 12)
        ax.set_title(f"Distribution of {column}", fontsize=14)
        ax.set_xlabel(column, fontsize = 12)
        ax.set_ylabel("Frequency", fontsize = 12)
        ax.grid(True, linestyle="--", alpha = 0.6)

plt.suptitle("Traffic Dataset Histograms", size=24, y=1.02)
plt.tight_layout(rect=[0,0,1,0.98])
plt.show()

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

