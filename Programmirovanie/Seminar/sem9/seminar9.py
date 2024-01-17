# pip install pandas
import pandas as pd
# california_housing_train.csv
file = 'california_housing_train.csv'
df = pd.read_csv(file)
# print(df)
# print(df.head())
# print(df.tail())
# print(df.shape)
# print(df.columns)
# print(df.info)
# print(df.dtypes)
# print(df.isnull().sum())
# print(df[['median_house_value', 'median_income']])
# print(df['median_house_value'])
# print(df.loc[df.median_income < 2, ['median_house_value', 'median_income']])

# print(df[['longitude', 'latitude']])
# print(df.iloc[: , 0:2])
# Выбрать данные где housing_median_age < 20 и
# median_house_value > 70000
# print(df.loc[(df.housing_median_age < 7) & (df.median_house_value > 360000) & (df.median_house_value < 400000), ['housing_median_age', 'median_house_value']])
# print(df.median_house_value.max(), df.median_house_value.min())
# print(df['median_house_value'].max(), df['median_house_value'].min())
# print(df['median_house_value'].median(), df['median_house_value'].mean())
# avg = df['median_house_value'].median(), df['median_house_value'].mean()

# Показать максимальное median_house_value, где
# median_income = 3.1250
# print(df.loc[df.median_income == 3.125, ['median_house_value', 'median_income']])
# print(df.loc[df.median_income == 3.125, ['median_house_value', 'median_income']].max())

# Узнать какая максимальная population в зоне
# минимального значения median_house_value
# print(df.median_house_value.min())
# print(df.loc[df.median_house_value == df.median_house_value.min(), ['median_house_value', 'population']])
# print(df.loc[df.median_house_value == df.median_house_value.min(), ['median_house_value', 'population']].max())
#
# print('*' * 15)
# print(df.median_house_value.min())
# print(df.median_house_value.max())
# print(df.median_house_value.quantile(.05))
#
# print(df.loc[df.median_house_value <= df.median_house_value.quantile(.05), ['population']].max())

df1 = df.loc[df.median_house_value == df.median_house_value.min(), ['median_house_value', 'population']]
df1.to_csv('new_data1.csv')

df2 = df[['median_house_value', 'population']]
print(df2)
print(type(df2))
df2.to_csv('new_data.csv')
