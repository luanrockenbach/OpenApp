import functions
import json
import sys

reset_input = True
user_input = 0
content = True


biblioteca = open('biblioteca.json', 'r+', encoding='utf-8', errors='ignore')

print("--------------### OLÁ ###---------------")
print("Digite 'exit' para fechar")
help_run = input("Gostaria de ler as instruções? [s/n]\n")

while reset_input:
    if 's' in help_run.lower():
        reset_input = False
        functions.instructions()
        while content:
            print('''[ 1 ] Oque é diretório?
[ 2 ] Como achar o diretório que eu desejo?
[ 3 ] Por que este programa existe?
[ 4 ] OK (sair das instruções)
--USE SOMENTE OS NÚMEROS PARA REPRESENTAR SUA DÚVIDA.''')
            nmr = input("Oque desejas saber? \n")
            if nmr == '1':
                print("Diretório é o local onde o arquivo original esta instalado no seu computador ou o "
                      "endereço do seu site\n")
            elif nmr == '2':
                print("Para saber o diretório do arquivo que você deseja, clique com o botão direito do"
                      " mouse\n"
                      "no atalho do arquivo que você deseja adicionar, vá na aba 'propriedades'\n"
                      "copie o destino do atalho e cole quando pedir o diretório. Se você deseja abrir um site,\n"
                      "digite o endereço do site EXEMPLO: www.google.com.br")
            elif nmr == '3':
                print("Me desculpe, eu não sei.\n")
            elif nmr == '4':
                content = False
            else:
                print("Digite somente o número da pergunta\n")

    elif 'n' in help_run.lower():
        print("Ok, você manda")
        reset_input = False
    elif help_run == 'exit':
        sys.exit()
    else:
        print("Digite somente 's' ou 'n' por favor")
        reset_input = True
        help_run = input("Gostaria de ler as instruções? [s/n]\n")

data = json.load(open('biblioteca.json', 'r', encoding='utf-8', errors='ignore'))


functions.openapp()
