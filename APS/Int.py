# -*- coding: utf-8 -*-
from PySimpleGUI import PySimpleGUI as Int
from validador import array, get_user, UserDocs
#

#
Int.theme('BluePurple')

def menu():
    lyt = [
        [Int.Button('Convolução',size=(15,2)),Int.Button('Biometria',size=(15,2))],
        [Int.VPush()],
        [Int.Button('Sair',size=(5,1))]
        ]
    return Int.Window('Qual deseja iniciar?',lyt,size=(300,150),finalize=True)

def login():
    lyt2 = [
        [Int.Text('Nome: '),Int.Input(key='input1')],
        [Int.Text('Senha '),Int.Input(key='input2',password_char = '*')],
        [Int.Text(' ',key = 'Erro',text_color = 'red'),Int.VPush()],
        [Int.Button('Login',size=(5,1)),Int.Button('Voltar',size=(5,1))]
    ]
    return Int.Window('Login',lyt2,size=(300,150),finalize=True)

def confirma():
    lyt3 = [
        [Int.Text('Insira o nome do documento'),Int.Input("doc",key='nome_doc')],
        [Int.Button('Confirmar',size=(5,1)),Int.Button('Voltar',size=(5,1))]
    ]
    return Int.Window('Salvar',lyt3,size=(300,150),finalize=True)
#

def Docs(nivel,usuario,senha,nome): ### n = Nivel do usuario 1,2 ou 3
    a = array("Nome",nivel)

    colr_layout = [
        [Int.Text('Insira o Nome do documento', key="enun_doc"),Int.Input("doc",key='nome_doc')],
        [Int.Multiline(key='m1',size=(100,28))],
        [Int.Combo(UserDocs(usuario,senha),readonly=True,key='combo',size=(72,3)),Int.Button('Novo',size=(6,3)),Int.Button('Salvar',size=(6,3)),Int.Button('Carregar',size=(6,3))]
        ]
    coll_layout = [
        [Int.Text("Bem vindo {}".format(get_user(usuario,senha,"Nome")),size=(25,2))]
        #[Int.Button('Central',size=(25,2),disabled=True),]
        ]
    print(a)
    i = 1
    while i<=len(a):
        if a[i-1][0] == nome:
            cor = "black"
        else:
            cor = "grey"
        coll_layout.append( [Int.Button(a[i-1][0],size=(25,2),key=a[i-1][0],button_color = cor)]) ### Monta de acordo com o indice no array
        i=i+1
    lyt3 = [
        [Int.Column(coll_layout, element_justification='left', expand_x=True),Int.Column(colr_layout, element_justification='right', expand_x=True)]
        ]   
    return Int.Window('Documentos',lyt3,size=(1000,550),finalize=True)

def IMmenu(karnel,karnel0):
    lyt = [
        [Int.Button('Escolher Imagem',size=(15,2))],
        [Int.Combo(values=karnel,default_value=karnel0,enable_events=True, key='Matriz',size=(20,1)),Int.Button('Enviar',size=(12,1))],
        [Int.Button('Voltar',size=(5,3)),Int.Push()]
        ]
    return Int.Window('Opções de Convolução',lyt,size=(300,120),element_justification='c',finalize=True)