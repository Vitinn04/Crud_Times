import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Vict@r04',
    database='timescomsql',
)

cursor = conexao.cursor()

def caso1(nomeTime, dataCriacaoTime, paisTime):
    comando = f'INSERT INTO times (nomeTime, dataCriacaoTime, paisTime) VALUES ("{nomeTime}", "{dataCriacaoTime}", "{paisTime}")'
    cursor.execute(comando)
    conexao.commit()

def caso2():
    comando = 'SELECT * FROM times'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    return resultado

def caso3(nomeTime, valor):
    comando = f'UPDATE times SET nomeTime = "{valor}" WHERE nomeTime = "{nomeTime}"'
    cursor.execute(comando)
    conexao.commit()

def caso4(valor):
    comando = f'DELETE FROM times WHERE idTime= "{valor}"'
    cursor.execute(comando)
    conexao.commit()

def caso_padrao():
    return "Opção inválida."

continuar = True
while continuar:
    opcao = int(input("Digite 1 - Inserir | 2 - Ler | 3 - Atualizar | 4 - Deletar: "))

    if opcao == 1:
        nome = input("Digite o nome do time: ")
        data = input("Digite a data de criação do time: ")
        pais = input("Digite o país do time: ")
        caso1(nome, data, pais)
    elif opcao == 2:
        resultado = caso2()
        print(resultado)
    elif opcao == 3:
        nome = input("Digite o nome do time que deseja atualizar: ")
        novo_nome = input("Digite o novo nome do time: ")
        caso3(nome, novo_nome)
    elif opcao == 4:
        idTime = input("Digite o ID do time que deseja deletar: ")
        caso4(idTime)
    else:
        print(caso_padrao())

    continuar_input = input("Deseja continuar inserindo times? (s/n): ")
    if continuar_input.lower() != 's':
        continuar = False

cursor.close()
conexao.close()
