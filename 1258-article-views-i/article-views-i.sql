# Write your MySQL query statement below
Select DISTINCT viewer_id as id FROM Views WHERE viewer_id = author_id Order By viewer_id ASC;