# Write your MySQL query statement below
select id, case when p_id IS NULL then "Root" when id IN (Select p_id from Tree) then 'Inner' else 'Leaf' end as type From Tree;