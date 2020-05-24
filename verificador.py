

base = "BASEPROJETO.txt"

arquivo = open(base, 'r')

DADOS = open('Dados.txt', 'w+')


cpf_primeiro_peso = [10, 9, 8, 7, 6, 5, 4, 3, 2]
cpf_segundo_peso = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

cnpj_primeiro_peso = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
cnpj_segundo_peso = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]


def baseDeDados():
    """
    Essa função pega o BASEPROJETO.txt e formata o arquivo para que 
    os cpfs fiquem em primeiro e os cnpjs por ultimo.

    a função retorna a formatação em forma de uma lista para que eventualmente posssa ser processada em outra função
    retorna uma lista:  cpf_cnpj[]
    """

    cpf_cnpj = []
    for line in arquivo.readlines():
        cpf_cnpj.append(line.strip(' ').strip('\n'))

    

    return cpf_cnpj


def calculaCPF_CNPJ(dado):  # calcula os dois digitos verificadores, tanto do cnpj como o cpf
    """
    a função tem que receber:
    - dado = uma cpf ou um cnpj
    - peso1 = uma lista de pesos para o calculo do primeiro numero verificador (CPF/CNPJ)
    - peso2 = uma lista de pesos para o calculo do segundo  numero verificador (CPF/CNPJ)

    """
    # calcula o primeiro numero verificador do cpf/cnpj
    
    cpf = []
    cnpj = []
    for d in dado:
        primeiro_numero = 0
        if len(d) == 9:
            peso1 = cpf_primeiro_peso
            peso2 = cpf_segundo_peso

        else:
            peso1 = cnpj_primeiro_peso
            peso2 = cnpj_segundo_peso

        for numero, p1 in zip(d, peso1):
            primeiro_numero += int(numero) * p1

        if primeiro_numero % 11 < 2:
            primeiro_numero = 0
        else:
            primeiro_numero = 11 - (primeiro_numero % 11)

        d = d + str(primeiro_numero)

        # calcula o segundo numero verificador do cpf/cnpj
        segundo_numero = 0
        for numero, p2 in zip(d, peso2):
            segundo_numero += int(numero) * p2

        if segundo_numero % 11 < 2:
            segundo_numero = 0
        else:
            segundo_numero = 11 - (segundo_numero % 11)

        
        d = d + str(segundo_numero)
        
        if len(d) == 11:
            cpf.append(d)
        
        else:
            cnpj.append(d)

    for c in cpf:
        DADOS.write(c +'\n')
        
    for c in cnpj:
        DADOS.write(c +'\n')

def main():
    dados = baseDeDados()
    calculaCPF_CNPJ(dados)


if __name__ == "__main__":
    main()
    arquivo.close()


"""
processes = []
for i in range(NUM_PROCESSOS):
    p = Process(target=processa_dado, args=(
        dados, i, cpf_completo, cnpj_completo))  # Passing the list
    p.start() # inicia os mini processos
    processes.append(p)
for p in processes:
    p.join() #faz esperar
"""