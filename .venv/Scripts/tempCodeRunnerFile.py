plt.figure(figsize=(10,5))
sns.histplot(data=df, x="Day of the week", hue="Traffic Situation")