select count(c.CustomerId)
from Customer c 
where c.City="Berlin" 
group by c.CustomerId;