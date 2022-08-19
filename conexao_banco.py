import mysql.connector

class ConectarBanco:

    con = mysql.connector.connect(host='localhost', database='game', user='root', password ='1234')

    if con.is_connected():
        db_info = con.get_server_info()
        print("Conectado ao servidor MySQL versão", db_info)
        cursor = con.cursor() #objeto que permite fazer fazer a interação dos elementos da tabela retornados e
        # lê individualmente cada objeto
        cursor.execute("use game")
        cursor.execute("create table player (name VARCHAR(200));")

        #linha = cursor.fetchone()
        #print(linha)

    if con.is_connected():
        cursor.close()
        con.close()
        print("Conexão ao MySQL foi encerregada")




