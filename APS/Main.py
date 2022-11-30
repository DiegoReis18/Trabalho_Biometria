# -*- coding: utf-8 -*-
import Int as inter
import PySimpleGUI as Int
from validador import carregarDoc, get_user, salvar_txt, validacao, UserDocs, docs_outros
import Convolucao as convo
import Webcam

Int.theme('BluePurple')
wmenu,wlogin,wdoc,wconfirma,wIMmenu,img = inter.menu(), None, None, None,None,None
#-------------------------------------------------------------

while True:
    window,event,values = Int.read_all_windows()
    if event == Int.WINDOW_CLOSED:
       window.hide()
       break
    if event == 'Sair':
       window.hide()
       break
    if event == 'Biometria' and window == wmenu:
        wlogin=inter.login()
        wmenu.hide()
    if event == 'Convolução' and window == wmenu:
        wmenu.hide()
        wIMmenu = inter.IMmenu(convo.getKernels(None),convo.getKernels(0)) 
    if event == 'Escolher Imagem' and window == wIMmenu:
        img = Int.popup_get_file("", no_window=True)
    if event == 'Enviar' and window == wIMmenu:
        a=convo.start(img,values['Matriz']) 
    if event == 'Voltar':
        window.hide()
        wmenu.un_hide()
    if event == 'Login' and window == wlogin:
        usuario = values['input1']
        senha = values['input2']
        print(usuario,senha)
        validador,prioridade = validacao(usuario, senha)
        print(validador,prioridade)
        try:
            if (validador==1):
                wlogin.hide()
                Webcam.Inicio(usuario,senha)
                nome = get_user(usuario,senha,"Nome")
                wdoc=inter.Docs(prioridade,usuario,senha,nome)
                event_anterior = nome
            else:
                window['Erro'].update('Acesso Negado')
        except:
            window['Erro'].update('Acesso Negado')

    if window == wdoc:
        if event == 'Carregar':
            print(values["combo"])
            print(event_anterior)
            texto = carregarDoc(event_anterior,values["combo"])
            window["m1"].update(texto)
            window["enun_doc"].update("Nome do documento carregado")
            window["nome_doc"].update(values['combo'],disabled=True)

        elif event == 'Salvar':
            print(usuario,senha,prioridade,values["m1"],values["nome_doc"])
            i = 0
            salvar_txt(usuario,senha,prioridade,values["m1"],values["nome_doc"])
            window["enun_doc"].update("Documento atual salvo (caso haja um documento com o mesmo nome, ele será sobrescrito)")
            window["combo"].update(values=(UserDocs(usuario,senha)))

        elif event == 'Novo':
            window["enun_doc"].update("Insira o nome do documento")
            window["combo"].update("")
            window["m1"].update("")
            window["nome_doc"].update("doc",disabled=False)
        else:
            docs_central = docs_outros(event)
            window.Element(event_anterior).Update(button_color = ('grey'))
            window.Element(event).Update(button_color = ('Black'))
            if event == nome:
                window["enun_doc"].update("Insira o nome do documento")
                window["Novo"].update(disabled=False)
                window["Salvar"].update(disabled=False)
                window["combo"].update("")
                window["combo"].update(values=(docs_central))
                window["m1"].update("", disabled=False)
                window["nome_doc"].update("doc",disabled=False)
            else:
                window["Novo"].update(disabled=True)
                window["Salvar"].update(disabled=True)
                window["enun_doc"].update("Você está vendo os documentos de {}".format(event))
                window["combo"].update("")
                window["m1"].update("", disabled=True)
                window["nome_doc"].update("",disabled=True)
            print(docs_central)
            window["combo"].update(values=(docs_central))
            event_anterior = event