import time
from multiprocessing import Process
base = "BASEPROJETO.txt"

arquivo = open(base, 'r')

DADOS = open('Dados.txt', 'w+') # Output


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


def calculaCPF_CNPJ(dados):  # calcula os dois digitos verificadores, tanto do cnpj como o cpf
    """
    a função recebe uma lista de Dados

    """
    # calcula o primeiro numero verificador do cpf/cnpj
    
    cpf = []
    cnpj = []
    for d in dados:
        primeiro_numero = 0
        if len(d) == 9:
            peso1 = cpf_primeiro_peso
            peso2 = cpf_segundo_peso

        else:
            peso1 = cnpj_primeiro_peso
            peso2 = cnpj_segundo_peso
            
# calcula o primeiro numero verificador do cpf/cnpj

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
        DADOS.write(c +'\n') #adiciona os cpf completos no arquivo DADOS
        
    for c in cnpj:
        DADOS.write(c +'\n') #adiciona os cnpj completos no arquivo DADOS

def main(): 
    
    dados = baseDeDados() # retorna uma lista
    #calculaCPF_CNPJ(dados)
    process = []
    for i in range(4):
        proc = Process(target=calculaCPF_CNPJ, args=(dados, ))
        proc.start() # Inicia os 4 processos
        process.append(proc)
    for p in process:
        p.join() # espera todos os processos acabarem
    


if __name__ == "__main__":
    main()
    # Fechamento dos arquivos, só uma boa prática
    arquivo.close()
    DADOS.close()