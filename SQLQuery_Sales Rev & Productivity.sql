SELECT * FROM [dbo].[sales_data]

SELECT
    Region,
    Product,
    SUM(Sales_Amount) AS Total_Revenue
FROM
    [dbo].[sales_data]
GROUP BY
    Region, Product
ORDER BY
    Total_Revenue DESC;

SELECT
    Salesperson_ID,
    SUM(Sales_Amount) AS Total_Sales,
    SUM(Target_Amount) AS Total_Target,
    ROUND(SUM(Sales_Amount) / SUM(Target_Amount) * 100, 2) AS Quota_Percentage
FROM
    sales_data
GROUP BY
    Salesperson_ID
ORDER BY
    Quota_Percentage DESC;

SELECT
    Sales_Date,
    SUM(Sales_Amount) AS Total_Sales
FROM
    sales_data
GROUP BY
    Sales_Date
ORDER BY
    Sales_Date;
SELECT
    Salesperson_ID,
    SUM(Sales_Amount) AS Total_Sales,
    RANK() OVER (ORDER BY SUM(Sales_Amount) DESC) AS Sales_Rank
FROM
    sales_data
GROUP BY
    Salesperson_ID
ORDER BY
    Sales_Rank;
