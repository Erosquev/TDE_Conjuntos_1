# ALUNO: Eros Felipe de Quevedo Dos Santos


# ENUNCIADO: 

# Para obter os pontos relativos a este trabalho, você deverá criar um programa, utilizando a
# linguagem Python, C, ou C++. Este programa, quando executado, irá apresentar os resultados de
# operações que serão realizadas entre dois conjuntos de dados.
# O programa que você desenvolverá irá receber como entrada um arquivo de texto (.txt)
# contendo vários conjuntos de dados e várias operações. Estas operações e dados estarão representadas
# em um arquivo de textos contendo apenas os dados referentes as operações que devem ser realizadas
# segundo a seguinte regra fixa: a primeira linha do arquivo de texto de entrada conterá o número de
# operações que estão descritas no arquivo, este número de operações será um inteiro; as linhas
# seguintes seguirão sempre o mesmo padrão de três linhas: a primeira linha apresenta o código da
# operação (U para união, I para interseção, D para diferença e C produto cartesiano), a segunda e
# terceira linhas conterão os elementos dos conjuntos separados por virgulas. A seguir está um exemplo
# das linhas que podem existir em um arquivo de testes para o programa que você irá desenvolver:
# 4
# U
# 3, 5, 67, 7
# 1, 2, 3, 4
# I
# 1, 2, 3, 4, 5
# 4, 5
# D
# 1, A, C, 34
# A, C, D, 23
# C
# 3, 4, 5, 5, A, B, R
# 1, B, C, D, 1
# Neste exemplo temos 4 operações uma união (U), uma interseção (I), um diferença (D) e um
# produto cartesiano (C). A união, definida por U, deverá ser executada sobre os conjuntos {𝟑, 𝟓, 𝟔𝟕, 𝟕} e
# {𝟏, 𝟐, 𝟑, 𝟒}, cujos elementos estão explicitados nas linhas posteriores a definição da operção (U).
# A resposta do seu programa deverá conter a operação realizada, descrita por extenso, os dados
# dos conjuntos identificados, e o resultado da operação. No caso da união a linha de saída deverá conter
# a informação e a formatação mostrada a seguir:
# União: conjunto 1 {3, 5, 67, 7}, conjunto 2 {1, 2, 3, 4}. Resultado: {3, 5, 67, 7, 1, 2, 4}
# Seu programa deverá mostrar a saída no terminal, ou em um arquivo de textos. Em qualquer
# um dos casos, a saída será composta por uma linha de saída para cada operação constante no arquivo
# de textos de entrada formatada segundo o exemplo de saída acima. Observe as letras maiúsculas e
# minúsculas, e os pontos utilizados na formatação da linha de saída apresenta acima.
# No caso do texto de exemplo, teremos 4 linhas, e apenas 4 linhas de saída, formatadas e
# pontuadas conforme o exemplo de saída acima. O uso de linhas extras na saída, ou erros de formatação,
# implicam em perda de pontos como pode ser visto na rubrica de avaliação constante neste documento.

# Para que seu programa possa ser testado você deve criar, no mínimo, três arquivos de entrada
# contendo um número diferente de operações, operações com dados diferentes, e operações em ordem
# diferentes. Os arquivos de entrada criados para os seus testes devem estar disponíveis tanto no
# ambiente repl.it quanto no ambiente Github.
# Observe que o professor irá testar seu programa com os arquivos de testes que você criar e com,
# no mínimo um arquivo de testes criado pelo próprio professor

# #####################################################################################################

# #CÓDIGO:

# Escreva na variável abaixo ou o path do arquivo ou o nome dele se estiver na mesma pasta.

escolhaArquivo = '/Users/eros/Desktop/tde_conjuntos _1/teste3.txt'

# Função que realiza a união dos conjuntos:
def funcao_uniao(arquivo):
    linha = arquivo.readline().strip()
    conj1 = [item.strip() for item in linha.split(',')]  # Remove espaços de cada item que não foram antes removidos pelo strip da linha
    linha = arquivo.readline().strip()
    conj2 = [item.strip() for item in linha.split(',')] # Remove espaços de cada item que não foram antes removidos pelo strip da linha

    # set determina determina os conjuntos que serão utilizados na operação
    conj1 = set(conj1)
    conj2 = set(conj2)
    
    # Operação de união feita com os conjuntos
    conjU = conj1 | conj2

    # Resultado é printado no terminal de saída
    print(f"\nUnião: conjunto 1 {conj1}, conjunto 2 {conj2}.  Resultado: {conjU}")

