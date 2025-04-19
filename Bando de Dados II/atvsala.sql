select  r_name,n_name
from region,nation
where n_regionkey = r_regionkey
order by r_name;


select c_name, n_name
from customer, nation
where c_nationkey = n_nationkey;

select r_name, count(c_name) as QNT_CLI
from customer, region, nation
where c_nationkey = n_nationkey
and n_regionkey = r_regionkey
group by r_name
having qnt_cli >80;