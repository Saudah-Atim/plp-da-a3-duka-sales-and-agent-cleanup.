This project contains two data analytics engagements:

Duka Electronics Sales Analysis

Mobile Money Agent Network Data Cleaning and Analysis

Engagement 1: Duka Electronics

This engagement analyses sales data from five branches between January and June 2026.

Executive Summary

The dataset contains 1,000 sales orders from five branches between January and June 2026.

Nairobi recorded the highest revenue of KES 26,106,100 from 376 orders.

Laptops generated the highest product revenue of KES 41,535,000.

Tablets recorded the highest sales volume, with 691 units sold.

Weekdays recorded 723 orders, while weekends recorded 277 orders.

Files

duka_sales_exploration.ipynb – Sales data exploration and analysis.

excel/duka_branch_summary.xlsx – Branch revenue summary, region lookup and PivotTable.

outputs/premium_online_coast_capital.csv – Premium online sales from Nairobi and Mombasa.

Engagement 2: Mobile Money Agent Network

This engagement focuses on cleaning and analysing mobile money agent transactions.

Data Overview

Agents before cleaning: 20 rows.

Transactions before cleaning: 612 rows.

Transactions after removing duplicates: 600 rows.

Duplicate transactions removed: 12.

Files

agent_cleanup.ipynb – Data quality checks, cleaning, merging and analysis.

cleaning_pipeline.py – Function used to clean agent transaction data.

outputs/agent_transactions_clean.csv – Final cleaned transaction dataset.

Running the Notebooks

Open Google Colab.

Upload the project files.

Run generate_data.py to generate the datasets.

Open duka_sales_exploration.ipynb and run all cells.

Open agent_cleanup.ipynb and run all cells.

Requirements

The project uses Python and the following libraries:

pandas

numpy

openpyxl
