Select a.Name as Artist, count(t.TrackId) as "Track Count"
from Artist a 
inner join Album al on a.ArtistId=al.ArtistId
inner join Track t on al.AlbumId=t.AlbumId
group by a.Name
order by count(t.TrackId) desc
limit 5;