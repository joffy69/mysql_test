select concat(c.FirstName,' ', c.LastName) as Name, i.InvoiceDate, i.Total
from Invoice as i 
inner join Customer c on i.CustomerId=c.CustomerId
order by i.Total desc, i.InvoiceDate desc
limit 10;

