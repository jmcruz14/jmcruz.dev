import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
sns.set_theme(style="darkgrid")

df = pd.read_csv('/Users/jccruz/Desktop/IE 198/2 Data Visualization/Datasets (Case Study 2)/ramen-ratings.csv')
df.set_index('Review #', inplace=True)
df.sort_index(inplace=True)

#%%
nissin_raw = df.copy()
nissin = nissin_raw[nissin_raw["Stars"] != "Unrated"]
b = pd.to_numeric(nissin["Stars"])
nissin["Stars"] = b
nissin_1 = nissin[nissin["Brand"] == "Nissin"]
nissin_1.drop(columns=["Brand", "Variety", "Style", "Country", "Top Ten"], inplace=True)

plt.title("Nissin Ramen Rating Distribution", 
          y=1.01,
          fontsize=19)
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)
sns.histplot(nissin_1.Stars, kde=True)
plt.show()

#%%

style_copy = df.copy()

style_copy.drop(columns=['Variety', 'Country', 'Top Ten'], inplace=True)
sc = style_copy[style_copy["Stars"] != "Unrated"]
value_counts = sc['Brand'].value_counts()
remove = value_counts[value_counts < 30].index #to ensure that each restaurant's average rating approximates a normal distribution
sc.replace(remove, np.nan, inplace=True)
sc.dropna(subset=["Brand"], inplace=True)
a = pd.to_numeric(sc["Stars"])
sc["Stars"] = a
sc.drop(columns=["Brand"], inplace=True)

plt.title("Average Ramen Rating According to Style Specialty",
          y=1.01,
          fontsize=17)
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)
sns.boxplot(x="Style", y="Stars", data=sc)

plt.show()

#%%

tt_copy = df.copy()
tt_copy.dropna(subset=["Top Ten"], inplace=True)
tt = tt_copy[tt_copy["Top Ten"] != "\n"]

country_rep = pd.DataFrame(tt["Country"].value_counts().reset_index().values, columns=["Country", "Appearances"])
plt.figure(figsize = (15,8))
plt.title('Frequency of Countries with Top 10 Ramen Products from 2012-2016',
          y=1.01,
          fontsize=25)
plt.xticks(fontsize=13)
plt.yticks(fontsize=17)
ax = sns.barplot(x="Country", y="Appearances", data=country_rep)
plt.show()
