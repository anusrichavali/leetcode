# Write your MySQL query statement below
select v.customer_id, COUNT(*) as count_no_trans from visits v left join transactions t on t.visit_id = v.visit_id where transaction_id is null group by v.customer_id;