base = "BASEPROJETO.txt"

arquivo = open(base, 'r')

cnpjs = open('cnpj.txt', 'w')
cpfs = open('cpf.txt', 'w')

def dados_base():
    cadastros_pessoas = []
    for line in arquivo.readlines():
        cadastros_pessoas.append(line.strip(' ').strip('\n'))


def separa_Documento():
    for linha in arquivo:
        if len(arquivo) >= 12:
            cnpjs.write(linha)
        else:
            cpfs.write(linha)

def main():
    dados_base()
    separa_Documento()







if __name__ == "__main__":
    main()