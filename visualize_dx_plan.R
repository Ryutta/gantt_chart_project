# Set library path to include user library
.libPaths(c("~/R/library", .libPaths()))

# Load necessary libraries
suppressPackageStartupMessages({
  library(readxl)
  library(vistime)
  library(htmlwidgets)
  library(dplyr)
  library(plotly)
})

# Define file path
file_path <- "dx_plan_2025.xlsx"

# Check if file exists
if (!file.exists(file_path)) {
  stop(paste("File not found:", file_path))
}

# Read the Excel file
df <- read_excel(file_path)

# Prepare data for vistime
# Ensure dates are Date objects
df$Start_Date <- as.Date(df$Start_Date)
df$End_Date <- as.Date(df$End_Date)

# Define colors based on Status
df <- df %>%
  mutate(Color = case_when(
    grepl("Completed", Status) ~ "#28a745", # Green
    Status == "Planned" ~ "#17a2b8",         # Blue
    TRUE ~ "#6c757d"                         # Gray
  ))

# Create the Gantt chart using vistime
# We use plotly engine for interactivity
p <- vistime(df,
             col.event = "Task",
             col.start = "Start_Date",
             col.end = "End_Date",
             col.group = "Category",
             col.color = "Color",
             title = "DX Plan FY2025 Visualization",
             show_labels = TRUE)

# Save the plot as an HTML file
output_file <- "dx_plan_gantt.html"
saveWidget(p, output_file, selfcontained = TRUE)

cat(paste("Successfully created Gantt chart:", output_file, "\n"))
