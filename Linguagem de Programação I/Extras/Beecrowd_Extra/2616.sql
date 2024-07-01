select id,name
from customers
where id NOT IN(
    select id_customers
    from locations
    )
