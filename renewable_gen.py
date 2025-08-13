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


print("\n Creating plot... ")

sns.boxplot(x='penetration_level', y='price', data=df_uk)

plt.savefig("penetration_level_vs_price.png")