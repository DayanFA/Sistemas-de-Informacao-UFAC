desc clientes;
select cli_codigo, cli_nome, cli_endereco from clientes order by cli_nome ;

select pro_codigo, pro_descricao, pro_valor_unit, pro_valor_unit*1.15 VALOR_REAJUSTADO from produtos;

select distinct cli_endereco from clientes where CLI_ENDERECO is not null ;

select * from clientes;

-- a) Listar todos os produtos das categorias de código 1 e 2 ordenados pelo valor (do mais caro para o mais barato)
desc produtos;
select pro_cat_codigo, PRO_VALOR_UNIT  from produtos  where PRO_CAT_CODIGO = 1 or  PRO_CAT_CODIGO = 2  order by PRO_VALOR_UNIT desc;
-- b) Listar todos os fornecedores ordenados do mais antido para o mais recente
desc fornecedores;
select * from fornecedores order by FOR_DATA_CADASTRO desc; 
-- c) Listar as vendas com valor total maior ou igual a 100
desc vendas;
select * from vendas where VEN_VALOR_TOTAL >=100;


