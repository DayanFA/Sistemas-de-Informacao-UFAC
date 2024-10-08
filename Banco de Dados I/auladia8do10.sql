SELECT for_codigo, for_nome_fantasia from fornecedores where for_codigo between '003' and '005';
select for_codigo, for_nome_fantasia from fornecedores where for_codigo IN(1,3,5);
SELECT pro_descricao,pro_qnt_disponivel, pro_valor_unit FROM produtos WHERE PRO_CAT_CODIGO ='001';
desc hist_vendas;
SELECT pro_descricao, pro_qnt_disponivel, pro_valor_unit FROM produtos WHERE PRO_VALOR_UNIT >= '50,00';
SELECT cli_codigo, cli_nome, cli_sexo from clientes where cli_nome like 'j%';
SELECT cli_codigo, cli_nome, cli_sexo from clientes where cli_nome like 'A___L%';

