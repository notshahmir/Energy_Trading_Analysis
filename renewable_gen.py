import pandas as pd

df_all = pd.read_csv("/mnt/c/games/time_series_60min_singleindex.csv")

df_uk = df_all[['utc_timestamp', 'GB_GBN_wind_generation_actual', 'GB_GBN_solar_generation_actual', 'GB_GBN_price_day_ahead', 'GB_GBN_load_actual_entsoe_transparency']].copy()

df_uk.rename(
    columns={
        'utc_timestamp': 'timestamp',
        'GB_GBN_wind_generation_actual': 'wind_generation',
        'GB_GBN_solar_generation_actual': 'solar_generation',
        'GB_GBN_price_day_ahead': 'price',
        'GB_GBN_load_actual_entsoe_transparency': 'load'
    },
    inplace=True
)

df_uk['timestamp'] = pd.to_datetime(df_uk['timestamp'])

df_uk.dropna(inplace=True)

df_uk['total_renewables'] = df_uk['wind_generation'] + df_uk['solar_generation']

df_uk['renewable_penetration'] = df_uk['total_renewables'] / df_uk['load']

penetration_level = []

for x in df_uk['renewable_penetration']:
    if x > 0.4:
        penetration_level.append('high')

    elif x < 0.2:
        penetration_level.append('low')
    else:
        penetration_level.append('medium')

df_uk['penetration_level'] = penetration_level


import matplotlib.pyplot as plt

import seaborn as sns



target_col = 'price'
features_cols = ['wind_generation', 'solar_generation', 'load']

X = df_uk[features_cols]
y = df_uk[target_col]


print("--- Data Preparation Complete ---")
print("Features (X) head:")
print(X.head())
print("Target (y) head:")
print(y.head())


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
print("--- Train-Test Split Complete ---")


print(f"Training set size: {len(X_train)} rows")
print(f"Testing set size: {len(X_test)} rows")


from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X_train, y_train)

print("--- Model Training Complete ---")


from sklearn.metrics import mean_absolute_error

predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
print(f"Mean Absolute Error: {mae}")
