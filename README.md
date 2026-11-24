This project contains two data analytics engagements:

1. Duka Electronics Sales Analysis
2. Mobile Money Agent Network Data Cleaning and Analysis

---

## Engagement 1: Duka Electronics

This engagement analyses sales data from five branches between January and June 2026.

### Executive Summary

- The dataset contains 1,000 sales orders.
- Nairobi recorded the highest revenue of KES 26,106,100.
- Laptops generated KES 41,535,000 in revenue.
- Tablets recorded 691 units sold.
- Weekdays recorded 723 orders, while weekends recorded 277 orders.

### Files

- duka_sales_exploration.ipynb
- excel/duka_branch_summary.xlsx
- outputs/premium_online_coast_capital.csv

---

## Engagement 2: Mobile Money Agent Network

This engagement focuses on cleaning and analysing mobile money agent transactions.

### Data Overview

- Agents before cleaning: 20 rows.
- Transactions before cleaning: 612 rows.
- Transactions after removing duplicates: 600 rows.
- Duplicate transactions removed: 12.

### Files

- agent_cleanup.ipynb
- cleaning_pipeline.py
- outputs/agent_transactions_clean.csv

---

## Running the Notebooks

1. Open Google Colab.
2. Upload the project files.
3. Run generate_data.py.
4. Open and run duka_sales_exploration.ipynb.
5. Open and run agent_cleanup.ipynb.

---

## Requirements

- pandas
- numpy
- openpyxl
