
import sqlite3

conexao = sqlite3.connect('Exercicios_SQL')
cursor = conexao.cursor ()

## 1) Crie uma tabela chamada "alunos" com os seguintes campos: id (inteiro), nome (texto), idade (inteiro) e curso (texto).

cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100)); ')

## 2) Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.

cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (1,"Alessandra",24,"Ciência de Dados")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (2,"João",32,"Educação Física")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (3,"Carlos",19,"Administração")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (4,"Isadora",26,"Economia")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (5,"Joana",28,"Estatística")')

# 3. Consultas Básicas
#Escreva consultas SQL para realizar as seguintes tarefas:
#a) Selecionar todos os registros da tabela "alunos".

dados = cursor.execute('SELECT * FROM alunos ')
for i in dados:
   print(i)

#b) Selecionar o nome e a idade dos alunos com mais de 20 anos.

dados = cursor.execute('SELECT nome, idade FROM alunos WHERE idade>20 ')
for i in dados:
   print(i)

#c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.

dados = cursor.execute('SELECT * FROM alunos WHERE curso = "Engenharia" order by nome ')
for i in dados:
   print(i)

#d) Contar o número total de alunos na tabela

dados = cursor.execute('SELECT count (*) as numero_de_alunos FROM alunos ')
for i in dados:
   print(i)

#4. Atualização e Remoção
#a) Atualize a idade de um aluno específico na tabela.

cursor.execute('UPDATE alunos SET idade=34 WHERE nome="Isadora"')

#b) Remova um aluno pelo seu ID.

cursor.execute ('DELETE FROM alunos where id=5')

#5. Criar uma Tabela e Inserir Dados, crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns registros de clientes na tabela.

cursor.execute('CREATE TABLE clientes(id INT, nome VARCHAR(100), idade INT, saldo FLOAT); ')
cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES (1,"Pedro",19, 2.000)')
cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES (2,"Maria",65,4.000)')
cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES (3,"Fernanda",32,6.000)')
cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES (4,"Josefá",24,7.500)')
cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES (5,"Jasmine",21,8.499)')

#6. Consultas e Funções Agregadas
#Escreva consultas SQL para realizar as seguintes tarefas:
#a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.

dados = cursor.execute('SELECT nome, idade FROM clientes WHERE idade>30 ')
for i in dados:
   print(i)


#b) Calcule o saldo médio dos clientes.

dados = cursor.execute('SELECT (SUM(saldo)/count(*)) as media FROM clientes ')
for i in dados:
   print(i)

#c) Encontre o cliente com o saldo máximo.

dados = cursor.execute('SELECT nome,MAX(saldo) FROM clientes ')
for i in dados:
   print(i)

#d) Conte quantos clientes têm saldo acima de 1000.

dados = cursor.execute('SELECT count (*) FROM clientes WHERE saldo>1.000')
for i in dados:
   print(i)

#7. Atualização e Remoção com Condições
#a) Atualize o saldo de um cliente específico.

cursor.execute('UPDATE clientes SET saldo=14.000 WHERE nome="Pedro"')

#b) Remova um cliente pelo seu ID.

cursor.execute('DELETE from clientes WHERE id=5')

#8. Junção de Tabelas
#Crie uma segunda tabela chamada "compras" com os campos: id
#(chave primária), cliente_id (chave estrangeira referenciando o id
#da tabela "clientes"), produto (texto) e valor (real). Insira algumas
#compras associadas a clientes existentes na tabela "clientes".
#Escreva uma consulta para exibir o nome do cliente, o produto e o
#valor de cada compra

cursor.execute('CREATE TABLE compras(id INT, cliente_id INT, produto VARCHAR(100), valor FLOAT); ')
cursor.execute('INSERT INTO compras(id,cliente_id,produto,valor) VALUES (8,1,"relogio", 4.000)')
cursor.execute('INSERT INTO compras(id,cliente_id,produto,valor) VALUES (10,2,"almofada", 7.000)')
cursor.execute('INSERT INTO compras(id,cliente_id,produto,valor) VALUES (9,3,"tv", 6.000)')
cursor.execute('INSERT INTO compras(id,cliente_id,produto,valor) VALUES (6,4,"Computador", 12.000)')

dados = cursor.execute('SELECT a.nome, b.produto, b.valor FROM clientes a INNER JOIN compras b on a.ID = b.cliente_id')
for i in dados:
   print(i)


conexao.commit()
conexao.close