# UK Renewable Generation & Power Price Analysis

## 1. Objective
This project analyses the impact of renewable power generation on wholesale electricity prices in the United Kingdom and develops a baseline predictive model for forecasting prices. The analysis uses hourly data from 2015 to 2020.

## 2. Data Source
The data was sourced from the Open Power System Data (OPSD) project, using their public time series dataset for Europe.

## 3. Methodology
The project was conducted in two phases: exploratory analysis and predictive modelling.

**Exploratory Analysis:** The dataset was loaded and manipulated in Python using the **pandas** library. Key data points for Great Britain, including the day ahead price, actual load, and generation from wind and solar, were selected and cleaned. To analyse the market impact, a 'renewable penetration' metric was engineered by calculating the proportion of total demand met by combined renewables. The relationship between these variables was visualised using **Matplotlib** and **Seaborn**.

**Predictive Modelling:** Following the analysis, a simple Linear Regression model was built using the **scikit-learn** library. The model was trained to predict the `price` (target) using `wind_generation`, `solar_generation`, and `load_actual` as its inputs (features). The data was split into training (80%) and testing (20%) sets chronologically to simulate a real world forecasting scenario.

## 4. Key Findings
The analysis revealed a strong, clear relationship between renewable penetration and electricity price behaviour.

The box plot below illustrates that as the share of demand met by renewables increases, both the median price and price volatility fall dramatically. Hours with **high renewable penetration** show significantly lower prices and an almost complete absence of extreme price spikes.

![Renewable Penetration vs Price](penetration_level_vs_price.png)

The baseline predictive model confirmed this relationship. On the unseen test data, the model achieved a **Mean Absolute Error (MAE) of £9.70**. This means that, on average, the model's price prediction was incorrect by £9.70, providing a solid benchmark and proving that generation and load data have tangible predictive power.

## 5. Further Improvements
* Develop the predictive model by engineering time based features (e.g., hour of day, month) and holiday flags.
* Implement more complex models (e.g., Gradient Boosting, LSTMs) to better capture non linear patterns.
* Incorporate additional data sources, such as natural gas prices and carbon prices (EUAs), which are major drivers of electricity prices.
