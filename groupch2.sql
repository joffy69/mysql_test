select sum(i.UnitPrice*i.Quantity) as "Sales Total"
from InvoiceLine i 
inner join Track t on t.TrackId=i.TrackId
where t.Name ="The Woman King"; 