import mysql.connector

def cria_conexao(host, usuario, senha, bd):
    return mysql.connector.connect(host = host, user = usuario, password = senha, database = bd)

def aux_conec(banco): #Preenchimento da conexão
    return cria_conexao("localhost","root","",banco)

def aux_cursor(): #CONEXÃO E CURSOR PARA FAZER O COMANDO
    con = aux_conec("aps")
    cursor = con.cursor() 
    return cursor,con

def encerrar_con(cursor,con): #ENCERRA A CONEXÃO
    cursor.close()
    con.commit()
    con.close()



