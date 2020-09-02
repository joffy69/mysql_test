select count(t.TrackId)
from Track t 
inner join MediaType mt on t.MediaTypeId=mt.MediaTypeId
where mt.Name="Purchased AAC audio file";