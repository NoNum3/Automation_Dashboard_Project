# Automation Dashboard Project

This repository contains a Streamlit-based dashboard for visualizing and analyzing sales data from a Superstore. The dashboard provides various interactive features to explore sales data over time and across different regions, categories, and states. 

## Table of Contents

- [Introduction](#introduction)
- [Setup](#setup)
- [Features](#features)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Superstore Dashboard is designed to facilitate data exploration and analysis of sales data from a Superstore. The dashboard is built using [Streamlit](https://streamlit.io/), a Python library for creating web applications with minimal effort. The project also utilizes [Plotly Express](https://plotly.com/python/plotly-express/) for interactive and visually appealing data visualizations.

## Setup

To run the dashboard locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/NoNum3/Automation_Dashboard_Project.git
   ```

2. Change to the project directory:

   ```bash
   cd Automation_Dashboard_Project
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:

   ```bash
   streamlit run app.py --server.port 8888
   ```

5. Access the dashboard in your web browser at [http://localhost:8501](http://localhost:8501).

## Features

- **File Upload**: Allows users to upload a CSV file containing Superstore sales data.

- **Date Range Selection**: Enables users to filter data based on a specified date range.

- **Multi-level Filters**: Provides interactive sidebar filters for Region, State, and City.

- **Category and Region-wise Sales Visualizations**: Displays bar charts and pie charts for category-wise and region-wise sales, respectively.

- **Data Export**: Allows users to download filtered data as CSV files.

- **Time Series Analysis**: Presents a line chart for time series analysis of sales over different months.

- **Hierarchical Sales Treemap**: Visualizes hierarchical sales data using a treemap for Regions, Categories, and Sub-Categories.

## Usage

1. Upload your Superstore sales data in CSV format using the file upload feature.

2. Use the date range selector and sidebar filters to customize your data view.

3. Explore the interactive charts and visualizations to gain insights into category-wise, region-wise, and time-based sales patterns.

4. Download filtered data for further analysis using the provided download buttons.

## Contributing

If you'd like to contribute to this project, feel free to submit issues or pull requests on the GitHub repository: [https://github.com/NoNum3/Automation_Dashboard_Project](https://github.com/NoNum3/Automation_Dashboard_Project).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.