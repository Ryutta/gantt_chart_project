# Create library directory if it doesn't exist
lib_dir <- "~/R/library"
if (!dir.exists(lib_dir)) {
  dir.create(lib_dir, recursive = TRUE)
}
.libPaths(c(lib_dir, .libPaths()))

# Install necessary packages
if (!requireNamespace("readxl", quietly = TRUE)) install.packages("readxl", lib = lib_dir, repos = "http://cran.us.r-project.org")
if (!requireNamespace("vistime", quietly = TRUE)) install.packages("vistime", lib = lib_dir, repos = "http://cran.us.r-project.org")
if (!requireNamespace("htmlwidgets", quietly = TRUE)) install.packages("htmlwidgets", lib = lib_dir, repos = "http://cran.us.r-project.org")
if (!requireNamespace("dplyr", quietly = TRUE)) install.packages("dplyr", lib = lib_dir, repos = "http://cran.us.r-project.org")
if (!requireNamespace("plotly", quietly = TRUE)) install.packages("plotly", lib = lib_dir, repos = "http://cran.us.r-project.org")
