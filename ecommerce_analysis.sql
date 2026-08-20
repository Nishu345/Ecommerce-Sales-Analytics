	USE ecommerce_analytics;

SELECT SUM(Net_Amount) AS Total_Sales
FROM ecommerce_orders;

SELECT COUNT(*) AS Total_Orders
FROM ecommerce_orders;
-- Total Sales
SELECT SUM(Net_Amount) AS Total_Sales
FROM ecommerce_orders;

-- Total Orders
SELECT COUNT(*) AS Total_Orders
FROM ecommerce_orders;

-- Average Order Value
SELECT AVG(Net_Amount) AS Average_Order_Value
FROM ecommerce_orders;

-- Product-wise Sales
SELECT Product, SUM(Net_Amount) AS Total_Sales
FROM ecommerce_orders
GROUP BY Product
ORDER BY Total_Sales DESC;

-- Category-wise Sales
SELECT Category, SUM(Net_Amount) AS Total_Sales
FROM ecommerce_orders
GROUP BY Category
ORDER BY Total_Sales DESC;

-- City-wise Sales
SELECT City, SUM(Net_Amount) AS Total_Sales
FROM ecommerce_orders
GROUP BY City
ORDER BY Total_Sales DESC;

-- Payment Mode-wise Sales
SELECT Payment_Mode, SUM(Net_Amount) AS Total_Sales
FROM ecommerce_orders
GROUP BY Payment_Mode
ORDER BY Total_Sales DESC;

-- Order Status
SELECT Order_Status, COUNT(*) AS Total_Orders
FROM ecommerce_orders
GROUP BY Order_Status;

-- Monthly Sales
SELECT
    YEAR(Order_Date) AS Order_Year,
    MONTH(Order_Date) AS Order_Month,
    SUM(Net_Amount) AS Monthly_Sales
FROM ecommerce_orders
GROUP BY YEAR(Order_Date), MONTH(Order_Date)
ORDER BY Order_Year, Order_Month;