import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set seaborn style
sns.set(style="darkgrid")

# Load dataset
df = pd.read_csv("world_population.csv")

# Categorize columns
categorical_columns = ["Continent", "Country/Territory"]
numerical_columns = [
    "2022 Population", "2020 Population", "2015 Population", "2010 Population",
    "2000 Population", "1990 Population", "1980 Population", "1970 Population",
    "Area (km²)", "Density (per km²)", "Growth Rate", "World Population Percentage"
]

# Show valid input options
print("\nValid columns for Bar Chart X-axis (categorical):")
for col in categorical_columns:
    print(f"  - {col}")

print("\nValid columns for Bar Chart Y-axis or Histogram (numerical):")
for col in numerical_columns:
    print(f"  - {col}")

# ---- USER INPUT ----
print("\nLet's create a Bar Chart:")
bar_chart_category = input("Enter the column for Bar Chart X-axis (category): ").strip()
bar_chart_value = input("Enter the column for Bar Chart Y-axis (value): ").strip()



# ----- BAR CHART -----
if bar_chart_category in df.columns and bar_chart_value in df.columns:
    grouped_data = df.groupby(bar_chart_category)[bar_chart_value].sum().sort_values(ascending=False)

    plt.figure(figsize=(10, 6))
    sns.barplot(x=grouped_data.index, y=grouped_data.values, palette="Set2")
    plt.title(f"Total {bar_chart_value} by {bar_chart_category}", fontsize=16)
    plt.xlabel(bar_chart_category, fontsize=12)
    plt.ylabel(bar_chart_value, fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
else:
    print(f"\nError: Column '{bar_chart_category}' or '{bar_chart_value}' not found in the dataset.")


# ---- USER INPUT ----
print("\nNow, let's create a Histogram:")
histogram_column = input("Enter the column for Histogram: ").strip()


# ----- HISTOGRAM -----
if histogram_column in df.columns:
    plt.figure(figsize=(10, 6))
    sns.histplot(df[histogram_column], bins=30, kde=True, color="skyblue")
    plt.title(f"Distribution of {histogram_column} Across Countries", fontsize=16)
    plt.xlabel(histogram_column, fontsize=12)
    plt.ylabel("Number of Countries", fontsize=12)
    plt.tight_layout()
    plt.show()
else:
    print(f"\nError: Histogram column '{histogram_column}' not found in the dataset.")
    