# cpi-ppi-inflation-trends
## 📘 Overview
This project analyzes U.S. inflation trends by comparing **Consumer Price Index (CPI)** and **Producer Price Index (PPI)** data.  
Using Python, it:
- Loads CPI and PPI “Current” datasets.
- Aggregates yearly changes (2000–2021).
- Plots a **line chart** comparing CPI vs. PPI inflation rates.
- Builds a **correlation heatmap** from a merged CPI/PPI dataframe.

---

## 🧱 Code Structure
- **`src/final_code.py`** — main analysis script:
  - Loads CPI and PPI data files.
  - Filters for relevant years (1999–2021).
  - Computes average yearly inflation rates.
  - Plots:
    - CPI vs. PPI line chart.
    - Correlation heatmap.

- **`src/utils.py`** — helper functions for file reading, data transformation, and aggregation.

