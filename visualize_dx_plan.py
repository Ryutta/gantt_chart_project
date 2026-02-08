import pandas as pd
import plotly.express as px
import os

# Load data
df = pd.read_excel("dx_plan_2025.xlsx")

# Ensure date format
df['Start_Date'] = pd.to_datetime(df['Start_Date'])
df['End_Date'] = pd.to_datetime(df['End_Date'])

# Sort by Category and Start Date to group tasks visually
df = df.sort_values(by=['Category', 'Start_Date'], ascending=[True, True])

# Define colors based on Status logic similar to R script
# We can't easily map row-by-row colors in px.timeline like R's vistime without a column map.
# So we use 'Status' for color legend.
color_map = {
    "Completed": "#28a745",
    "Completed (実績)": "#28a745",
    "Planned": "#17a2b8"
}
# Fallback for others will be plotly default or we can add more

# Create Gantt chart
# We color by Status to match the R script's visual intent (Completed vs Planned)
fig = px.timeline(
    df,
    x_start="Start_Date",
    x_end="End_Date",
    y="Task",
    color="Status",
    hover_data=["Category", "Progress", "Notes"],
    title="DX Plan FY2025 Visualization",
    color_discrete_map=color_map
)

# Reverse Y axis so first task is at top
fig.update_yaxes(autorange="reversed")

# Ensure directory exists
os.makedirs("docs", exist_ok=True)

# Save
output_file = "docs/index.html"
fig.write_html(output_file)
print(f"Gantt chart saved to {output_file}")
