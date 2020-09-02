select Track.Name, MediaType.Name 
from Track
Inner Join MediaType 
On Track.MediaTypeId=MediaType.MediaTypeId;