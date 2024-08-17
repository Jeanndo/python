import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import date2num
from matplotlib.backends.backend_pdf import PdfPages

# Define the phases and their durations
phases = {
    "Initial Planning": 2,
    "Design Phase": 4,
    "Development Phase": {
        "Core Inventory Management": 4,
        "Purchasing Management": 3,
        "Sales Management": 3,
        "Warehouse Management": 2,
        "Reporting and Analytics": 2,
        "User Management and Security": 1,
        "Integrations": 1,
    },
    "Testing Phase": 4,
    "Deployment": 2,
    "Training and Support": "Ongoing",
    "Maintenance and Updates": "Ongoing"
}

# Initialize start date
start_date = pd.to_datetime("2024-08-01")

# Prepare data for Gantt chart
data = []
current_date = start_date
for phase, duration in phases.items():
    if isinstance(duration, int):
        end_date = current_date + pd.DateOffset(weeks=duration)
        data.append([phase, current_date, end_date])
        current_date = end_date
    elif isinstance(duration, dict):
        for subphase, sub_duration in duration.items():
            end_date = current_date + pd.DateOffset(weeks=sub_duration)
            data.append([subphase, current_date, end_date])
            current_date = end_date
    else:
        data.append([phase, current_date, "Ongoing"])

# Convert to DataFrame
df = pd.DataFrame(data, columns=["Phase", "Start", "End"])

# Plot Gantt chart
fig, ax = plt.subplots(figsize=(10, 6))
for idx, row in df.iterrows():
    if row["End"] != "Ongoing":
        ax.barh(row["Phase"], date2num(row["End"]) - date2num(row["Start"]), left=date2num(row["Start"]), color='skyblue')
    else:
        ax.barh(row["Phase"], 1, left=date2num(row["Start"]), color='lightcoral', hatch='/')

ax.xaxis_date()
plt.xlabel('Timeline')
plt.ylabel('Phases')
plt.title('Inventory Management System Development Roadmap')

# Save the figure as an image
fig.savefig("/mnt/data/gantt_chart.png")
plt.close(fig)
