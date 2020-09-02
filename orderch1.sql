select i.InvoiceDate, i.BillingAddress, i.Total
from Invoice i 
order by i.InvoiceDate desc;