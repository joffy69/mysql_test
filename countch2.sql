select count(c.CustomerId) 
from Customer c 
inner join Employee e on e.EmployeeId =  c.SupportRepId
where concat(e.FirstName, ' ',e.LastName)="Jane Peacock";