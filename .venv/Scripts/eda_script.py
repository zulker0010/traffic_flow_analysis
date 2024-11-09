import seaborn as sns
from clean_data import df

car_to_bike = sns.pairplot(df, vars=["CarCount", "BikeCount"], hue="BikeCount")
car_to_bike