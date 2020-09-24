import json
import os


reset_input = True
user_input = 0
content = True
exist = True


def instructions():
    print("----- INSTRUÇÕES: -----\n"
          "\n--Para abrir o programa ou site que você deseja digite o nome do site ou arquivo--\n"
          "\n******OBS: Se for abrir algo pela primeira vez digite 'diretorio' e cole o diretório do arquivo.\n"
          "\nEXEMPLO : para abrir o YouTube pela primeira vez digite [diretorio], após isso, digite o nome do site\n"
          "no exemplo, [YouTube ou youtube] pressione enter após, cole o diretório do"
          "youtube (www.youtube.com.br), \nfeito isto a segunda vez que digitar YouTube (não precisa ter letras "
          "maiusculas)\n"
          "o site abrirá sem precisar do diretorio*******\n")


directory = json.load(open('biblioteca.json', 'r', encoding='utf-8', errors='ignore'))


def openapp():

    existing = True
    while existing:

        data = json.load(open('biblioteca.json', 'r', encoding='utf-8', errors='ignore'))
        user_inputs = input(
            "Digite o App ou site que deseje abrir, ou digite, [diretorio] para adicionar novos aplicativos na "
            "memória:\n")

        if user_inputs in data:
            os.startfile(data[user_inputs.lower()])
            print("OK, Estou abrindo o(a) " + user_inputs)
            ok = input("Deseja abrir outro programa?[s/n]\n")
            if ok == 's':
                existing = True
            else:
                existing = False
        elif user_inputs != 'diretorio':
            if user_inputs != 'exit':
                print("Desculpe, não achei o diretório que deseja. Tente incluí-lo na minha biblioteca"
                      " digitando: "
                      "diretorio")
                existing = True

        elif user_inputs == 'diretorio':
            chave = input("Oque você deseja abrir/executar?:\n ")
            chave = chave.lower()
            resp = input("Qual é o diretório do(a) {} ?\n".format(chave))
            resp.replace('"', '')
            directory[chave] = resp
            json.dump(directory, open('biblioteca.json', 'w', encoding='utf-8', errors='ignore'))
            print(directory)

        if user_inputs == 'exit':
            existing = False
