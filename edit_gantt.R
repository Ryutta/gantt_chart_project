library(openxlsx)

# File path
file_path <- "gantt.xlsx"

# Load existing workbook
# If the file didn't exist, we would use createWorkbook()
if (file.exists(file_path)) {
  wb <- loadWorkbook(file_path)
} else {
  wb <- createWorkbook()
  addWorksheet(wb, "Sheet1")
}

# Create sample data for Gantt Chart
gantt_data <- data.frame(
  Task = c("Requirement Analysis", "System Design", "Implementation", "Testing", "Deployment"),
  Start_Date = as.Date(c("2023-10-01", "2023-10-10", "2023-10-25", "2023-11-15", "2023-11-25")),
  End_Date = as.Date(c("2023-10-09", "2023-10-24", "2023-11-14", "2023-11-24", "2023-11-30")),
  Status = c("Completed", "Completed", "In Progress", "Pending", "Pending"),
  Progress = c(1.0, 1.0, 0.6, 0.0, 0.0)
)

# Write data to the first sheet
# This overwrites existing data starting at cell A1
writeData(wb, sheet = 1, x = gantt_data)

# Adjust column widths for better visibility
setColWidths(wb, sheet = 1, cols = 1:5, widths = c(25, 15, 15, 15, 10))

# Save the workbook
saveWorkbook(wb, file_path, overwrite = TRUE)

cat("Gantt chart data written to", file_path, "\n")
