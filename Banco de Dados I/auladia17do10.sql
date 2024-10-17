select * from vendas;

select sum(ven_valor_total) "Soma do valor das vendas" 
from vendas; -- Retorma a soma do alor das vendas

select avg(ven_valor_total) "Valor medio de vendas"
from vendas; -- Retorna o valor da media de vendas

select min(ven_valor_total) "Menor valor em venda" 
from vendas; -- Retorna o menor valor de vendas

select max(ven_valor_total) "Maior valor em venda" 
from vendas; -- Retorna o maior valor de vendas 

select count(*) "Número total de vendas" 
from vendas; -- Retorna o total de vendas

select count(*) "Clientes Cadastrados" 
from clientes; -- Quantidade de clientes cadastrados no BD

select * from hist_vendas;
select sum(HVE_QNT_ITENS) "Quantidade de Itens vendidos" 
from hist_vendas; -- Retorna a soma da quantidade de itens vendidos

select * from clientes;
select min(CLI_DATA_NASCIMENTO) 
from clientes; -- Retorna a menor data de nascimento em clientes

select max(CLI_DATA_NASCIMENTO) 
from clientes; -- Retorna o maior data de nascimento em clientes

-- Escreva as Consultas que:
-- 1) Retorne data de cadastro do cliente mais antigo
select min(CLI_DATA_cadastro) "Data de cadastro mais antigo"
from clientes; -- Retorna o cliente mais antigo cadastrado

-- 2) Retorne o somatorio do valor unitário dos produtos de uma categoria especifica
select * from produtos;
select sum(pro_valor_unit) "Soma do valor unitario da categoria 1"
from produtos where pro_cat_codigo = 1; -- Retorna a soma do valor unitario dos produtos de categoria 1

-- 3) Retorne o valor médio dos produtos
select avg(pro_valor_unit) "Valor medio dos produtos"
from produtos; -- Retorna o valor do preço unitario dos produtos cadastrado no BD

-- 4) Retorna a quantidade de produtos vendidos de uma determinada venda
select count(*) 
from hist_vendas where hve_ven_codigo=1;

select sum(hve_qnt_itens) "Quantidade de produtos vendidos na venda 1"
from hist_vendas where hve_ven_codigo =1; -- Retorna a quantidade de produtos vendidos na venda 1