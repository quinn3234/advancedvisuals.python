import seaborn as sns 
import matplotlib.pyplot as plt 

df = sns.load_dataset('tips')
df = df.dropna()
print(df.head())
print(df.info)

sns.barplot(x='day', y='total_bill', hue='sex', data=df)
plt.title('Average Total Bill per Day by Gender')
plt.xlabel('Day')
plt.ylabel('Average Bill ($)')
plt.show()

sns.countplot(x='day', hue='sex', data=df)
plt.title('Number of Diners per day by Gender')
plt.xlabel('Day')
plt.ylabel('Count')
plt.show()

sns.boxplot(x='day', y='total_bill', data=df)
plt.title('Spread of Total Bill per Day')
plt.xlabel('Day')
plt.ylabel('Total Bill of ($)')
plt.show()

sns.stripplot(x='day', y='total_bill', data=df)
plt.title('Spread of Total Bill per Day (Strip Plot)')
plt.xlabel('Day')
plt.ylabel('Total Bill of ($)')
plt.show()

sns.swarmplot(x='day', y='total_bill', data=df)
plt.title('Spread of Total Bill per Day (Swarm Plot)')
plt.xlabel('Day')
plt.ylabel('Total Bill of ($)')
plt.show()
