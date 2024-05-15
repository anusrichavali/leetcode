# Write your MySQL query statement below
select m.symbol as metal, n.symbol as nonmetal from Elements m join Elements n on m.type = "Metal" and n.type = "Nonmetal";