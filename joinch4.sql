select pl.Name, t.Name, a.Title, ar.Name
from Track t
inner join PlaylistTrack plt on t.TrackId = plt.TrackId
inner join Playlist pl on plt.PlaylistId = pl.PlaylistId
inner join Album a on t.AlbumId = a.AlbumId
inner join Artist ar on a.ArtistId = ar.ArtistId
Where pl.Name = "Grunge"; 