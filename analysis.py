import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Phone_Model": ["iPhone 11", "Samsung A20", "iPhone 11", "Huawei P30", "Samsung A20"],
    "Repair_Type": ["Screen", "Battery", "Battery", "Screen", "Screen"],
    "Cost": [1200, 600, 500, 1100, 700]
}

df = pd.DataFrame(data)

total_revenue = df["Cost"].sum()
print("Total Revenue:", total_revenue)

most_common = df["Repair_Type"].value_counts()
print("\nMost Common Repairs:\n", most_common)

most_common.plot(kind='bar')
plt.title("Most Common Repairs")
plt.xlabel("Repair Type")
plt.ylabel("Count")
plt.show()
