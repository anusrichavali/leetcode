# Write your MySQL query statement below
select artist, COUNT(artist) as occurrences from Spotify group by artist order by occurrences desc, artist asc;