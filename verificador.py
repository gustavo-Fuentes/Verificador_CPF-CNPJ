base = "BASEPROJETO.txt"

arquivo = open(base, 'r')

cnpjs = open('cnpj.txt', 'a')
cpfs = open('cpf.txt', 'a')


primeiro_verificador_pesos = [10, 9, 8, 7, 6, 5, 4, 3, 2]
segundo_verificador_pesos = [11, 0, 9, 8, 7, 6, 5, 4, 3, 2]


def coleta_separa():

    cadastros_pessoas = []
    for line in arquivo.readlines():
        cadastros_pessoas.append(line.strip(' ').strip('\n'))
        # print(cadastros_pessoas)

    for linha in cadastros_pessoas:
        if len(linha) == 12:
            cnpjs.write(linha + '\n')
        elif len(linha) == 9:
            cpfs.write(linha + '\n')

def calculaCPF():
    algo =[]
    


def main():
    coleta_separa()
    # separa_Documento()



if __name__ == "__main__":
    main()
    arquivo.close()
    cnpjs.close()
    cpfs.close()