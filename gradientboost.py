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

df_uk['hour'] = df_uk['timestamp'].dt.hour
df_uk['dayofweek'] = df_uk['timestamp'].dt.dayofweek
df_uk['quarter'] = df_uk['timestamp'].dt.quarter
df_uk['month'] = df_uk['timestamp'].dt.month
df_uk['dayofyear'] = df_uk['timestamp'].dt.dayofyear

print("DataFrame Head (69):")
print(df_uk.head())

target_col = 'price'

# --- REVISED Leaner Feature Selection ---
features_cols = [
    'wind_generation', 
    'solar_generation', 
    'load', 
    'hour', 
    'dayofweek'
]

X = df_uk[features_cols]
y = df_uk[target_col]

train_df = df_uk[df_uk['timestamp'].dt.year < 2020]
test_df = df_uk[df_uk['timestamp'].dt.year == 2020]

X_Train = train_df[features_cols]
y_Train = train_df[target_col]

X_Test = test_df[features_cols]
y_Test = test_df[target_col]

import lightgbm as lgb

model = lgb.LGBMRegressor()
model.fit(X_Train, y_Train)

print("Training complete")

from sklearn.metrics import mean_absolute_error

predictions = model.predict(X_Test)

mae = mean_absolute_error(y_Test, predictions)
print(f"Mean Absolute Error: {mae}")

