# E-Commerce Sales Analytics

An end-to-end **E-Commerce Sales Analytics** project that analyzes sales, orders, products, categories, cities, payment modes, and order status using **Python, MySQL, and Power BI**.

## Project Overview

The project starts with an unclean e-commerce dataset in Excel. Python is used for data inspection, cleaning, transformation, and feature engineering. The cleaned data is stored in MySQL and analyzed using SQL. Finally, Power BI is used to create an interactive dashboard for business analysis and decision-making.

## Project Workflow

**Raw Excel Data → Python Data Cleaning → MySQL Database → SQL Analysis → Power BI Dashboard → Business Insights**

## Technologies Used

* **Python** – Data cleaning, transformation, and feature engineering
* **Pandas** – Data manipulation and analysis
* **MySQL** – Database storage
* **SQL** – Data analysis and aggregation
* **Power BI** – Interactive dashboard and visualization
* **Excel** – Raw source dataset

## Data Cleaning

The Python script performs the following tasks:

* Loads the raw Excel dataset
* Checks missing values
* Checks duplicate records
* Converts numeric columns into appropriate data types
* Cleans the Discount column
* Converts Order Date and Delivery Date into proper date formats
* Handles missing numeric values
* Calculates Gross Amount
* Calculates Discount Amount
* Calculates Net Amount
* Calculates Delivery Days
* Uploads the cleaned dataset into MySQL

## SQL Analysis

SQL queries are used to analyze:

* Total Sales
* Total Orders
* Average Order Value
* Product-wise Sales
* Category-wise Sales
* City-wise Sales
* Payment Mode-wise Sales
* Order Status Distribution
* Monthly Sales Trend

## Power BI Dashboard

The dashboard provides an interactive view of:

* Total Sales
* Total Orders
* Average Order Value
* Return Rate
* Category-wise Sales
* City-wise Sales
* Product-wise Sales
* Payment Mode-wise Sales
* Monthly Sales Trend
* Order Status Distribution

The dashboard also includes filters for **Category, City, Order Status, and Payment Mode**.

## Key Project Metrics

Based on the current dataset:

| Metric              |  Value |
| ------------------- | -----: |
| Total Sales         | ₹4.31M |
| Total Orders        |    514 |
| Average Order Value | ₹8.39K |
| Return Rate         | 25.29% |

## Project Files

```text
Ecommerce-Sales-Analytics/
│
├── analysis.py
├── ecommerce_analysis.sql
├── Ecommerce_Unclean_Project.xlsx
├── powerbi.pbix
└── README.md
```

## Purpose of the Project

The main objective of this project is to demonstrate an end-to-end **Data Analytics workflow**, from raw data cleaning to database analysis and interactive business reporting.

This project focuses on converting raw e-commerce data into meaningful information that can support business decision-making.

 ## Business Insights & Recommendations
 
### Key Business Insights

1. **Electronics is the strongest category**
   Electronics generates the highest sales among the available product categories, indicating strong customer demand.

2. **Laptop is the top-performing product**
   Laptop generates the highest product-wise sales, making it an important product for inventory and marketing decisions.

3. **Pune is the highest-sales city**
   Pune records the highest sales among the analyzed cities, indicating strong market demand in this location.

4. **Return Rate is 25.29%**
   Approximately one-fourth of orders are being returned. This indicates an area that requires further investigation.

5. **Payment modes show different sales contributions**
   COD, Wallet, NetBanking, UPI, and Card contribute differently to total sales, which can help optimize payment options and promotions.

### Business Recommendations

* Investigate the reasons behind product returns and work on reducing the **25.29% return rate**.
* Maintain sufficient inventory for high-performing **Electronics products**.
* Closely monitor **Laptop inventory** to avoid stock-outs.
* Focus targeted marketing and promotional activities on the **Pune market**.
* Monitor payment-mode performance and make popular payment options easily available to customers.


## Future Improvements

* Add more detailed business insights
* Analyze return reasons
* Add advanced customer analysis
* Create additional Power BI pages
* Add automated data refresh workflow


## Author

**Nishu Shakya**

B.Tech Student | Aspiring Data Analyst

