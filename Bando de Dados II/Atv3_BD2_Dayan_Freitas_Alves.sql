-- 1) Executando a consulta Product Type Profit Measure Query (Q9) com o valor padrão 'green' para o parâmetro COLOR
select
    nation,
    o_year,
    sum(amount) as sum_profit
from (
    select
        n_name as nation,
        extract(year from o_orderdate) as o_year,
        l_extendedprice * (1 - l_discount) - ps_supplycost * l_quantity as amount
    from
        part,
        supplier,
        lineitem,
        partsupp,
        orders,
        nation
    where
        s_suppkey = l_suppkey
        and ps_suppkey = l_suppkey
        and ps_partkey = l_partkey
        and p_partkey = l_partkey
        and o_orderkey = l_orderkey
        and s_nationkey = n_nationkey
        and p_name like '%green%'
) as profit
group by
    nation,
    o_year
order by
    nation,
    o_year desc;

-- 2) Executando a consulta novamente com o valor 'red' para o parâmetro COLOR
select
    nation,
    o_year,
    sum(amount) as sum_profit
from (
    select
        n_name as nation,
        extract(year from o_orderdate) as o_year,
        l_extendedprice * (1 - l_discount) - ps_supplycost * l_quantity as amount
    from
        part,
        supplier,
        lineitem,
        partsupp,
        orders,
        nation
    where
        s_suppkey = l_suppkey
        and ps_suppkey = l_suppkey
        and ps_partkey = l_partkey
        and p_partkey = l_partkey
        and o_orderkey = l_orderkey
        and s_nationkey = n_nationkey
        and p_name like '%red%'
) as profit
group by
    nation,
    o_year
order by
    nation,
    o_year desc;

-- 3) Criar uma consulta ad hoc e documentá-la de acordo com a especificação.
select
    s.s_name as supplier_name,
    extract(year from o.o_orderdate) as order_year,
    sum(l.l_extendedprice * (1 - l.l_discount)) as total_revenue,
    count(distinct o.o_orderkey) as total_orders,
    avg(l.l_discount) as avg_discount,
    max(l.l_discount) as max_discount
from
    supplier s,
    orders o,
    lineitem l
where
    s.s_suppkey = l.l_suppkey
    and o.o_orderkey = l.l_orderkey
    and l.l_extendedprice > (
        select avg(l2.l_extendedprice)
        from lineitem l2
        where l2.l_orderkey = l.l_orderkey
    )
group by
    s.s_name,
    extract(year from o.o_orderdate)
having
    sum(l.l_extendedprice * (1 - l.l_discount)) > [Limite_de_Receita]
order by
    s.s_name asc,
    order_year desc;


-- 4.1 Relatório da quantidade total de encomendas (Orders) para uma região específica
SELECT
    r_name AS region,
    COUNT(o_orderkey) AS total_orders
FROM
    region
JOIN
    nation ON region.r_regionkey = nation.n_regionkey
JOIN
    customer ON nation.n_nationkey = customer.c_nationkey
JOIN
    orders ON customer.c_custkey = orders.o_custkey
WHERE
    r_name = 'AMERICA'
GROUP BY
    r_name;

-- 4.2 Relatório dos recipientes (Containers) e média de tamanho das peças transportadas
SELECT
    p_container AS container,
    AVG(p_size) AS avg_size
FROM
    part
GROUP BY
    p_container
ORDER BY
    avg_size DESC;

-- 4.3 Relatório dos meios de transporte (Shipmode) com somatório e média das taxas (Tax)
SELECT
    l_shipmode AS shipmode,
    COUNT(*) AS total_count,
    SUM(l_tax) AS total_tax,
    AVG(l_tax) AS avg_tax
FROM
    lineitem
GROUP BY
    l_shipmode
ORDER BY
    l_shipmode;

-- 4.4 Relatório: Saldo médio dos clientes por região e nação
SELECT
    r_name AS region,
    n_name AS nation,
    AVG(c_acctbal) AS avg_balance
FROM
    region r
JOIN
    nation n ON r.r_regionkey = n.n_regionkey
JOIN
    customer c ON n.n_nationkey = c.c_nationkey
GROUP BY
    r_name, n_name
ORDER BY
    r_name;

-- 4.5 Relatório: Maior e menor saldo dos fornecedores por região
SELECT
    r_name AS region,
    MAX(s_acctbal) AS max_balance,
    MIN(s_acctbal) AS min_balance
FROM
    region r
JOIN
    nation n ON r.r_regionkey = n.n_regionkey
JOIN
    supplier s ON n.n_nationkey = s.s_nationkey
GROUP BY
    r_name
ORDER BY
    r_name;
