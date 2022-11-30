
from conexao import aux_conec, aux_cursor, encerrar_con

def get_user(usuario,senha,coluna_desejada): #FUNÇÃO PARA PEGAR ALGUMA INFORMAÇÃO DA TABELA FUNCIONÁRIO
    cursor,con = aux_cursor()
    comando = ("SELECT {} FROM funcionarios where Usuario='{}' and Senha='{}'".format(coluna_desejada,usuario,senha))
    cursor.execute(comando)
    comando = cursor.fetchall()
    encerrar_con(cursor,con)
    try:
        return comando[0][0]
    except:
        return None
def UserDocs(usuario,senha): #FUNÇÃO PARA PEGAR TODOS OS DOCS DE UM MESMO USUÁRIO
    con = aux_conec("aps")
    cursor = con.cursor()
    docs = []
    cd = get_user(usuario,senha,"CD_func")
    comando = ("SELECT d.Nome FROM  funcionarios f INNER JOIN docs d ON f.CD_func = d.CD_dono where d.CD_dono={};".format(cd))
    cursor.execute(comando)
    resultado = cursor.fetchall()
    encerrar_con(cursor,con)
    print(resultado)
    if (resultado==False): #PARA POSSIVEIS BUGS
        return None
    for x in range(len(resultado)):
        aux = resultado[x][0]
        docs.append(aux)
    print(docs)
    return docs
def carregarDoc(nome,doc): #CARREGA O TEXTO DO DOC SELECIONADO
    if(doc == ""):
        print("Selecione um doc")
        return None
    con = aux_conec("aps")
    cursor = con.cursor()
    comando = ("SELECT d.Texto FROM  funcionarios f INNER JOIN docs d ON f.CD_func = d.CD_dono where f.Nome='{}' and d.Nome='{}';".format(nome,doc))

    cursor.execute(comando)
    resultado = cursor.fetchall()
    encerrar_con(cursor,con)
    return resultado[0][0]
def salvar_txt(usuario,senha,nivel,txt,nome): #SALVA O DOC OU REESCREVE
    con = aux_conec("aps")
    cursor = con.cursor()
    cd_dono = get_user(usuario,senha,"CD_func")
    validador = verifica_duplicata(cd_dono,nome,cursor)
    print(validador)
    if (validador==False):
        comando = ("insert into docs (CD_dono,Nome,Nivel,Texto) values ({},'{}', {},'{}');".format(cd_dono,nome,nivel,txt))
        print("inseriu")
    else:
        comando = ("Update docs set Texto='{}' where CD_dono={} and Nome='{}';".format(txt,cd_dono,nome))
        print("Atualizado")
    cursor.execute(comando)
    cursor.close()
    con.commit()
def verifica_duplicata(cd,nome,cursor): #AUXILIA A FUNÇÃO ANTERIOR PARA VER SE TEM DOCS DUPLICADOS
    comando = ("SELECT d.Nome FROM  funcionarios f INNER JOIN docs d ON f.CD_func = d.CD_dono where d.CD_dono={} and d.Nome='{}';".format(cd,nome))
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print(resultado)
    if (resultado):
        return True
    else:
        return False
def array(coluna_desejada,prioridade):#CARREGA O NOME DOS USUÁRIOS DE MENOR HIERARQUIA
    cursor,con = aux_cursor()
    comando = ("SELECT {} FROM funcionarios where CD_cargo>='{}' order by CD_cargo".format(coluna_desejada,prioridade))
    cursor.execute(comando)
    comando = cursor.fetchall()
    encerrar_con(cursor,con)
    return comando
def docs_outros(nome): # MOSTRA O DOC DOS OUTROS USUÁRIOS AO CLICAR NO NOME DELES
    con = aux_conec("aps")
    comando = ("SELECT Usuario,Senha FROM funcionarios where Nome='{}'".format(nome))
    cursor = con.cursor()
    cursor.execute(comando)
    comando = cursor.fetchall()
    encerrar_con(cursor,con)
    print(comando)
    docs = UserDocs(comando[0][0],comando[0][1])
    return docs   
def insere_dado(nome, usuario, senha, cargo): #FUNÇÃO SEM USO NO MOMENTO, CASO PRECISE INSERIR ALGO
    con = aux_conec("aps")
    cursor = con.cursor()
    comando = "insert into docs (,Texto) values (%s, %s, %s, %s)"
    valor = (nome, usuario, senha, cargo)
    cursor.execute(comando, valor)
    cursor.close()
    con.commit()
    print("inseriu")
def validacao (usuario, senha): #VALIDA USUARIO E SENHA 
    
    validador = get_user(usuario,senha,"*")
    nome = get_user(usuario,senha,"Nome")
    prioridade = get_user(usuario,senha,"CD_cargo")
    if (validador):
        print("validado {}".format(nome))
        aux_doc = 1
    else:
        print("nao validado")
        aux_doc = 2
    return aux_doc,prioridade





