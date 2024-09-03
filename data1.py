import pandas as pd
import numpy as np
import os

# List of Microsoft products
products = [
    "Microsoft 365", "Azure", "Dynamics 365", "Windows 10", "Windows 11",
    "Visual Studio", "SQL Server", "Power BI", "OneDrive", "Teams",
    "SharePoint", "Exchange", "Surface Pro", "Surface Laptop", "Xbox",
    "Outlook", "Edge", "Minecraft", "LinkedIn", "GitHub"
]

# Define the dataset structure
data = {
    "Salesperson_ID": np.random.randint(1000, 1050, 100),
    "Region": np.random.choice(["North America", "Europe", "Asia-Pacific", "Latin America"], 100),
    "Product": np.random.choice(products, 100),  # Randomize Microsoft products
    "Sales_Amount": np.round(np.random.uniform(5000, 50000, 100), 2),
    "Target_Amount": np.round(np.random.uniform(10000, 60000, 100), 2),
    "Sales_Date": pd.date_range(start="2023-01-01", periods=100, freq="D"),
    "Quota": np.random.choice(["Met", "Not Met"], 100),
    "Sales_Stage": np.random.choice(["Lead", "Qualified", "Proposal", "Closed"], 100),
}

# Create the DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file on the desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "sales_data.csv")
df.to_csv(desktop_path, index=False)

print(f"Dataset generated and saved to {desktop_path}")
