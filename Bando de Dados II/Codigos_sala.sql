-- Lista de fornecedores e suas partes com custo de fornecimento superior à média
SELECT 
    s.s_name AS fornecedor,
    p.p_name AS parte,
    ps.ps_supplycost AS custo_fornecimento
FROM 
    tpch.supplier s
JOIN 
    tpch.partsupp ps ON s.s_suppkey = ps.ps_suppkey
JOIN 
    tpch.part p ON ps.ps_partkey = p.p_partkey
WHERE 
    ps.ps_supplycost > (
        SELECT AVG(ps_supplycost) 
        FROM tpch.partsupp
    )
ORDER BY 
    ps.ps_supplycost DESC;

-- Total de pedidos por segmento de mercado de clientes
SELECT 
    c.c_mktsegment AS segmento_mercado,
    SUM(o.o_totalprice) AS valor_total_pedidos
FROM 
    tpch.customer c
JOIN 
    tpch.orders o ON c.c_custkey = o.o_custkey
GROUP BY 
    c.c_mktsegment
ORDER BY 
    valor_total_pedidos DESC;

-- Países com maior número de pedidos atrasados
SELECT 
    n.n_name AS pais,
    COUNT(*) AS total_pedidos_atrasados
FROM 
    tpch.lineitem l
JOIN 
    tpch.orders o ON l.l_orderkey = o.o_orderkey
JOIN 
    tpch.customer c ON o.o_custkey = c.c_custkey
JOIN 
    tpch.nation n ON c.c_nationkey = n.n_nationkey
WHERE 
    l.l_receiptdate > l.l_shipdate
GROUP BY 
    n.n_name
ORDER BY 
    total_pedidos_atrasados DESC;







-- O_TotalPrice = sum(L_quantity*L_extendedprice*L_discount-1*L_taxa+1);











select distinct p_type 
from tpch.part;
select p_type, count(*)
from tpch.part, tpch.lineitem
where p_partkey = l_partkey
group by p_type; 

select count(*)
from tpch.limeitem;


select count(*)
from part
where p_type is null;


select l_orderkey "Pedido", count(*) "Total de Itens"
from lineitem
group by l_orderkey 
having count(*) > 4
order by count(*) desc; 


select l_returnflag,l_linestatus,
	sum(l_quantity) as sum_qty,
	sum(l_extendedprice) as sum_base_price,
	sum(l_extendedprice*(1-l_discount)) as sum_disc_price,
	sum(l_extendedprice*(1-l_discount)*(1+l_tax)) as sum_charge,
	avg(l_quantity) as avg_qty,
	avg(l_extendedprice) as avg_price,
	avg(l_discount) as avg_disc,
	count(*) as count_order
from lineitem
where l_shipdate >= '1992-01-13'
and l_shipdate <= '1998-10-23'
group by l_returnflag, l_linestatus
order by l_returnflag, l_linestatus;




