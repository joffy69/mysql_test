select Track.Name, Genre.Name
from Track
inner join Genre
on Track.GenreId=Genre.GenreId
where Genre.Name="Jazz";