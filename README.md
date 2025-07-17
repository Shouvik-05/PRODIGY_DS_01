# 📊 Internship Task-01 Submission
Name: Shouvik Bhattacharjee
Task: Data Visualization using Bar Chart / Histogram
Organization: Prodigy Infotech
Dataset Used: world_population.csv

# ✅ Task Description
Create a bar chart or histogram to visualize the distribution of a categorical or continuous variable using a dataset of your choice.

# 📁 Files Included
File Name	Description
task01_population_analysis.py	Main Python script with interactive input and charts
world_population.csv	Dataset containing world population statistics
README.txt or README.md	This document with description and usage steps

# 🚀 Features of the Script
Displays valid column options before asking for input

User chooses:

Category (e.g., Continent) and Value (e.g., 2022 Population) for Bar Chart

Any continuous column for Histogram

Automatically generates:

A bar chart of totals grouped by category

A histogram showing value distribution across countries

Built using pandas, matplotlib, and seaborn

# 🛠️ How to Run the Project

## 1. Install required libraries:
``` bash
pip install pandas matplotlib seaborn
```

## 2. Make sure these files are in the same folder:

task01_population_analysis.py

world_population.csv

## 3. Run the script:

```bash
python task01_population_analysis.py
```

## 4. Example Input:
``` bash
Enter the column for Bar Chart X-axis (category): Continent
Enter the column for Bar Chart Y-axis (value): 2022 Population
Enter the column for Histogram: 2022 Population
```

