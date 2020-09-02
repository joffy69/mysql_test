select count(plt.TrackId), pl.Name
from Playlist pl, PlaylistTrack plt 
inner join PlaylistTrack on plt.PlaylistId=pl.PlaylistId
group by pl.Name;