# Função que realiza a intersecção dos conjuntos: 
def funcao_interseccao (arquivo): 
    linha = arquivo.readline().strip()
    conj1 = [item.strip() for item in linha.split(',')]  # Remove espaços de cada item que não foram antes removidos pelo strip da linha
    linha = arquivo.readline().strip()
    conj2 = [item.strip() for item in linha.split(',')] # Remove espaços de cada item que não foram antes removidos pelo strip da linha
    
    # set determina determina os conjuntos que serão utilizados na operação
    conj1 = set(conj1)
    conj2 = set(conj2)

     # Operação de intersecção feita com os conjuntos
    conjI = conj1 & conj2
    
    # Resultado é printado no terminal de saída
    print(f"\nIntersecção: conjunto 1 {conj1} conjunto 2 {conj2}.  Resultado: {conjI}")

    

def funcao_diferenca(arquivo):
    linha = arquivo.readline().strip()
    conj1 = [item.strip() for item in linha.split(',')]  # Remove espaços de cada item que não foram antes removidos pelo strip da linha
    linha = arquivo.readline().strip()
    conj2 = [item.strip() for item in linha.split(',')] # Remove espaços de cada item que não foram antes removidos pelo strip da linha
    linha = arquivo.readline().strip()

     # set determina determina os conjuntos que serão utilizados na operação
    conj1 = set(conj1)
    conj2 = set(conj2)

    # Operação de diferença feita com os conjuntos
    conjD = conj1 - conj2
    
    # Resultado é printado no terminal de saída
    print(f"\nDiferença: conjunto 1 {conj1}, conjunto 2 {conj2}.  Resultado: {conjD}")


def funcao_produto_cartesiano(arquivo):
    linha = arquivo.readline().strip()
    conj1 = [item.strip() for item in linha.split(',')]  # Remove espaços de cada item que não foram antes removidos pelo strip da linha
    linha = arquivo.readline().strip()
    conj2 = [item.strip() for item in linha.split(',')]  # Remove espaços de cada item que não foram antes removidos pelo strip da linha

    # set determina determina os conjuntos que serão utilizados na operação
    conj1 = set(conj1)
    conj2 = set(conj2)

    # Produto cartesiano feito com os conjuntos
    conjC = [(a, b) for a in conj1 for b in conj2]
            
    # Resultado é printado no terminal de saída
    print(f"\nProduto Cartesiano: conjunto 1 {conj1}, conjunto 2 {conj2}.  Resultado: {conjC}")



# Aqui é onde as funções são chamadas:

# Primeiramente é utilizado um try e except para caso ocorra algum erro na abertura do arquivo selecionado para ser lido
try:
    arquivo = open(escolhaArquivo, "r")   #Arquivo esolhido é aberto
    linha = arquivo.readline().strip()  # é feita a leitura da primeira linha (a qual determina a quantidade de operações a ser feita - sendo esta armazenada na variável numOperacoes.)

    numOperacoes = int(linha)
    idx = 0
    while idx <= numOperacoes:  # é utilizado um loop while para repetir o processo de leitura até que todas as operações descritas no arquivo txt tenham sido executadas
        linha = arquivo.readline().strip()  # é lida a próxima linha que determina qual operação será executada através de if e elif. 
        if linha == "U":     # Dependendo de qual operação estiver no arquivo a correnpondente função será chamada
            funcao_uniao(arquivo) 
            idx+=1   #é incrementado o idx do while a cada função executada

        elif linha == "I":
            funcao_interseccao (arquivo)
            idx+=1
        elif linha == "D":
            funcao_diferenca(arquivo)
            idx+=1
        elif linha == "C":
            funcao_produto_cartesiano(arquivo)
            idx+=1

    arquivo.close()  #Arquivo é fechado após execução das funções

# except utilizado caso ocorra de o arquivo não ser encontrado ou outro erro ocorrer
except FileNotFoundError:
    print(f"Arquivo '{escolhaArquivo}' não encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")



