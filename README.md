# Energy_Trading_Analysis
An analysis of the relationship between wind generation and wholesale electricity prices in the UK.


# UK Wind Generation & Power Price Analysis

## 1. Objective
This project aims to quantify the impact of wind power generation on wholesale electricity prices (system price) in the United Kingdom.

## 2. Data Sources
- **Power Price Data:** Sourced from the Elexon BMRS API (System Prices).
- **Wind Generation Data:** Sourced from the Elexon BMRS API (Actual Aggregated Wind Generation).

## 3. Methodology
*Data was downloaded programmatically using Python's `requests` library. Timestamps were aligned, and the datasets were merged into a single pandas DataFrame. The relationship between wind generation and system price was analyzed using correlation and visualized with `matplotlib` and `seaborn`.*

## 4. Key Findings
*(This section will be updated with key charts and conclusions.)*



## 5. Potential Further Improvements
- Incorporate demand forecast data to isolate the impact of wind.
- Analyze the impact of interconnector flows with Europe.
- Investigate how the wind/price relationship changes based on the time of day or season.
