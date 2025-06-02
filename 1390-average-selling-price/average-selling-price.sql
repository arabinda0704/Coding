# Write your MySQL query statement below
select Prices.product_id,ifnull(ROUND(SUM(units*price)/SUM(units),2),0) as average_price from Prices left join UnitsSold on Prices.product_id=UnitsSold.product_id AND
UnitsSold.purchase_date BETWEEN start_date AND end_date
group by product_id;
